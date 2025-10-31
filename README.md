# 📰 Article Website Django – README

## 📘 Overview

This backend provides **user authentication** and **article management (blogs & comments)** through RESTful API endpoints.  
It is built using **Django** and **Django REST Framework (DRF)** with support for **JWT authentication** for secure access.

The system allows users to:

- Register and log in (with or without JWT tokens)
- Create, edit, and delete blog posts
- Submit, edit, and remove comments
- Like or dislike blogs and comments
- Activate or deactivate blog visibility

---

## 🔐 Authentication Endpoints (`/auth/`)

### 1️⃣ Signup – Create New User

**POST** `/auth/singin/`

**Body (JSON):**

```json
{
  "first_name": "John",
  "last_name": "Doe",
  "user_name": "john_doe",
  "user_type": "author",
  "password": "your_password"
}
```

**Auth:** None (AllowAny)  
**Success Response:** `201 Created`

```json
{
  "msg": "user created",
  "user": { ... },
  "tokens": {
    "access": "ACCESS_TOKEN",
    "refresh": "REFRESH_TOKEN"
  }
}
```

**Error Responses:**

- `400 Bad Request` → Missing required fields  
- `403 Forbidden` → Username already exists  

---

### 2️⃣ Manual Login – Username + Password

**POST** `/auth/manual-login/`

**Body (JSON):**

```json
{
  "id_code": "john_doe",
  "password": "your_password",
  "remember": true
}
```

**Behavior:**

- If `remember = true` → returns **JWT tokens**
- If `remember = false` → returns user data only  

**Success Response (remember = true):**

```json
{
  "success": "Login successful",
  "tokens": {
    "access": "ACCESS_TOKEN",
    "refresh": "REFRESH_TOKEN"
  },
  "user": { ... }
}
```

**Error Response:**  
`404 Not Found` → Invalid credentials  

---

### 3️⃣ Login via JWT – Preferred Method

**POST** `/auth/login/`

**Headers:**

```
Authorization: Bearer ACCESS_TOKEN
```

**Auth:** None (token verified manually)  
**Success Response:**

```json
{
  "success": "Login successful",
  "user": { ... }
}
```

**Error Response:**  
`400 Bad Request` → Invalid or expired JWT  

---

## 📝 Document (Blog & Comment) Endpoints (`/doc/`)

### 1️⃣ Create Blog

**POST** `/doc/create-blog/`

**Headers:**

```
Authorization: Bearer ACCESS_TOKEN
```

**Body (JSON):**

```json
{
  "title": "My First Blog",
  "description": "Short description here",
  "content": "Full content here...",
  "tags": "django-rest-backend"
}
```

**Success Response:**

```json
{
  "msg": "Blog created",
  "blog": { ... }
}
```

---

### 2️⃣ Submit Comment

**POST** `/doc/sub-comment/`

**Headers:**

```
Authorization: Bearer ACCESS_TOKEN
```

**Body (JSON):**

```json
{
  "content": "This article is awesome!",
  "blog_id": 1
}
```

**Success Response:**

```json
{
  "msg": "Comment submitted",
  "comment": { ... }
}
```

---

### 3️⃣ Edit Blog

**PUT** `/doc/edit-blog/`

**Headers:**

```
Authorization: Bearer ACCESS_TOKEN
```

**Body (JSON):**

```json
{
  "blog_id": 1,
  "new_title": "Updated Title",
  "new_description": "Updated Description",
  "new_content": "Updated content...",
  "new_tags": "django-updated"
}
```

**Success Response:**

```json
{
  "msg": "Blog updated",
  "blog": { ... }
}
```

---

### 4️⃣ Edit Comment

**PATCH** `/doc/edit-comment/`

**Headers:**

```
Authorization: Bearer ACCESS_TOKEN
```

**Body (JSON):**

```json
{
  "commentId": 5,
  "newContent": "Edited comment content"
}
```

**Success Response:**

```json
{
  "msg": "Comment updated",
  "comment": { ... }
}
```

---

### 5️⃣ Remove Blog

**DELETE** `/doc/remove-blog/`

**Headers:**

```
Authorization: Bearer ACCESS_TOKEN
```

**Body (JSON):**

```json
{
  "blog_id": 1
}
```

**Success Response:**

```json
{ "msg": "Blog deleted" }
```

---

### 6️⃣ Remove Comment

**DELETE** `/doc/remove-comment/`

**Headers:**

