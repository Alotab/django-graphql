from django.contrib import admin

# Register your models here.
from .models import Category
from .models import Ingredients

admin.site.register(Category)
admin.site.register(Ingredients)


