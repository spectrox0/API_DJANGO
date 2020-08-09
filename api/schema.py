from graphene_django import DjangoObjectType
import graphene

from .models import Work ,Category ,Image 

class WorkType(DjangoObjectType):
    class Meta:
        model = Work

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class ImageType(DjangoObjectType):
    class Meta:
        model = Image

class Query(graphene.ObjectType):
    works = graphene.List(WorkType)
    
    def resolve_works(self, info):
        return Work.objects.all()

schema = graphene.Schema(query=Query)