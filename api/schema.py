import graphene
from graphene_django import DjangoObjectType

from .models import Category,Image,Work

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class WorkType(DjangoObjectType):
    class Meta:
        model = Work

class ImageType(DjangoObjectType):
    class Meta:
        model = Image
       
class Query(graphene.ObjectType):
    works = graphene.List(WorkType)
   

    def resolve_works(root, info):
        return Work.objects.all()

    #def resolve_category_by_name(root, info, name):
    #    try:
    #       return Category.objects.get(name=name)
     #   except Category.DoesNotExist:
     #       return None

schema = graphene.Schema(query=Query)