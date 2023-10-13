#
from django.urls import path,include
from django.contrib import admin
from . import views 
from .views import submit_appointment
from .views import ContactMessageView
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('submit_appointment/', views.submit_appointment, name='submit_appointment'),
    path('service_selection.html', views.service_selection, name='service_selection'),
    path('about/', views.about, name='about'),  # Corrected the view function name
    path('our_services/', views.our_services, name='our_services'),
    path('about/service_selection.html', views.service_selection, name='service_selection'),
    path('our_services/service_selection.html', views.service_selection, name='service_selection'),
    path('service_selection.html', views.service_selection, name='contact_service_selection'),
    path('contact/service_selection.html', views.service_selection, name='contact_service_selection'),
    path('submit_appointment/', views.submit_appointment, name='submit_appointment'),
    path('contact_message/', ContactMessageView.as_view(), name='save_contact_message'),

]
 


    
