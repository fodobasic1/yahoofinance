from django.db import models
from django.db.models import fields
from rest_framework import serializers

from .models import News

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = (
            'guid',
            'description',
            'link',
            'title',
            'publishedDate',
            'symbol'
        )

    def __str__(self):
            return self.title
