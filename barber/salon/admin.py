from django.contrib import admin
from salon.models import salon,Service,salon_head
# Register your models here.

class salon(admin.ModelAdmin):
    list_display=('salon_name','location','ratings','description','reviews','image')    
    admin.site.register(salon)

class service(admin.ModelAdmin):
    list_display=('salon','service_name','description','price','duration')
    admin.site.register(Service)

class salon_head(admin.ModelAdmin):
    list_display=('name','surname','age','address','phone_no','date_of_birth')
    admin.site.register(salon_head)