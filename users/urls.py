from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

from users import views

router = DefaultRouter()
router.register('', views.UsersView, 'users')

urlpatterns = [
    path('refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegistrationAPIView.as_view(), name='register'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('password-recovery/', views.RequestPasswordResetEmail.as_view(), name="request-reset-email"),
    path('profile/password/', views.PasswordView.as_view(), name='update-pass'),
    path('', include(router.urls)),
]