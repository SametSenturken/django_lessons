from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

# http://127.0.0.1:8000

def index(request):
    return HttpResponse("Merhaba")

def details(request):
    return HttpResponse("details")

def list(request):
    return HttpResponse("list")

def getProductsByCategory(request, category):
    category_text = None
    if category == "bilgisayar":
        category_text = "Lenovo, HP, Apple"
    elif category == "telefon":
        category_text = "samsung, xaomi, huawei"
    else:
        category_text = "Yanlış kategori seçimi"
    
    return HttpResponse(category_text)


