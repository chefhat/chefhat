from django.shortcuts import render, get_object_or_404
from .models import Recipe

# Create your views here.


def index(request):
    return render(request, 'recipes/index.html', {'recipes': Recipe.objects.all()})


def show(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    return render(request, 'recipes/show.html',
                  {'recipe': recipe, 'materials': recipe.materials.all(), 'ingredients': recipe.ingredients.all(), 'steps': recipe.steps.all()})


def new(request):
    recipe = get_object_or_404(Recipe, id=id)
    return render(request, 'recipes/show.html',
                  {'recipe': recipe, 'materials': recipe.materials.all(), 'ingredients': recipe.ingredients.all(), 'steps': recipe.steps.all()})
