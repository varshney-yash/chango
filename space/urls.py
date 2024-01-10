from django.urls import path
from .views import spaces

urlpatterns = [
    path('',spaces,name='spaces')
]
