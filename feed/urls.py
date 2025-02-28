from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserCreate

router = DefaultRouter()
urlpatterns = [
    path('', include(router.urls)),
    path("register/", UserCreate.as_view(),name="user-create"),
]