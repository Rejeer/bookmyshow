from django.db import models
from django.contrib.auth.models import User

class Show(models.Model):
    gen_choice = (
        ('Action', 'Action'),
        ('Sports', 'Sports'),
        ('Drama', 'Drama'),
        ('Fantasy', 'Fantasy'),
        ('Horror', 'Horror'),
        ('Comedy', 'Comedy'),
        ('Si-Fi', 'Si-Fi'),
        ('Thriller', 'Thriller'),
        ('Biopic', 'Biopic'),
    )
   
    movies = models.CharField(max_length=30, null=True)
    director = models.CharField(max_length=30, null=True)
    actor = models.CharField(max_length=30, null=True)
    genres = models.CharField(max_length=30, choices=gen_choice, default='Action')
    created_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)  


 
class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=25, blank=True)
    image = models.ImageField(upload_to='image/',null=True,blank=True)
    


