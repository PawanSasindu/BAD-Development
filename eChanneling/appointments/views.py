from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'Home.html')
def other_services(request):
    return render(request, 'Other Service.html')
