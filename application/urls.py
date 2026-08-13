from django.contrib import admin
from django.urls import path
from .views import account, email_sent, forgot_password, logout, register, login, index, reset_password, two_factor_auth

urlpatterns = [

    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),

    path('forgot-password/', forgot_password, name='forgot-password'),
    path('email-sent/', email_sent, name='email-sent'),
    path('two-factor-authentication/', two_factor_auth, name='two-factor-authentication'),
    path('reset-password/', reset_password, name='reset-password'),

    path('', index, name='index'),
    path('account/', account, name='account'),
]
