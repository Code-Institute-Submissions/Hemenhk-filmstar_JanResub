from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

"""
Note that this code was used from Code Institute's "I Think Therefore I Blog"
tutorial to help create this project.
"""


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')
