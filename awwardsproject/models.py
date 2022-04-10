
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator, MinValueValidator


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length=300, default='') 
    email = models.EmailField(null=True) 
    name =models.CharField(max_length=50, blank=True)   

    
    def __str__(self):
        return f'{self.user.username} Profile'

class Post (models.Model):
    title = models.CharField(max_length=20)
    post = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    projecturl= models.URLField(max_length=200, default='')
    published_date = models.DateTimeField(auto_now_add=True)
    picture = CloudinaryField('image')
    design_rating = models.IntegerField(default=0)
    usability_rating = models.IntegerField(default=0)
    content_rating = models.IntegerField(default=0)

    class Meta:
        ordering = ['-published_date']  

    @classmethod
    def display(cls):
        posts = cls.objects.all()
        return posts

    def save_posts(self):
        self.user
    def delete_posts(self):
        self.delete()
    @classmethod
    def search_projects(cls, name):
        return cls.objects.filter(title__icontains=name).all()       

class Rating(models.Model):
    # Design, Usability, Content
    rating = models.CharField(max_length=20, default='design')
    # "score" 1-10
    scale = models.IntegerField(default=1)
    # selected post
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='ratings')
    # logged in user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # class Meta:
    #     constraints = [
    #         CheckConstraint(check=Q(rate__range=(0, 10)), name='valid_rate'),
    #         UniqueConstraint(fields=['user', 'post'], name='rating_once')
    #     ]

        