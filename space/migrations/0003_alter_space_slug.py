# Generated by Django 4.2.1 on 2024-01-10 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0002_space_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='space',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
