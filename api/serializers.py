from rest_framework import serializers
from .models import Work, Category, Image


class WorkSerializer(serializers.ModelSerializer):
    categories = serializers.StringRelatedField(many=True)
    images = serializers.StringRelatedField(many=True)
    class Meta:
        model = Work
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
