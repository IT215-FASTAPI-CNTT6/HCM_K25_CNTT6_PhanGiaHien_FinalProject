from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password


def register_user(
    db: Session,
    user_data: UserCreate
):
    """Đăng ký một tài khoản mới."""

    # Kiểm tra email đã tồn tại hay chưa
    existing_user = db.query(User).filter(
        User.email == user_data.email
    ).first()

    if existing_user:
        return None

    # Tạo user mới
    new_user = User(
        email=user_data.email,
        full_name=user_data.full_name,
        password_hash=hash_password(
            user_data.password
        )
    )

    # Lưu vào database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
