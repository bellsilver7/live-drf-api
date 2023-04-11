from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    """
    username(사용자명, 로그인할 때의 '아이디')
    password
    first_name
    last_name
    email
    is_staff
    is_active
    date_joined
    last_login
    """
    profile_image = models.ImageField("프로필 이미지", upload_to="users/profile", blank=True)
    short_description = models.TextField("소개글", blank=True)

    def __str__(self):
        return self.username
