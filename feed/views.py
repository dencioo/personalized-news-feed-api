# Contains views that define the app's behavior
from django.shortcuts import render #Django's tradtional view renderer
from rest_framework import viewsets
from .models import BlogPost, UserProfile, Category
from .serializers import BlogPostSerializer, UserProfileSerializer, CategorySerializer

# Create your views here.

class BlogPostListCreate(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer 

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer