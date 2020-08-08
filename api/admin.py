from django.contrib import admin
from .models import Work, Category, Image

# Register your models here.
admin.site.register((Work, Category, Image))
