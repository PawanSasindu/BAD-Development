from django.shortcuts import render
from.models import Doctortable
#for signup page
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib import messages

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import UserProfile


from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AppointmentForm 
from .models import Doctor

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

        # Check if a user with the given id_number exists in UserProfile
        try:
            user_profile = UserProfile.objects.get(id_number=id_number)
        except UserProfile.DoesNotExist:
            user_profile = None

        if user_profile is not None:
            # If the user is valid, log in the user and redirect to the appointment page
            login(request, user_profile.user)
            return redirect('appointment')
        else:
            # If the user is not valid, display an error message
            messages.error(request, 'User not found. Please sign up.')
            return redirect('signin')

    return render(request, 'signin.html')


# appoinment creating
def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            customer_name = form.cleaned_data['customer_name']
            phone_number = form.cleaned_data['phone_number']
            id_number = form.cleaned_data['id_number']
            doctor = form.cleaned_data['doctor']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']

            # Create an Appointment instance and save it
            appointment = Appointment(
                customer_name=customer_name,
                phone_number=phone_number,
                id_number=id_number,
                doctor=doctor,
                date=date,
                time=time
            )
            appointment.save()

            # Generate and display the report in the browser
            report_content = appointment.generate_report()
            response = HttpResponse(report_content, content_type='text/plain')
            response['Content-Disposition'] = 'inline; filename=appointment_report.txt'
            return response  # This is the correct return statement

    # If it's a GET request or form is not valid, create a form and render the template
    form = AppointmentForm()
    doctors = Doctor.objects.all()
    return render(request, 'appointment.html', {'form': form, 'doctors': doctors})
