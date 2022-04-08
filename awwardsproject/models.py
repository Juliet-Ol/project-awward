import email
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length=300, default='') 
    email = models.EmailField(null=True) 
    name =models.CharField(max_length=50, blank=True)   

    
    def __str__(self):
        return f'{self.user.username} Profile'