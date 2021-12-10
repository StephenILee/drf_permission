from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *

router = DefaultRouter()
router.register('user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user_fbv/<int:id>', get_user),
    path('user_fbv2/<int:id>', get_user2),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]