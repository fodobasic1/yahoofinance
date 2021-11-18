from rest_framework import generics

from core.models import News
from core.serializers import NewsSerializer

# Retrieving all News (.../news)
class NewsList(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

# Retrieving specific object based on its GUID (...news/<GUID>) since the GUID is the primary key
class NewsDetail(generics.RetrieveAPIView):
    lookup_field = 'guid'
    queryset = News.objects.all()
    serializer_class = NewsSerializer
