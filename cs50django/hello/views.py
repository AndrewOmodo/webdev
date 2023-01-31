from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello, World!') #result from a HTTP request

def andrew(request):
    return HttpResponse('Hello, Andrew!')

def parvin(request):
    return HttpResponse('Hello, Parvin!')