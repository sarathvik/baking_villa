from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('register/register2/',views.register,name='register2'),
    path('login/login2/',views.login,name='login2'),
    path('Logout',views.Logout,name='Logout')
]