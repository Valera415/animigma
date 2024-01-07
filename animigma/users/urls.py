from django.urls import path

from .views import *

urlpatterns = [
    path('registration/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('activate/<uidb64>/<token>', activate, name='activate'),
    path('profile/', user_profile, name='profile'),
]
