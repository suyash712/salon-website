from django.db import models

class salon_head(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    age = models.IntegerField()
    address = models.CharField(max_length=200)  # Changed to CharField
    phone_no = models.CharField(max_length=200)
    date_of_birth = models.DateField()


class salon(models.Model):
    salon_head = models.ForeignKey(salon_head, on_delete=models.CASCADE, related_name='salon')
    salon_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    address = models.CharField(max_length=200, default="xyz")
    ratings = models.IntegerField(default=1)
    description = models.CharField(max_length=200)  # Ensure you're saving this field
    reviews = models.CharField(max_length=200)      # Ensure you're saving this field
    image = models.ImageField(upload_to='salon_images/')  # Specify upload_to for image
    no_of_barbers = models.IntegerField()
    no_of_chairs = models.IntegerField()
    opening_time = models.TimeField()   # Change to TimeField
    closing_time = models.TimeField()   # Change to TimeField


class Service1(models.Model):
    salon = models.ForeignKey(salon, on_delete=models.CASCADE, related_name='services')
    service_name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField()

class registration(models.Model):
    username =models.CharField(max_length=200)
    email = models.EmailField()
    password =models.CharField(max_length=200)