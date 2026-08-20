````markdown
# Research Management API

Hệ thống quản lý đề tài nghiên cứu khoa học được xây dựng bằng **FastAPI**, sử dụng **MySQL** và **SQLAlchemy**.

## 1. Công nghệ sử dụng

- Python 3.11+
- FastAPI
- SQLAlchemy
- MySQL
- Pydantic
- JWT Authentication
- bcrypt
- Uvicorn
- Pytest
- Swagger/OpenAPI

## 2. Chức năng chính

### Quản lý người dùng

- Đăng ký tài khoản
- Đăng nhập bằng JWT
- Mã hóa mật khẩu bằng bcrypt
- Phân quyền User/Admin
- Xem thông tin tài khoản hiện tại

### Quản lý đề tài nghiên cứu

- Tạo đề tài
- Xem danh sách đề tài
- Xem chi tiết đề tài
- Cập nhật đề tài
- Xóa đề tài
- Tìm kiếm đề tài
- Lọc theo trạng thái
- Phân trang
- Sắp xếp dữ liệu

### Quản lý thành viên

- Thêm thành viên vào đề tài
- Xem thành viên của đề tài
- Xóa thành viên
- Kiểm tra quyền truy cập theo thành viên

### Quản lý công việc

- Tạo công việc cho đề tài
- Xem danh sách công việc
- Cập nhật công việc
- Xóa công việc
- Lọc theo trạng thái
- Lọc theo người được giao
- Phân trang và sắp xếp

## 3. Cấu trúc project

```text
research_management/
│
├── app/
│   ├── main.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── database.py
│   │   └── security.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── project.py
│   │   ├── member.py
│   │   └── task.py
│   │
│   ├── schemas/
│   │   ├── user.py
│   │   ├── project.py
│   │   ├── member.py
│   │   └── task.py
│   │
│   ├── routers/
│   │   ├── auth.py
│   │   ├── users.py
│   │   ├── projects.py
│   │   ├── members.py
│   │   └── tasks.py
│   │
│   └── dependencies.py
│
├── tests/
│
├── .env.example
├── requirements.txt
├── README.md
└── pytest.ini
````

## 4. Cài đặt

### Bước 1: Tạo môi trường ảo

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Bước 2: Cài đặt thư viện

```bash
pip install -r requirements.txt
```

## 5. Cấu hình MySQL

Tạo database:

```sql
CREATE DATABASE research_management
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
```

Sau đó tạo file `.env` từ `.env.example`.

Ví dụ:

```env
DATABASE_URL=mysql+pymysql://root:password@localhost:3306/research_management

SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

Thay `root`, `password` và các thông tin kết nối bằng thông tin MySQL của máy.

## 6. Chạy server

```bash
uvicorn app.main:app --reload
```

Server mặc định chạy tại:

```text
http://127.0.0.1:8000
```

## 7. Swagger API

Sau khi chạy server, truy cập:

```text
http://127.0.0.1:8000/docs
```

Swagger cho phép xem và trực tiếp thử nghiệm toàn bộ API.

OpenAPI JSON:

```text
http://127.0.0.1:8000/openapi.json
```

## 8. Xác thực

Hệ thống sử dụng JWT Bearer Token.

Sau khi đăng nhập thành công, lấy `access_token` và sử dụng trong Swagger bằng nút:

```text
Authorize
```

Nhập:

```text
Bearer <access_token>
```

Các API yêu cầu đăng nhập sẽ sử dụng token này để xác thực.

## 9. Phân quyền

Hệ thống có hai vai trò:

* `user`: người dùng thông thường
* `admin`: quản trị viên

Các API có kiểm tra quyền truy cập trước khi thực hiện thao tác.

Người dùng chỉ có thể thao tác với những dữ liệu mà họ có quyền truy cập.

## 10. Các API chính

### Authentication

```text
POST /auth/register
POST /auth/login
GET  /users/me
```

### Research Projects

```text
POST   /projects
GET    /projects
GET    /projects/{project_id}
PUT    /projects/{project_id}
DELETE /projects/{project_id}
```

Có hỗ trợ:

* Tìm kiếm
* Lọc
* Phân trang
* Sắp xếp

### Project Members

```text
POST   /projects/{project_id}/members
GET    /projects/{project_id}/members
DELETE /projects/{project_id}/members/{member_id}
```

### Research Tasks

```text
POST   /projects/{project_id}/tasks
GET    /projects/{project_id}/tasks
GET    /projects/{project_id}/tasks/{task_id}
PUT    /projects/{project_id}/tasks/{task_id}
DELETE /projects/{project_id}/tasks/{task_id}
```

## 11. Kiểm tra hệ thống

Chạy test:

```bash
pytest
```

Kiểm tra server:

```text
GET /health
```

Nếu hệ thống hoạt động bình thường, endpoint health sẽ trả về trạng thái thành công.

## 12. Xử lý lỗi

API sử dụng HTTP status code phù hợp, ví dụ:

```text
200 OK
201 Created
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
422 Unprocessable Entity
500 Internal Server Error
```

Các dữ liệu đầu vào được kiểm tra bằng Pydantic trước khi xử lý.

## 13. Những chức năng không triển khai

Theo yêu cầu, project chỉ tập trung vào các chức năng bắt buộc.

Không triển khai các chức năng mở rộng như:

* Refresh Token
* Rate Limiting
* Seed dữ liệu tự động
* Activity Log
* Soft Delete
* Comment
* File Attachment

Các chức năng trên có thể được bổ sung sau nếu cần.

## 14. Mục tiêu thiết kế

Project được tổ chức theo hướng modular để dễ:

* Phát triển thêm chức năng
* Bảo trì
* Kiểm thử
* Phân quyền
* Mở rộng API
* Kết nối với frontend sau này

Backend hiện tại tập trung vào API và cơ sở dữ liệu, không bao gồm giao diện frontend.
