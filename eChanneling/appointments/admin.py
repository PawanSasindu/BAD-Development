from django.contrib import admin
from .models import Doctortable
#for signup page
from .models import UserProfile
# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'available_days', 'available_time', 'image')

admin.site.register(Doctortable, DoctorAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ( 'full_name', 'phone_number', 'id_number') #delete user from the list

admin.site.register(UserProfile, UserProfileAdmin)