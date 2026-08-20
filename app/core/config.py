from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # --- Cấu hình Database ---
    # Đọc từ biến môi trường DATABASE_URL trong file .env
    DATABASE_URL: str

    class Config:
        # Chỉ định file .env để tự động đọc biến môi trường
        env_file = ".env"
        env_file_encoding = "utf-8"


# Khởi tạo một instance duy nhất để dùng cho toàn bộ ứng dụng
settings = Settings()
