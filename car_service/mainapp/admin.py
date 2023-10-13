from django.contrib import admin
from .models import ContactMessage
# Register your models here.


from django.contrib import admin
from .models import Appointment

admin.site.register(Appointment)







# Register the ContactMessage model
admin.site.register(ContactMessage)
