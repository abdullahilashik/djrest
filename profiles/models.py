from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    ''' custome manager for user profile model '''

    def create_user(self, email, name, password=None):
        ''' create a new user profile '''
        if not email:
            raise ValueError('Email is required')

        clean_email = self.normalize_email(email)
        user = self.model(email=clean_email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        pass


class UserProfile(AbstractUser, PermissionsMixin):
    ''' Database model for the custom user table '''
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        ''' get user's full name '''
        return self.name

    def get_short_name(self):
        ''' user short name function / method '''
        return self.name

    def __str__(self):
        ''' string representation of object '''
        return self.email
