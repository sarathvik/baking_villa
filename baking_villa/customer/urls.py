from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('register/register2/',views.register2,name='register2'),
    path('login/login2/',views.login2,name='login2')
]