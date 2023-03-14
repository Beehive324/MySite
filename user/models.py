#django imports
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Manager(BaseUserManager): # User Management class 
    def c_user(self, email, username, password=None):
        if not email:
            raise ValueError("Please enter an Email address")
        if not username:
            raise ValueError("Please enter a valid username")
        
        user = self.model(
            email=self.normalize_email(email), #converts emails to lower case
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password): # function to create a superuser
        user = self.c_user(
               email=self.normalize_email(email),
               username=username,
               password=password,
        )   
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user


class User(AbstractBaseUser): # This is the class for creating an account for a specific user
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = Manager()

    def __str__(self):
        return self.email + "," + self.username #fields required to input
    
    def has_perm(self, perm, obj=None):
        return self.is_admin # A user can only have permission if they are the admin
    
    def has_module_perms(self, app_Label):
        return True