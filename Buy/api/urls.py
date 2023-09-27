
from django.urls import path
from .views import Index,UserDetailAPI,LoginView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.authtoken import views

  


urlpatterns = [
    path('getfilerdata/',Index.as_view()),
    path('Userdata/',UserDetailAPI.as_view()),
    path('Logindata/',LoginView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-token-auth/', views.obtain_auth_token)
]