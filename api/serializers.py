from rest_framework import serializers
from .models import Work, Category, Image, Skill


class WorkSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=False)
    skills = serializers.StringRelatedField(many=True)
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


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'
