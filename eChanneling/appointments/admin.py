from django.contrib import admin
from .models import Doctortable
# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'available_days', 'available_time', 'image')

admin.site.register(Doctortable, DoctorAdmin)