# Defines the database models for the App
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Article(models.Model):
    # Extend the users model to store the preferences
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    preferred_categories = models.ManyToManyField('Category')
    preferred_sources = models.JSONField(default=list)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name