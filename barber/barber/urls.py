"""
URL configuration for barber project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login',views.login),
    path('',views.home),
    path('barbershoplist',views.barbershop_list),
    path('shopdetails',views.barbershop),
    path('salon/<int:pk>/', views.salon_detail, name='salon_detail'),
    path('dashboard',views.dashboard),
    path('salon_registration',views.salon_registration),
    path('register_salon',views.register_salon,name='register_salon'),
    path('login1',views.login1,name='login1'),
    path('register',views.register,name='register')

    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)