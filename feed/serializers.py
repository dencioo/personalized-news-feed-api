from rest_framework import serializers
from django.contrib.auth.models import User
from .models import BlogPost, UserProfile, Category

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ["id", "title", "content", "published_date"]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class UserProfileSerializer(serializers.ModelSerializer):
    preffered_categories = CategorySerializer(many=True, readonly=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'preferred_categories', 'preferred_sources']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user