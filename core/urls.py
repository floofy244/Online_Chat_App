from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage, name = 'frontpage'),
    path('signup/', views.signup, name = 'signup'),
    path('logout/', views.logout_user, name = 'logout'),
    path('login/', views.login_user, name='login'),
]