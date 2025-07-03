from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, name='', **extra_fields):
        if not email:
            raise ValueError("Email kiritish majburiy.")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, name='', **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, name, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    is_provider = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return f"{self.user.email} profili"


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.customer.email}"


class Offer(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='offers')
    provider = models.ForeignKey(User, on_delete=models.CASCADE, related_name='offers')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_time = models.IntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"Taklif: {self.order.title} - {self.provider.email}"
