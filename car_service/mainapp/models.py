from django.db import models

# Create your models here.


from django.db import models
from django.utils import timezone

class Service(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class AppointmentSlot(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    slot_time = models.DateTimeField()

    def __str__(self):
        return f"{self.service.name} - {self.slot_time}"

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)  # Use ForeignKey to reference Service model
    appointment_date = models.DateTimeField(default=timezone.now)  # Use DateTimeField for appointment date

    def __str__(self):
        return f"{self.name} "  # Customize the display in the admin interface


from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
