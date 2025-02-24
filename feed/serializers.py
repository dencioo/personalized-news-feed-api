from rest_framework import serializers
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