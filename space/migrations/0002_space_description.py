# Generated by Django 4.2.1 on 2024-01-10 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='space',
            name='description',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
