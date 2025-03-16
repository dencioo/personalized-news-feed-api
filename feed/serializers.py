from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Category

class CategorySerializer(serializers.ModelSerializer): # Serialize for the Category model
    class Meta:
        model = Category    # Link the serializer to the Category model
        fields = ['id', 'name'] # Specify the fields to be serialized

class UserProfileSerializer(serializers.ModelSerializer):   # Serialize for the UserProfile model
    # Use the CategorySerializer for many to many relationship
    # This insert the info about each news category in the user's prefrence
    preferred_categories = CategorySerializer(many=True, read_only=True) 

    preferred_categories_ids = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.all(), # Queryset to get all the categories
        many = True, # Allow for multiple categories
        write_only = True # Field is not included in the serialized data
    )
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'preferred_categories', 'preferred_sources'] # Specified fields to be included in Serialized data

    def update(self, instance, validated_data):
        preferred_categories = validated_data.pop('preferred_categories_ids', None)
        instance.preferred_categories.set(preferred_categories) # preferred_categories is a many-to-many field
        return super().update(instance, validated_data) # Call the parent class update method
        
class UserSerializer(serializers.ModelSerializer): # Serialize for the User model
    class Meta:
        model = User # Link the serializer to Django's buit-in User model
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}, # This prevents from being exposed in API response
                        'email': {'required': True},    # This ensures that email is required
                        } 

    def create(self, validated_data):
        email = validated_data.pop('email', None) # Extract the email safely
        user = User.objects.create_user(**validated_data) # This customization ensures that the password is hashed before being stored in the database
        
        if email:
            user.email = email   # This manually set the email
            user.save() # Save email to the user
        return user                                       # this uses Django's built-in create_userg