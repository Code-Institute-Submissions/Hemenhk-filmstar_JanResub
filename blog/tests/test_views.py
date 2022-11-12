from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    """
    This code was inspired by The Dumbfounds. Specific link can be followed in the readme
    """
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.contact_url = reverse('contact')
        self.about_url = reverse('about')

    def test_get_post_list_page_GET(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')