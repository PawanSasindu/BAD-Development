from django.urls import path
from . import views 
# for signup page
from .views import signup
from .views import signin

urlpatterns = [
    path('', views.home, name='home'),
    path('otherservice/', views.other_services, name='other_services'),
    path('doctor/', views.doctor, name='doctor'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
]
