FROM python:3.13-slim
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# Python bazasi
FROM python:3.13-slim

# Ishchi papka yaratish
WORKDIR /app

# Bog'lanayotgan fayllarni nusxalash
COPY . /app

# Pip yangilash va kutubxonalarni o‘rnatish
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Django uchun port
EXPOSE 8000

# Migrate va serverni ishga tushirish
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
