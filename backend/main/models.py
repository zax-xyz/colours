from json import dumps

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    id = models.IntegerField(default=0, primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    display_name = models.CharField(max_length=50)
    access_token = models.CharField(max_length=50)
    refresh_token = models.CharField(max_length=50)
    profile_picture = models.TextField(default='')
    colours = models.TextField(default=dumps([
            'Red', 'Firebrick', 'Chocolate', 'OrangeRed', 'Coral',
            'GoldenRod', 'YellowGreen', 'SeaGreen', 'Green', 'SpringGreen',
            'DodgerBlue', 'Blue', 'BlueViolet', 'HotPink'
        ]))

    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
    def natural_key(self):
        return self.display_name

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['id', 'username' 'display_name',
                       'access_token', 'refresh_token']
    
    
    
class CeleryTask(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                primary_key=True)
    id = models.CharField(max_length=36)


class Channel(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    username = models.CharField(max_length=50)
    display_name = models.CharField(max_length=50)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.username
    
    def natural_key(self):
        return self.display_name
    
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()