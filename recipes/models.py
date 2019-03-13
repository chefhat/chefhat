from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=80)
    steps = models.TextField()
    equipment = models.TextField(blank=True)
    ingredients = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    forked_from = models.ForeignKey(
            'self',
            default=None,
            on_delete=models.SET_DEFAULT,
            blank=True,
            null=True)
