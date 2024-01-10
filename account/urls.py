from django.contrib.auth.views import LogoutView,LoginView
from django.urls import path
from .views import signup

urlpatterns = [
    path('signup/',signup,name='signup'),
    path('login/',LoginView.as_view(template_name='account/login.html'),name='login'), 
    path('logout/',LogoutView.as_view(),name='logout')
]
