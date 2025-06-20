"""
Módulo de autenticación para la API REST.

Incluye funciones para generar y verificar tokens JWT.
Usa el esquema HTTPBearer para autenticación con token Bearer.
"""

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from datetime import datetime, timedelta

# Clave secreta para firmar el token (debe mantenerse segura)
SECRET_KEY = "clave_super_secreta"  
ALGORITHM = "HS256"  # Algoritmo de cifrado
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Tiempo de expiración del token

# Instancia del esquema de autenticación Bearer
auth_bearer = HTTPBearer(auto_error=True)

def crear_token(data: dict, expires_delta: timedelta = None) -> str:
    """
    Crea un token JWT válido por un tiempo determinado.

    Args:
        data (dict): Datos a codificar en el token (por ejemplo, {"sub": "usuario"}).
        expires_delta (timedelta, opcional): Duración del token.

    Returns:
        str: Token JWT generado.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verificar_token(credentials: HTTPAuthorizationCredentials = Depends(auth_bearer)) -> dict:
    """
    Verifica y decodifica un token JWT.

    Args:
        credentials (HTTPAuthorizationCredentials): Token recibido desde el encabezado Authorization.

    Raises:
        HTTPException: Si el token es inválido o ha expirado.

    Returns:
        dict: Información contenida en el token (payload).
    """
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )


