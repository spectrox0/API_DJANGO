from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import WorkSerializer, CategorySerializer ,ImageSerializer
from .models import Work, Category, Image
from django.http import JsonResponse
from django.middleware.csrf import get_token
# Create your views here.


@api_view(["GET"])
def get_works(request):
    works = Work.objects.all()
    serializer = WorkSerializer(works, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_images(request):
    images = Image.objects.all().select_related()
    
    serializer = ImageSerializer(images, many=True)
    print(serializer.data)
    return Response(serializer.data)
    


# todolist/views.py
def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})

def ping(request):
    return JsonResponse({'result': 'OK'})