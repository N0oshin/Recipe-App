from django.db import models
from django.conf import settings

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(
            max_length=200)
    ingredients = models.CharField(
            max_length=800)
    method = models.TextField()
    owner = models.ForeignKey(
            settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
            related_name='recipe_owner')
    created_at = models.DateTimeField(
            auto_now_add=True)
    updated_at = models.DateTimeField(
            auto_now=True)
    content_type = models.CharField(
            max_length=256, null=True, blank=True,
            help_text='The MIMEType of the file')
    picture = models.BinaryField(
            null=True, blank=True, editable=True)
    favorites = models.ManyToManyField(
                settings.AUTH_USER_MODEL, through='Fav',
                related_name='favorite_recipes')

    def __str__(self):
        return self.title

class Fav(models.Model) :
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favs_user')

    class Meta:
        unique_together = ('recipe', 'user')

    def __str__(self) :
        return '%s likes %s'%(self.user.username, self.recipe.title[:10])