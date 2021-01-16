from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello ようこそ")

# Create your views here.
