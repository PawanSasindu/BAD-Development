from django.shortcuts import render
from.models import Doctortable

# Create your views here.
def home(request):
    return render(request, 'Home.html')
def other_services(request):
    return render(request, 'Other Service.html')

def doctor(request):
    database = Doctortable.objects.all()
    return render(request, 'Doctor.html',{"database":database})
