from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'user_accounts'

urlpatterns = [
    path('register/', views.registerview, name='register'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),
]