from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello, James')


# Create your views here.
