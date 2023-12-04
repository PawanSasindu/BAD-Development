from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('otherservice/', views.other_services, name='other_services'),
]
