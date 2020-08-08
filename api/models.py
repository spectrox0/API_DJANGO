from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Work(models.Model):
    title = models.CharField(max_length=100)
    height = models.IntegerField()
    content = models.CharField(max_length=255)
    link = models.CharField(max_length=100, null=True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, blank=True)
   
    def __str__(self):
        return self.title


class Image(models.Model):
    url = models.CharField(max_length=255)
    work = models.ForeignKey(Work, related_name="images", null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.url

