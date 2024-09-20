from django.db import models

class salon_head(models.Model):
    name=models.CharField(max_length=200)
    surname=models.CharField(max_length=200)
    age=models.IntegerField()
    address=models.IntegerField()
    phone_no=models.CharField(max_length=200)
    date_of_birth=models.DateField()


# Create your models here.
class salon(models.Model):
    salon_name=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    ratings=models.IntegerField()
    description=models.CharField(max_length=200)
    reviews=models.CharField(max_length=200)
    image=models.ImageField()
    no_of_barbers=models.IntegerField()
    no_of_chairs=models.IntegerField()
    opening_time=models.IntegerField()
    closing_time=models.IntegerField()
      
   
class Service(models.Model):
    salon = models.ForeignKey(salon, on_delete=models.CASCADE, related_name='services')
    service_name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration=models.IntegerField()



