from datetime import timezone, datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Service, Appointment, AppointmentSlot
from django.conf import settings
def index(request): 
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def service_selection(request):
    return render(request, 'service_selection.html')

def about(request):
    return render(request, 'about.html')


def our_services(request):
    return render(request, 'our_services.html')


from django.http import JsonResponse
from django.utils import timezone
from .models import Appointment
from .models import Appointment, Service
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Service, Appointment
from django.core.mail import send_mail

@csrf_exempt
def submit_appointment(request):
    if request.method == 'POST':
        # Get data from the POST request
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        service_id = request.POST.get('service')
        appointment_date = request.POST.get('appointment_date')
        print('Service ID:', service_id)  # Add this line to print the service ID
        try:
            # Retrieve the service based on the provided ID
            service = Service.objects.get(pk=service_id)
        except Service.DoesNotExist:
            print('Service does not exist')  # Add this line to print if service doesn't exist
            return JsonResponse({'message': 'Service does not exist.'}, status=400)

        # Convert appointment_date to a Python datetime object
        appointment_slot = timezone.datetime.strptime(appointment_date, "%Y-%m-%d").date()

        # Create a new Appointment instance and save it to the database
        appointment = Appointment(name=name, phone=phone, email=email, service=service, appointment_date=appointment_slot)
        appointment.save()

           # Send an email confirmation
        send_confirmation_email(name, email, service.name, appointment_date)

        return JsonResponse({'message': 'Appointment saved successfully!'})

    return JsonResponse({'message': 'Invalid request method.'}, status=400)

def send_confirmation_email(name, email, service, appointment_date):
    subject = 'Car Service Appointment Confirmation'
    message = f'Dear {name},\n\n Your appointment for {service} on {appointment_date} has been confirmed.'

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )



 

#contact us
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import ContactMessage
import json

@method_decorator(csrf_exempt, name='dispatch')  # Allow CSRF exemption for this view
class ContactMessageView(View):

    def post(self, request):
        # Parse the JSON data from the request
        data = json.loads(request.body)
        
        # Extract the data
        name = data.get('name', '')
        email = data.get('email', '')
        message = data.get('message', '')

        # Save the contact message to the database
        contact_message = ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )
        contact_message.save()

        # You can return a response if needed
        response_data = {'status': 'Message saved successfully.'}
        return JsonResponse(response_data, status=200)
    

    

