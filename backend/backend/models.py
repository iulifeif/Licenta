from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            username = self.username,
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Crates and saves a staff user with the given email and password
        """
        user = self.create_user(
            email,
            password = password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password
        """
        user = self.create_user(
            email,
            password = password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address',
            max_length=255, unique=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

objects = UserManager()

USERNAME_FIELD = 'email'
REQUIRED_FIELDS = ['username']

def get_full_name(self):
    return self.username

def get_email(self):
    return self.email

def __str__(self):
    return self.email

def has_perm(self, perm, obj=None):
    return True

@property
def is_staff(self):
    "Is the user a member of staff?"
    return self.staff

@property 
def is_admin(self):
    "Is the user a admin member?"
    return self.admin