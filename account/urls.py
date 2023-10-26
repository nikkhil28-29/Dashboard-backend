from django.urls import path
from account.views import MyUserRegistrationView,LoginView

urlpatterns = [
    path('register',MyUserRegistrationView.as_view(),name='register'),
    path('login',LoginView.as_view(),name='login'),
]
