from django.test import TestCase
from datetime import datetime
import uuid

from core.models import News

# Test Class for testing model : News
_guid = uuid.uuid4()


class NewsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        News.objects.create(
            guid = _guid,
            description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
            link = 'https://9gag.com/',
            title = 'This is test title. Nothig more. Poyy',
            publishedDate = datetime.now(),
            symbol = 'AAPL'
        )
    # helper function to get news object by guid
    @classmethod
    def getObject(cls):
        return News.objects.get(guid = _guid)
    
    # check if the field label of 'description' is correct
    def test_description_label(self):
        news = self.getObject()
        field_label = news._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')
    
    # check if the field label of 'guid' is correct      
    def test_guid_label(self):
        news = self.getObject()
        field_label = news._meta.get_field('guid').verbose_name
        self.assertEqual(field_label, 'guid')
    
    # check if field 'guid' is actually a primary key
    def test_guid_pk(self):
        news = self.getObject()
        field_pk = news._meta.get_field('guid').primary_key
        self.assertTrue(field_pk)

    # check if 'link' field max_lenght is actually 200
    def test_url_max_length(self):
        news = self.getObject()
        max_length = news._meta.get_field('link').max_length
        self.assertEqual(max_length, 200)