from django.shortcuts import render,redirect, get_object_or_404 
from django.http import HttpResponse
from salon.models import salon


def login(request):
    return render(request,'index.html')

def barbershop_list(request):
    salon1=salon.objects.all()
    return render(request,'shop.html',{'salon':salon1})

def barbershop(request):
    return render(request,'shop-detail.html')

