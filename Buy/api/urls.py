
from django.urls import path
from .views import Index,UserDetailAPI,LoginView

urlpatterns = [
    path('getfilerdata/',Index.as_view()),
    path('Userdata/',UserDetailAPI.as_view()),
    path('Logindata/',LoginView.as_view()),
]