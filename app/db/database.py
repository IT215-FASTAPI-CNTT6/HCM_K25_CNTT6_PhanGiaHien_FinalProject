from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings


# Chuỗi kết nối MySQL lấy từ file .env
DATABASE_URL = settings.DATABASE_URL

# Khởi tạo SQLAlchemy Engine để kết nối tới MySQL
engine = create_engine(DATABASE_URL)

# Tạo SessionLocal class, mỗi instance là một session làm việc với database
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
    )

# Base class cho tất cả các ORM models
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
