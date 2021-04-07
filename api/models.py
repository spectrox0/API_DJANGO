from django.db import models
from cloudinary.models import CloudinaryField


class Translate(models.Model):
    es = models.CharField(max_length = 255)
    en = models.CharField(max_length = 255)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Work(models.Model):
    name = models.CharField(max_length=100)
    description = models.OneToOneField(Translate, on_delete=models.CASCADE, null = True , blank= True)
    link = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    skills = models.ManyToManyField(Skill, blank=True)
    image = CloudinaryField('image', null=True, blank=True)
    category = models.OneToOneField(Category, on_delete=models.CASCADE, null=True , blank=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = CloudinaryField('image', null=True, blank=True)
    work = models.ForeignKey(Work, related_name="images", null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.image.public_id

