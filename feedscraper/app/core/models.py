from django.db import models
from rest_framework.pagination import PageNumberPagination

# Create your models here.

class News(models.Model):
    description=models.TextField()
    link=models.CharField(max_length=255)
    title=models.CharField(max_length=200)
    guid=models.UUIDField()
    publishedDate=models.DateTimeField()
    symbol=models.CharField(max_length=20)

    def __str__(self):
        return self.title

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50
    page_query_param = 'p'