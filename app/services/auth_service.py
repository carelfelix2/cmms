from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from app.repositories.user_repository import UserRepository
from app.config.settings import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:
    def __init__(self, db_or_repo):
        if hasattr(db_or_repo, "query"):
            self.user_repo = UserRepository(db_or_repo)
        else:
            self.user_repo = db_or_repo

    def verify_password(self, plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password):
        return pwd_context.hash(password)

    def create_access_token(self, data: dict, expires_delta: timedelta = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
        return encoded_jwt

    def authenticate_user(self, username: str, password: str):
        user = self.user_repo.get_user_by_username(username)
        if not user:
            return False
        if not self.verify_password(password, user.hashed_password):
            return False
        return user

    def register_user(self, user, hashed_password: str = None):
        if hashed_password is None:
            hashed_password = self.get_password_hash(user.password)
        return self.user_repo.create_user(user, hashed_password)
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserLogin
from app.config.settings import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:
    def __init__(self, db_or_repo):
        # Accept either a Session (db) or an already-constructed UserRepository
        if hasattr(db_or_repo, "query"):
            self.user_repo = UserRepository(db_or_repo)
        else:
            self.user_repo = db_or_repo

    def verify_password(self, plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password):
        return pwd_context.hash(password)

    def create_access_token(self, data: dict, expires_delta: timedelta = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
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
