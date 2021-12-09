'''Urls for shop pages'''
from django.urls import path
from applications import views

urlpatterns = [
    path('', views.ApplicationListView.as_view(), name='token_refresh'),
    path('<int:pk>', views.ApplicationDetailsView.as_view()),
]
