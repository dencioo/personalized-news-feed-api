# Defines the database models for the App
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model): # models.Model is the base class for all models in Django
    # Extend the users model to store the preferences
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    preferred_categories = models.ManyToManyField('Category') # Allowing multiple categories for user preference
    preferred_sources = models.JSONField(default=list) # store a list of JSON fields of preferred sourcecs directly not linked to other model

# This represent a different news categories
class Category(models.Model):
    name = models.CharField(max_length=100) # The name of news category

    def __str__(self):  # Return the name as string representation of the category
        return self.name