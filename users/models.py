from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    institution_type = models.CharField(max_length=100)
    institution_ownership = models.CharField(max_length=100)
    user_role = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.email