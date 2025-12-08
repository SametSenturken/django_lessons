from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

# http://127.0.0.1:8000

def index(request):
    return HttpResponse("Merhaba")

