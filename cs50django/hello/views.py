from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse('Hello, World!') #result from a HTTP request
    return render(request, "hello/index.html")

def andrew(request):
    return HttpResponse('Hello, Andrew!')

def parvin(request):
    return HttpResponse('Hello, Parvin!')

def greet(request, name):
    return HttpResponse(f'Hello, {name.capitalize()}!')