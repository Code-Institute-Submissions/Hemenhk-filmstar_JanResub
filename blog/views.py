from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect, HttpResponse


#def base(request):
#    return render(request, 'base.html')


def home(request):
    return render(request, "index.html")


def contact(request):
    return render(request, "contact.html")