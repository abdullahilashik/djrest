from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

class UserProfileManager(BaseUserManager):
    ''' custom user object manager for the user in system '''

    def create_user(self, email, name, password=None):
        ''' create user in the system '''
        if not password:
            raise ValueError('You need to provide a valid password for the user')
        
        email = self.normalize_email(email)
        user = self.model(name=name, email=email)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, name, password):
        ''' create super user in the system '''

        user = self.create_user(email,name,password)

        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser):
    ''' database model for user in system '''
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=50, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserProfileManager()

    def get_short_name(self):
        ''' return short name for the user '''
        return self.name
    
    def get_full_name(self):
        ''' return full name for the user '''
        return self.name
    
    def __str__(self):
        return self.name