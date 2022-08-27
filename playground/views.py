from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def say_hello(request):
    return HttpResponse("Hello World")


def hello_page(request):
    return render(request, 'helloPage.html', {'name': 'Django'})
