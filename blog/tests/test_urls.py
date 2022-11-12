from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import PostList, PostLike, PostDetail

"""
This code was inspired by The Dumbfounds. Specific link can be found in the readme.
"""


class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, PostList)