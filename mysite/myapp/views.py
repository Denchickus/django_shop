from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def index(request):
    items = Product.objects.all()
    data = {
        'items': items
    }
    return render(request, "myapp/index.html", data)

def indexItem(request, id):
    item = Product.objects.get(id=id)
    context = {
        'item': item
    }
    return render(request, "myapp/detail.html", context=context)



