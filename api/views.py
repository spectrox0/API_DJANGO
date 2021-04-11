from django.http import HttpResponse
from rest_framework.response import Response
from django.middleware.csrf import get_token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Work, Category, Image
from .serializers import WorkSerializer, CategorySerializer, ImageSerializer


# Create your views here.


@api_view(["GET"])
def get_works(request):
    if request.method == "GET":
        works = Work.objects.all()
        serializer = WorkSerializer(works, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def get_work(request, pk):
    try:
        work = Work.objects.get(pk=pk)
    except Work.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == "GET":
        serializer = WorkSerializer(work)
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
