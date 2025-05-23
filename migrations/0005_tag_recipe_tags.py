# Generated by Django 4.2.7 on 2025-03-20 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0004_alter_fav_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                ("tag", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name="recipe",
            name="tags",
            field=models.ManyToManyField(
                blank=True, related_name="recipes_tag", to="recipes.tag"
            ),
        ),
    ]
