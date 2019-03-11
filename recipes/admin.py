from django.contrib import admin
from .models import Material
from .models import Ingredient
from .models import Step
from .models import Recipe

admin.site.register(Material)
admin.site.register(Ingredient)
admin.site.register(Step)
admin.site.register(Recipe)
