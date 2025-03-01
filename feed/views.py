# Contains views that define the app's behavior
from django.shortcuts import render #Django's tradtional view renderer
from rest_framework import viewsets, generics # Import DRF's viewsets and generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User # Import Django's built-in User model
from .models import UserProfile, Category # Import the models
from .serializers import UserProfileSerializer, CategorySerializer, UserSerializer  # Import the serializers for the models

# A ViewSet that provides full CRUD operation for the Models
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()  # Defines the queryset; all UserProfile instances
    serializer_class = UserProfileSerializer # Specifies the serializer to be used in converting UserProfile instances

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer # Specifies the serializer to be used in converting Category instances

# A view that allows users to create an account (User Registration )
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all() # All User instances for creation purposes
    serializer_class = UserSerializer # Specifies the serializer to used for User creations; handles password hashing
    permission_classes = [AllowAny] # This allows any user to create account