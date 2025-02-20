import pytest
from feed.models import Article, Category
from django.contrib.auth.models import User


@pytest.mark.django_db # this allows the test to interact with database
def test_create_article():  # prefixing with 'test_' and runs the function with 'test_'; to check if an "Article" can created, linked to a "User" and assigned categories
    user = User.objects.create(username="testuser") # to insert a new user to the database, but no password/email; this steps ensures we have valid user before creating article
    category = Category.objects.create(name="Technology") # to insert Category since it belong to multiple categories
    article = Article.objects.create(user=user) # creates a new article in the database, and this article belongs to the user we just created (testuser)
    article.preferred_categories.add(category) # Add() method is used because preferred_categories is a ManytoManyField

    assert article.user.username == "testuser" # check if it matches "testuser"
    assert category in article.preferred_categories.all() # returns a list of all categories; checks if the "Technology" is in that list
