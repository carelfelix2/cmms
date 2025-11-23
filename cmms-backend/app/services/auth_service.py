from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.config.settings import settings
import hashlib

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")


class AuthService:
    def __init__(self, db_or_repo):
        # Accept either a SQLAlchemy Session or a prepared UserRepository
        if hasattr(db_or_repo, "query"):
            self.user_repo = UserRepository(db_or_repo)
        else:
            self.user_repo = db_or_repo

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        # normalize input password (handles bcrypt 72-byte limit)
        prepared = self._normalize_password(plain_password)
        return pwd_context.verify(prepared, hashed_password)

    def get_password_hash(self, password: str) -> str:
        pw = self._normalize_password(password)
        return pwd_context.hash(pw)

    def _normalize_password(self, password: str) -> str:
        pw_bytes = password.encode("utf-8")
        if len(pw_bytes) > 72:
            # bcrypt input limited to 72 bytes — pre-hash with SHA256
            # keep the same normalization behaviour for consistency
            return hashlib.sha256(pw_bytes).hexdigest()
        return password

    def create_access_token(self, data: dict, expires_delta: timedelta | None = None) -> str:
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM if hasattr(settings, 'ALGORITHM') else getattr(settings, 'algorithm', 'HS256'))
        return encoded_jwt

    def authenticate_user(self, username: str, password: str):
        user = self.user_repo.get_user_by_username(username)
        if not user:
            return False
        if not self.verify_password(password, user.hashed_password):
            return False
        return user

    def register_user(self, user: UserCreate):
        hashed_password = self.get_password_hash(user.password)
        return self.user_repo.create_user(user, hashed_password)
