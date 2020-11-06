from django.shortcuts import render
from .models import Recipe

# Create your views here.
def index(request):
    return render(request, "recipes/index.html", {
        "recipes": Recipe.objects.all()
    })

# pagename is the title of my recipe
def page(request, pagename):
    try:
        recipe = Recipe.objects.get(title=pagename)
        return render(request, "recipes/recipe.html", {
            "recipe": recipe
        })
    except Recipe.DoesNotExist:
        return render(request, "recipes/error.html", {
            "error": pagename
        })