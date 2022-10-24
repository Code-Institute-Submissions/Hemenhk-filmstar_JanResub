from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic, View
from .models import Post


class Postpagination(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


def home(request):
    return render(request, "index.html")


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")