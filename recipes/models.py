from django.db import models

TEASPOON = 'tsp'
TABLESPOON = 'tbsp'
CUP = 'c'
OUNCE = 'oz'
POUND = 'lb'
CLOVE = 'cl'
INGREDIENT_CAPACITY_CHOICES = [
    (TEASPOON, 'teaspoon'),
    (TABLESPOON, 'tablespoon'),
    (CUP, 'cup')
]
INGREDIENT_WEIGHT_CHOICES = [
    (OUNCE, 'ounce'),
    (POUND, 'pound')
]
INGREDIENT_SPECIAL_CHOICES = [
    (CLOVE, 'clove')
]
INGREDIENT_CHOICES = list(set().union(
    INGREDIENT_WEIGHT_CHOICES, INGREDIENT_CAPACITY_CHOICES, INGREDIENT_SPECIAL_CHOICES))


class Material(models.Model):
    name = models.CharField(max_length=32)
    quantity = models.DecimalField(decimal_places=3, max_digits=6, blank=True)


class Ingredient(models.Model):
    name = models.CharField(max_length=32)
    quantity = models.DecimalField(decimal_places=3, max_digits=6, blank=True)
    type = models.CharField(
        max_length=32, choices=INGREDIENT_CHOICES, blank=True)


class Step(models.Model):
    description = models.TextField()
    note = models.BooleanField()


class Recipe(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField(blank=True)
    forked_from = models.ForeignKey(
        'self',
        default=None,
        on_delete=models.SET_DEFAULT,
        blank=True,
        null=True)
    materials = models.ManyToManyField(Material, blank=True)
    ingredients = models.ManyToManyField(Ingredient, blank=True)
    steps = models.ManyToManyField(Step, blank=True)
