from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = None
    
    # Основные поля
    email = models.EmailField(unique=True, verbose_name='Email')
    country = models.CharField(max_length=100, verbose_name='Страна')
    institution_type = models.CharField(max_length=100, verbose_name='Тип учреждения')
    institution_ownership = models.CharField(max_length=100, verbose_name='Форма собственности')
    user_role = models.CharField(max_length=50, verbose_name='Роль пользователя')
    
    # Даты (created_at уже есть в AbstractUser как date_joined)
    last_login = models.DateTimeField(null=True, blank=True, verbose_name='Последний вход')
    
    # Указываем, что поле email будет использоваться как идентификатор пользователя
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Поля, требуемые для createsuperuser

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'