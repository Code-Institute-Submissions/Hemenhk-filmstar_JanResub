from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import PostList, PostLike, PostDetail, contact, about

"""
This code was inspired by The Dumbfounds.
Specific link can be found in the readme.
"""


class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, PostList)

    def test_post_detail_url_is_resolved(self):
        url = reverse('post_detail', args=['test-slug'])
        self.assertEquals(resolve(url).func.view_class, PostDetail)

    def test_post_like_url_is_resolved(self):
        url = reverse('post_like', args=['test-slug'])
        self.assertEquals(resolve(url).func.view_class, PostLike)

    def test_contact_url_is_resolved(self):
        url = reverse('contact')
        self.assertEquals(resolve(url).func, contact)

    def test_about_url_is_resolved(self):
        url = reverse('about')
        self.assertEquals(resolve(url).func, about)
