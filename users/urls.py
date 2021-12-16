'''Urls for User's pages'''
from django.urls import path
from .views import UserDetailsView, \
    UserSignupView, UserSigninAPIView, \
    UserLogoutAPIView, UserDeleteAPIView

urlpatterns = [
    path('<int:pk>', UserDetailsView.as_view(), name='user-details'),
    path('user_register/', UserSignupView.as_view(), name='user-register'),
    path('user_login/', UserSigninAPIView.as_view(), name='user-login'),
    path('user_logout/', UserLogoutAPIView.as_view(), name='user-logout'),
]
