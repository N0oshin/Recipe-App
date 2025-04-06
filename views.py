from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from recipes.owner import OwnerCreateView, OwnerListView, OwnerDetailView, OwnerDeleteView, OwnerUpdateView
from recipes.models import Recipe
from recipes.forms import CreateForm
from taggit.models import Tag, TaggedItem
from django.contrib.contenttypes.models import ContentType



class RecipeCreateView(OwnerCreateView):
    model = Recipe
    fields = ['title', 'ingredients', 'method', 'picture']

    success_url = reverse_lazy('recipes:all')

    def get(self, request, pk=None):
        form = CreateForm()
        ctx = {'form': form}
        return render(request, 'recipes/recipe_form.html', ctx)

    def post(self, request, pk=None):
        form = CreateForm(request.POST, request.FILES or None)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, 'recipes/recipe_form.html' , ctx)

        # Add owner to the model before saving

        recipe = form.save(commit=False)
        recipe.owner = self.request.user
        recipe.save()
        form.save_m2m()


        return redirect(self.success_url)



class RecipeListView(OwnerListView):
    template_name = "recipes/recipe_list.html"

    def get(self, request):
        query = request.GET.get('q', '')
        tag_slug = request.GET.get('tag', '')  # We'll pass tag as a GET parameter

        rec_list = Recipe.objects.all()

        if query:
            rec_list = rec_list.filter(title__icontains=query)

        tag = None
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            rec_list = rec_list.filter(tags__slug=tag_slug)

        rec_list = rec_list.order_by('-updated_at')[:10]

        recipe_type = ContentType.objects.get_for_model(Recipe)
        tags = Tag.objects.filter(
            taggit_taggeditem_items__content_type=recipe_type
        ).distinct()


        context = {
            'rec_list': rec_list,
            'query': query,
            'tag': tag,
            'tags': tags,
        }

        return render(request, self.template_name, context)




class RecipeDetailView(OwnerDetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    def get(self,request, pk):
        x = get_object_or_404(Recipe, id=pk)
        context = { 'recipe' : x }
        return render(request, self.template_name, context)


def stream_file(request, pk):
    recipe = get_object_or_404(Recipe, id=pk)
    response = HttpResponse()
    response['Content-Type'] = recipe.content_type
    response['Content-Length'] = len(recipe.picture)
    response.write(recipe.picture)
    return response


class RecipeDeleteView(OwnerDeleteView):
    model = Recipe

class RecipeUpdateView(OwnerUpdateView):
    model = Recipe
    fields = ['title', 'ingredients', 'method', 'picture']

    template_name = 'recipes/recipe_form.html'
    success_url = reverse_lazy('recipes:all')

    def get(self, request, pk):
        recipe = get_object_or_404(Recipe, id=pk, owner=self.request.user)
        form = CreateForm(instance=recipe)
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        recipe = get_object_or_404(Recipe, id=pk, owner=self.request.user)
        form = CreateForm(request.POST, request.FILES or None, instance=recipe)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        recipe = form.save(commit=False)
        recipe.save()
        form.save_m2m()



        return redirect(self.success_url)