```
Authorization: Bearer ACCESS_TOKEN
```

**Body (JSON):**

```json
{
  "comentId": 10
}
```

**Success Response:**

```json
{ "msg": "Comment deleted" }
```

---

### 7️⃣ Like Comment

**PATCH** `/doc/like-comment/`

**Headers:**

```
Authorization: Bearer ACCESS_TOKEN
```

**Body (JSON):**

```json
{
  "comment_id": 10
}
```

**Success Response:**

```json
{ "msg": "Comment liked" }
```

---

### 8️⃣ Dislike Comment

**PATCH** `/doc/dislike-comment/`

**Headers:**

```
Authorization: Bearer ACCESS_TOKEN
```

**Body (JSON):**

```json
{
  "comment_id": 10
}
```

**Success Response:**

```json
{ "msg": "Comment disliked" }
```

---

### 9️⃣ Like Blog

**PATCH** `/doc/like-blog/`

**Headers:**

```
Authorization: Bearer ACCESS_TOKEN
```

**Body (JSON):**

```json
{
  "blog_id": 1
}
```

**Success Response:**

```json
{ "msg": "Blog liked" }
```

---

### 🔟 Dislike Blog

**PATCH** `/doc/dislike-blog/`

**Headers:**

```
Authorization: Bearer ACCESS_TOKEN
```

**Body (JSON):**

```json
{
  "blog_id": 1
}
```

**Success Response:**

```json
{ "msg": "Blog disliked" }
```

---

### 1️⃣1️⃣ Deactivate Blog

**PATCH** `/doc/deactive-blog/`

**Headers:**

```
Authorization: Bearer ACCESS_TOKEN
```

**Body (JSON):**

```json
{
  "blog_id": 1
}
```

**Success Response:**

```json
{ "msg": "Blog deactivated" }
```

---

### 1️⃣2️⃣ Activate Blog

**PATCH** `/doc/active-blog/`

**Headers:**

```
Authorization: Bearer ACCESS_TOKEN
```

**Body (JSON):**

```json
{
  "blog_id": 1
}
```

**Success Response:**

```json
{ "msg": "Blog activated" }
```

---

## ⚙️ Authentication Rules Summary

| Endpoint                  | Auth Required | Method | Description                  |
| -------------------------- | ------------- | ------ | ----------------------------- |
| `/auth/singin/`            | ❌             | POST   | User registration             |
| `/auth/manual-login/`      | ❌             | POST   | Manual login (with/without JWT) |
| `/auth/login/`             | ✅             | POST   | JWT login                     |
| `/doc/create-blog/`        | ✅             | POST   | Create blog                   |
| `/doc/sub-comment/`        | ✅             | POST   | Submit comment                |
| `/doc/edit-blog/`          | ✅             | PUT    | Edit blog                     |
| `/doc/edit-comment/`       | ✅             | PATCH  | Edit comment                  |
| `/doc/remove-blog/`        | ✅             | DELETE | Delete blog                   |
| `/doc/remove-comment/`     | ✅             | DELETE | Delete comment                |
| `/doc/like-comment/`       | ✅             | PATCH  | Like comment                  |
| `/doc/dislike-comment/`    | ✅             | PATCH  | Dislike comment               |
| `/doc/like-blog/`          | ✅             | PATCH  | Like blog                     |
| `/doc/dislike-blog/`       | ✅             | PATCH  | Dislike blog                  |
| `/doc/deactive-blog/`      | ✅             | PATCH  | Deactivate blog               |
| `/doc/active-blog/`        | ✅             | PATCH  | Activate blog                 |

---

## 🧠 Tech Stack

- **Django** – Backend framework  
- **Django REST Framework (DRF)** – API serialization & viewsets  
- **JWT Authentication** – Secure token-based authentication  
- **SQLite / PostgreSQL** – Database  
- **Redis (optional)** – Token blacklisting or caching  

---

## 🚀 Quick Start

```bash
# 1️⃣ Clone repository
git clone https://github.com/yourusername/article-website-django.git
cd article-website-django

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Run migrations
python manage.py migrate

# 4️⃣ Start server
python manage.py runserver
```

---

## 🧾 License

This project is licensed under the MIT License.  
Feel free to modify and distribute with attribution.

---

✍️ **Author:** Abolfazl Khezri  
📸 Instagram: [@estariorios](https://www.instagram.com/estariorios)  
🌐 GitHub: [github.com/EstarioRios](https://github.com/estariorios)
