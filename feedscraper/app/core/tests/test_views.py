from django.conf.urls import url
from django.test import TestCase
from django.urls import reverse
import uuid
from datetime import date, datetime

from core.models import News


class NewsListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_news = 13

        for news in range(number_of_news):
            News.objects.create(
                guid = uuid.uuid4(),
                description = 'Desc %d' %(news),
                link = 'Link %d' %(news),
                title = 'Title %d' %(news),
                publishedDate = datetime.now(),
                symbol = 'TWTR'
            )
    
    # check if view is accessable by correct url
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/news')
        self.assertEqual(response.status_code, 200)

    def test_view_url_exists_at_desired_location_fail(self):
        response = self.client.get('/newzzz')
        self.assertEqual(response.status_code, 404)

    # check if view is accessable by correct name
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('news'))
        self.assertEqual(response.status_code, 200)
    
    # check if pagination is working
    def test_pagination(self):
        response = self.client.get(reverse('news'), {'page':1})
        self.assertEqual(response.status_code, 200)
         
    # check if first page has 10 results
    def test_if_first_page_has_ten(self):
        response = self.client.get(reverse('news'), {'page':1})
        self.assertEqual(len(response.data['results']), 10)
    
    # check if second page has remaining 3 pages
    def test_if_second_page_has_three(self):
        response = self.client.get(reverse('news'), {'page':2})
        self.assertEqual(len(response.data['results']), 3)
    
    def test_next_previous(self):
        response = self.client.get(reverse('news'), {'page':2})
        self.assertEqual(len(response.data['results']), 3)
        self.assertTrue(response.data['previous'], 'http://testserver/news')
        self.assertTrue(response.data['count'], 13)
