from django.contrib import admin
from salon.models import salon,Service1,salon_head,registration

# Register your models here.

class salon(admin.ModelAdmin):
    list_display=('salon_head ','salon_name','location','address','ratings','description','reviews','image','no_of_barbers','no_of_chairs','opening_time','closing_time')    
    admin.site.register(salon)

class service(admin.ModelAdmin):
    list_display=('salon','service_name','description','price','duration')
    admin.site.register(Service1)

class salon_head(admin.ModelAdmin):
    list_display=('name','surname','age','address','phone_no','date_of_birth')
    admin.site.register(salon_head)

class registration(admin.ModelAdmin):
    list_display=('username','email','password')
    admin.site.register(registration)    