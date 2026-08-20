from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Tạo engine kết nối database
engine = create_engine(
    setting.DATABASE_URL,
    # Kiểm tra kết nối database trước khi lấy nó ra sử dụng.
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind = engine
)

Base = declarative_base()

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()