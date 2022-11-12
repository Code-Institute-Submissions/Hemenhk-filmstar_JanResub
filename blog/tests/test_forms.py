from django.test import TestCase
from blog.forms import CommentForm


class TestForms(TestCase):

    def test_comment_bodyfield_is_required(self):
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')