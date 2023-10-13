from django import forms

class AppointmentForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    phone = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(required=True)
    service = forms.CharField(max_length=100, required=True)
    appointment_date = forms.DateField(required=True)
