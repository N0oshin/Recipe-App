# Generated by Django 4.2.7 on 2025-03-18 08:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("recipes", "0002_recipe_content_type"),
    ]

    operations = [
        migrations.CreateModel(
            name="Fav",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "recipe",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="recipes.recipe"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="recipes_favs",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("recipe", "user")},
            },
        ),
        migrations.AddField(
            model_name="recipe",
            name="favorites",
            field=models.ManyToManyField(
                related_name="favorite_recipes",
                through="recipes.Fav",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
