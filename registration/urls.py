from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    path('logout/', auth_views.logout, {'template_name': 'home.html'}, name='logout'),
]
