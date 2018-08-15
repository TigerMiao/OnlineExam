from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return HttpResponse("<html><body><h1>Hello, world. You're at mysite index.</h1></body></html>")
