from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Space(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True,blank=True)
    description = models.CharField(max_length=1000, blank=True)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        if not self.description:
            self.description = f"{self.created_by.username}'s Space"
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name