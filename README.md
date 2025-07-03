# 🛠️ BirZum - Freelance xizmatlar platformasi (API)

**BirZum** — bu Django REST Framework yordamida yaratilgan, buyurtmachilar va xizmat ko‘rsatuvchilarni bog‘lovchi freelance platformasining API qismi.

## 📌 Funksionallik (MVP)

- 👤 Ro‘yxatdan o‘tish, login/logout (`JWT`)
- 🛒 Buyurtmalar yaratish, ko‘rish
- 💼 Xizmat takliflari yuborish va qabul qilish
- 🧑‍💼 Profil va yo'nalishlar (kategoriya) tanlash
- 🔒 Parolni o‘zgartirish
- 🔐 Token olish va yangilash (JWT auth)
- 📑 Swagger orqali test qilish

---

## 🚀 Texnologiyalar

- `Python 3.13`
- `Django 5.2`
- `Django REST Framework`
- `JWT (SimpleJWT)`
- `drf-yasg (Swagger)`
- `Docker` 
- `Render` server

---

## 📂 API URL'lar

| Endpoint                     | Tavsif                         |
|-----------------------------|--------------------------------|
| `/api/register/`            | Ro‘yxatdan o‘tish              |
| `/api/login/`               | Tizimga kirish (JWT)           |
| `/api/logout/`              | Tizimdan chiqish               |
| `/api/orders/`              | Buyurtmalar ro‘yxati           |
| `/api/my-orders/`           | Mening buyurtmalarim           |
| `/api/offers/`              | Takliflar ro‘yxati             |
| `/api/my-offers/`           | Mening takliflarim             |
| `/api/profile/`             | Profil ko‘rish/yangilash       |
| `/api/categories/`          | Yo‘nalishlar (kategoriya)      |
| `/api/token/`               | JWT token olish                |
| `/api/token/refresh/`       | Token yangilash                |

---

## 🧪 Swagger

👉 Swagger orqali test qilish:  
[`http://127.0.0.1:8000/swagger/`](http://127.0.0.1:8000/swagger/)

---



