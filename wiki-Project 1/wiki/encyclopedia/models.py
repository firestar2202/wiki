from django.db import models


# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=64)
    contents = models.CharField(max_length=128)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.title}"
