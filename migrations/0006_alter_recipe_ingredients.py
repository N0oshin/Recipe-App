# Generated by Django 4.2.7 on 2025-03-28 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0005_tag_recipe_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="ingredients",
            field=models.JSONField(default=list),
        ),
    ]
