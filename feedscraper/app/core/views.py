from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics

from core.models import News
from core.serializers import NewsSerializer

class NewsList(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class NewsDetail(generics.RetrieveAPIView):
    lookup_field = 'guid'
    queryset = News.objects.all()
    serializer_class = NewsSerializer
