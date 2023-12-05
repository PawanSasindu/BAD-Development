from django.db import models

from django.db import models

class Doctortable(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, editable=False, unique=True)
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    description = models.TextField()
    available_days = models.CharField(max_length=100)
    available_time = models.CharField(max_length=100)
    image = models.ImageField( blank=True, null=True)

    def __str__(self):
        return self.name
# Create your models here.
