from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
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


def fork(request, id):
    if request.method == 'POST':
        forked_from = get_object_or_404(Recipe, id=id)
        # need to get object twice because we must modify it to clone it
        recipe = get_object_or_404(Recipe, id=id)
        recipe.pk = None
        recipe.forked_from = forked_from
        recipe.title = "Fork of " + forked_from.title
        recipe.save()
        return HttpResponseRedirect('/recipes/' + str(recipe.id))
    else:
        raise Http404


def edit(request, id):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = get_object_or_404(Recipe, id=id)
            # todo figure out how to do these 6 lines in one line
            recipe.title = form.cleaned_data['title']
            recipe.steps = form.cleaned_data['steps']
            recipe.equipment = form.cleaned_data['equipment']
            recipe.ingredients = form.cleaned_data['ingredients']
            recipe.notes = form.cleaned_data['notes']
            recipe.save()
            return HttpResponseRedirect('/recipes/' + str(id))
    else:
        recipe = get_object_or_404(Recipe, id=id)
        form = RecipeForm(instance=recipe)

    return render(request, 'recipes/edit.html', {'form': form, 'recipe_id': id})
