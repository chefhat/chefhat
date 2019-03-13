from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Recipe
from .forms import RecipeForm

# Create your views here.


def index(request):
    return render(request, 'recipes/index.html', {'recipes': Recipe.objects.all()})


def show(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    return render(request, 'recipes/show.html', {'recipe': recipe})


def new(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            return HttpResponseRedirect('/recipes/' + str(recipe.id))
    else:
        form = RecipeForm()

    return render(request, 'recipes/new.html', {'form': form})
