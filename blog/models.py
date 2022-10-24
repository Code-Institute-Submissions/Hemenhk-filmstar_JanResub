from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=400, unique=True, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_post")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    posted_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def amount_of_likes(self):
        return self.likes.count()
