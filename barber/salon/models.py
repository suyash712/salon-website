from django.db import models

# Create your models here.
class salon(models.Model):
    salon_name=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    ratings=models.IntegerField()
    description=models.CharField(max_length=200)
    reviews=models.CharField(max_length=200)
    image=models.ImageField()




