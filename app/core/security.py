from passlib.context import CryptContext


# Cấu hình bcrypt để mã hóa mật khẩu
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password: str) -> str:
    """Mã hóa mật khẩu trước khi lưu vào database."""
    return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:
    """Kiểm tra mật khẩu nhập vào với mật khẩu đã mã hóa."""
    return pwd_context.verify(
        plain_password,
        hashed_password
    )
