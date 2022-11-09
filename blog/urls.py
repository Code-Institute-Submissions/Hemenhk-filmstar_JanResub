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
]
