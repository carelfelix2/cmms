// Use Vite proxy: call paths under /api -> Vite will forward to backend
const API_PREFIX = '/api'

const TOKEN_KEY = 'cmms_token'

export function setToken(token: string) {
  localStorage.setItem(TOKEN_KEY, token)
}

export function getToken(): string | null {
  return localStorage.getItem(TOKEN_KEY)
}

export function clearToken() {
  localStorage.removeItem(TOKEN_KEY)
}

async function request(path: string, options: RequestInit = {}) {
  const apiPath = path.startsWith('/api') ? path : `${API_PREFIX}${path}`

  const headers: Record<string, string> = {
    'Content-Type': 'application/json',
    ...(options.headers as Record<string, string> || {}),
  }

  const token = getToken()
  if (token) {
    headers['Authorization'] = `Bearer ${token}`
  }

  const res = await fetch(apiPath, { ...options, headers })
  if (!res.ok) {
    const text = await res.text()
    let message = text
    try {
      const json = JSON.parse(text)
      message = json.detail || JSON.stringify(json)
    } catch (_e) {}
    throw new Error(`API request failed: ${res.status} ${message}`)
  }
  // Some endpoints may return empty body
  const contentType = res.headers.get('content-type') || ''
  if (contentType.includes('application/json')) {
    return res.json()
  }
  return null
}

export const apiTest = async () => {
  return request(`/`)
}

export const getAssets = async () => {
  return request(`/assets/`)
}

export const createAsset = async (payload: any) => {
  return request(`/assets/`, { method: 'POST', body: JSON.stringify(payload) })
}

export const registerUser = async (payload: { username: string; email?: string; password: string }) => {
  return request(`/auth/register`, { method: 'POST', body: JSON.stringify(payload) })
}

export const loginUser = async (payload: { username: string; password: string }) => {
  const res = await request(`/auth/login`, { method: 'POST', body: JSON.stringify(payload) })
  // Expect response: { access_token, token_type }
  if (res && res.access_token) {
    setToken(res.access_token)
  }
  return res
}

export const logout = () => {
  clearToken()
}

