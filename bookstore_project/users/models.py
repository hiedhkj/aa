from django.db import models
from django.contrib.auth.hashers import make_password

class UserAccount(models.Model): 
    username = models.CharField(max_length=50, unique=True) 
    email = models.EmailField(unique=True) 
    password = models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True) 
    is_active = models.BooleanField(default=True) 
    last_login = models.DateTimeField(null=True, blank=True) 
    is_admin = models.BooleanField(default=False) 
    is_deleted = models.BooleanField(default=False)

    @classmethod
    def create_user(cls, username, email, password):
        user = cls(
            username=username,
            email=email,
            password=make_password(password)
        )
        user.save()
        return user
