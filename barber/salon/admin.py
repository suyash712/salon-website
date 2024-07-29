from django.contrib import admin
from salon.models import salon
# Register your models here.

class salon(admin.ModelAdmin):
    list_display=('salon_name','location','ratings','description','reviews','image')    
    admin.site.register(salon)



