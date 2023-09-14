from django.db import models

# Create your models here.
class trains(models.Model):
    id = models.AutoField(primary_key=True, default=2)
    train_name = models.CharField(max_length=50)
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    price = models.FloatField(default=120)
    seats_available = models.IntegerField()
    #schedule_type = models.CharField(max_length=10, choices=[('Daily', 'Daily'), ('Weekly', 'Weekly')])
    schedule_type = models.CharField(max_length=50)


class person(models.Model):
     
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    date_and_time_of_booking=models.DateTimeField(auto_now_add=True)
    train=models.ForeignKey('trains', on_delete=models.CASCADE)