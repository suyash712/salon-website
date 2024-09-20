from django.shortcuts import render,redirect, get_object_or_404 
from django.http import HttpResponse
from salon.models import salon,Service


def home(request):
    return render(request,'index.html')

def barbershop_list(request):
    salon1=salon.objects.all()
    return render(request,'shop.html',{'salon':salon1})

def barbershop(request):
    return render(request,'shop-detail.html')

def salon_detail(request, pk):
    salon1 = get_object_or_404(salon, pk=pk)
    services = Service.objects.filter(salon=salon1)  # Use this instead
    return render(request, 'shop-detail.html', {'salon': salon1, 'services': services})



def dashboard(request):
    

    return render(request, 'salon_dashboard.html')

def login(request):
    return render(request,'login.html')

def salon_registration(request):
    return render(request,'salon_registration.html')