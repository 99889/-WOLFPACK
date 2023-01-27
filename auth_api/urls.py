# imports
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from . import views

# register urls to the router
router = DefaultRouter()
router.register('profile', views.UserProfile, basename='user-api')

urlpatterns = [
    path('', include(router.urls)),
    path('auth', include(auth_api.urls)),

    
]
