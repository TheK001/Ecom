from django.urls import path
from .views import UserListView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from .views import RegisterView, LoginView
urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('register/', RegisterView.as_view(), name='register-api'),
    path('login/', LoginView.as_view(), name='login-api'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
