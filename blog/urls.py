from django.urls import path, include
from . import views

"""
Note that some code was used from Code Institute's 'I think therefore I blog'
tutorial to help create this project.
"""

urlpatterns = [
    path('', views.PostList.as_view(), name="home"),
    path('<slug:slug>/', views.PostDetail.as_view(), name="post_detail"),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('add', views.add_post, name='add_post'),
    path('<slug:slug>/edit/', views.post_edit, name="post_edit"),
    path('<slug:slug>/delete/', views.delete_post, name="post_delete"),

]
