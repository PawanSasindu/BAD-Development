from django.shortcuts import render
from.models import Doctortable
#for signup page
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib import messages

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'Home.html')
def other_services(request):
    return render(request, 'Other Service.html')

def doctor(request):
    database = Doctortable.objects.all()
    return render(request, 'Doctor.html',{"database":database})

#for signup page
def signup(request):
    if request.method == 'POST':
        full_name = request.POST['fullName']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirmPassword']
        phone_number = request.POST.get('phoneNumber', '')
        id_number = request.POST.get('idNumber', '')

        if password != confirm_password:
            messages.error(request, 'Password and Confirm Password do not match.')
            return redirect('signup')

        try:
            # Check if a user with the given email already exists
            user = User.objects.get(email=email)
            messages.error(request, 'User with this email already exists. Please choose a different email.')
            return redirect('signup')
        except User.DoesNotExist:
            # User does not exist, proceed with creating a new user
            user = User.objects.create_user(username=email, email=email, password=password)
            user_profile = UserProfile(user=user, full_name=full_name, phone_number=phone_number, id_number=id_number)
            user_profile.save()

            messages.success(request, 'New Registration. ')
            return redirect('home')
        except IntegrityError:
            # Handle other integrity errors if necessary
            messages.error(request, 'An error occurred during registration.')
            return redirect('signup')

    return render(request, 'signup.html')



def signin(request):
    if request.method == 'POST':
        id_number = request.POST['idNumber']
        password = request.POST['password']

        # Authenticate the user using the ID number and password
        user = authenticate(request, id_number=id_number, password=password)

        if user is not None:
            # If the user is valid, log in the user and redirect to the appointment page
            login(request, user)
            return redirect('appointment')
        else:
            # If the user is not valid, display an error message
            messages.error(request, 'User not found. Please sign up.')
            return redirect('signin')

    return render(request, 'signin.html')



