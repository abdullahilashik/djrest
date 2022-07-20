from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

class UserProfile(AbstractBaseUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=50, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = ['email']
    REQUIRED_FIELDS = ['name']

    def get_short_name(self):
        return self.name
    
    def get_full_name(self):
        return self.name