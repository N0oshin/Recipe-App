from django.urls import path, reverse_lazy
from . import views

app_name='recipes'
urlpatterns = [
    path('', views.RecipeListView.as_view(), name='all'),
    path('recipe/create', views.RecipeCreateView.as_view(success_url=reverse_lazy('recipes:all')), name='recipe_create'),
    path('recipe/<int:pk>', views.RecipeDetailView.as_view(), name = 'recipe_detail'),
    path('recipe_picture/<int:pk>', views.stream_file, name='recipe_picture'),
    path('recipe/<int:pk>/update', views.RecipeUpdateView.as_view(success_url=reverse_lazy('recipes:all')), name = 'recipe_update'),
    path('recipe/<int:pk>/delete', views.RecipeDeleteView.as_view(success_url=reverse_lazy('recipes:all')), name = 'recipe_delete'),

]

