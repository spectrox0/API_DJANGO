from django.urls import path
from .views import get_works,get_categories,get_images

urlpatterns = [
    path("works/", get_works, name="get-works"),
    path("categories/", get_categories, name="get-categories"),
    path("image/",get_images, name="get-images")
]
