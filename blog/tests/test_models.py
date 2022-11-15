from django.test import TestCase
from blog.models import Post, Comment
from django.contrib.auth.models import User


class TestModel(TestCase):

    def test_post_created_by_user_draft(self):
        user = User.objects.create(username='test-username')
        review = Post.objects.create(
            title='review1',
            author=user
        )

        self.assertFalse(review.status)

    def test_comments_set_to_false_by_default(self):
        user = User.objects.create(username='test-username')
        review = Post.objects.create(
            title='review1',
            author=user
        )

        comment = Comment.objects.create(
            post=review,
            body='review comment',
        )

        self.assertFalse(comment.approved)
