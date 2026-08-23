from datetime import datetime, timedelta, timezone

from jose import jwt
from passlib.context import CryptContext

from app.core.config import settings


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password):
    return pwd_context.hash(password)


def verify_password(password, password_hash):
    return pwd_context.verify(
        password,
        password_hash
    )


def create_access_token(data):
    token_data = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    token_data["exp"] = expire

    return jwt.encode(
        token_data,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )
