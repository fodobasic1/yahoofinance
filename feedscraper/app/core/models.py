from django.db import models
from rest_framework.pagination import PageNumberPagination

class News(models.Model):
    guid = models.UUIDField(primary_key=True, unique=True)
    description = models.TextField(max_length=1000)
    link = models.URLField(max_length=200)
    title = models.CharField(max_length=200)
    publishedDate = models.DateTimeField()
    symbol = models.CharField(max_length=20)

    def __str__(self):
        return self.title
        

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50
    page_query_param = 'p'