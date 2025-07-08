from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)
    member_id = models.CharField(max_length=20, unique=True, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_member = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} - {self.get_full_name()}"

    class Meta:
        swappable = 'AUTH_USER_MODEL'