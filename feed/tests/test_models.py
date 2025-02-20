import pytest
from feed.models import Article, Category
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_create_article():
    user = User.objects.create(username="testuser")
    category = Category.objects.create(name="Technology")
    article = Article.objects.create(user=user)
    article.preferred_categories.add(category)

    assert article.user.username == "testuser"
    assert category in article.preferred_categories.all()
