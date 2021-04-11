from django.urls import path
from .views import get_works,get_categories,get_images, get_work

urlpatterns = [
    path("work/", get_works, name="get-works"),
    path("work/<pk>", get_work, name="get-work"),
    path("category/", get_categories, name="get-categories"),
    path("image/",get_images, name="get-images"),
]
