from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenVerifyView, 
    TokenRefreshView, 
    TokenObtainPairView)
from .views import UserCreate, UserProfileViewSet, CategoryViewSet

router = DefaultRouter()

# Register the viewsets with router
router.register(r'userprofile', UserProfileViewSet) # This creates endpoints at /userprofile/
router.register(r'categories', CategoryViewSet) # This creates endpoints at /categories/

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserCreate.as_view(), name='user-create'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]