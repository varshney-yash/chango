from django.db import models
from django.contrib.auth.models import User

class Space(models.Model):
    name = models.CharField(max_length=255)
    slug  = models.SlugField(unique=True)
    created_by = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)