from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    forked_from = models.ForeignKey(
      'self',
      default=None,
      on_delete=models.SET_DEFAULT,
      blank=True,
      null=True)
