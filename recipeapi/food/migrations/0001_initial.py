# Generated by Django 5.0.2 on 2024-03-04 10:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('title', models.CharField(max_length=40, primary_key=True, serialize=False, unique=True)),
                ('category', models.CharField(max_length=10)),
                ('cuisine', models.CharField(max_length=20)),
                ('meal_type', models.CharField(max_length=20)),
                ('servings', models.IntegerField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='pictures')),
                ('ingredient_list', models.TextField()),
                ('recipe_detail', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
