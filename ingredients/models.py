from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


class Ingredients(models.Model):
    name = models.CharField(max_length=100, blank=True)
    notes = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='ingredients')

    def __str__(self):
        return self.name