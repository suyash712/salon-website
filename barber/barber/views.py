from django.shortcuts import render,redirect, get_object_or_404 
from django.http import HttpResponse
from salon.models import salon,Service1,salon_head


def home(request):
    return render(request,'index.html')

def barbershop_list(request):
    salon1=salon.objects.all()
    return render(request,'shop.html',{'salon':salon1})

def barbershop(request):
    return render(request,'shop-detail.html')

def salon_detail(request, pk):
    salon1 = get_object_or_404(salon, pk=pk)
    services = Service1.objects.filter(salon=salon1)  # Use this instead
    return render(request, 'shop-detail.html', {'salon': salon1, 'services': services})



def dashboard(request):
    

    return render(request, 'salon_dashboard.html')

def login(request):
    return render(request,'login.html')

def salon_registration(request):
    return render(request,'salon_registration.html')

def register_salon(request):
    if request.method == 'POST':
        # Step 1: Save Personal Information
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        age = request.POST.get('age')
        address = request.POST.get('address')
        phone_no = request.POST.get('phone_no')
        date_of_birth = request.POST.get('date_of_birth')

        personal_info = salon_head.objects.create(
            name=name,
            surname=surname,
            age=age,
            address=address,
            phone_no=phone_no,
            date_of_birth=date_of_birth
        )

        # Step 2: Save Salon Information
        salon_name = request.POST.get('salonName')
        location = request.POST.get('location')
        salon_address = request.POST.get('address')  # Changed variable to avoid conflict
        no_of_barbers = request.POST.get('no_of_barbers')
        image = request.FILES.get('image')  # Use request.FILES for file upload
        no_of_chairs = request.POST.get('no_of_chairs')
        opening_time = request.POST.get('opening_time')
        closing_time = request.POST.get('closing_time')
        description = request.POST.get('description')  # Ensure to get description

        salon_info = salon.objects.create(
            salon_head=personal_info,  # Associate salon info with personal info
            salon_name=salon_name,
            location=location,
            address=salon_address,
            image=image,
            no_of_barbers=no_of_barbers,
            no_of_chairs=no_of_chairs,
            opening_time=opening_time,
            closing_time=closing_time,
            description=description  # Save description here
        )

        # Step 3: Save Services (handling multiple services dynamically)
        services = zip(
            request.POST.getlist('serviceName[]'),
            request.POST.getlist('serviceDescription[]'),
            request.POST.getlist('servicePrice[]'),
            request.POST.getlist('serviceDuration[]')
        )

        for service_name, service_description, service_price, service_duration in services:
            Service1.objects.create(
                salon=salon_info,
                service_name=service_name,
                description=service_description,  # Ensure correct field name
                price=service_price,
                duration=service_duration
            )

        return redirect(home)  # Redirect to success page or display success message

    return render(request, 'salon_register.html')
