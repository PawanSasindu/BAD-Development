from django.db import models
from django.contrib.auth.models import User

class Doctortable(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, editable=False, unique=True)
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    description = models.TextField()
    available_days = models.CharField(max_length=100)
    available_time = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    id_number = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.user.username

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    description = models.TextField()
    available_days = models.CharField(max_length=100)
    available_time = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Appointment(models.Model):
    customer_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10)
    id_number = models.CharField(max_length=20)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.customer_name}'s Appointment with {self.doctor.name} on {self.date} at {self.time}"
