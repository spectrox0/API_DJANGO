from django.contrib import admin
from .models import Work, Category, Image, Skill, Translate

# Register your models here.
admin.site.register((Work, Category, Image, Skill, Translate))
