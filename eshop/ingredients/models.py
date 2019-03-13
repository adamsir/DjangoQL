from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, related_name='ingredients', on_delete=models.PROTECT)

    def __str__(self):
        return self.name