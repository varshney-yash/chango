from django.urls import path
from .views import spaces, space

urlpatterns = [
    path('',spaces,name='spaces'),
    path('<slug:slug>/',space, name='space')
]
