from django import forms
from .models import Appointment, ContactMessage


class AppointmentForm(forms.ModelForm):
    preferred_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-input'}),
    )
    preferred_time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-input'}),
    )

    SERVICE_CHOICES = [
    ('', 'Select a Service'),
    ('Homoeopathic Consultation', 'Homoeopathic Consultation'),
    ('Skin & Aesthetic Care', 'Skin & Aesthetic Care'),
    ('Acne & Skin Wellness Program', 'Acne & Skin Wellness Program'),
    ('Hair & Scalp Care', 'Hair & Scalp Care'),
    ('Preventive & Wellness Care', 'Preventive & Wellness Care'),
    ('Other', 'Other / General Consultation'),
]

    service = forms.ChoiceField(
        choices=SERVICE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-input'})
    )

    class Meta:
        model = Appointment
        fields = ['name', 'email', 'phone', 'service', 'preferred_date', 'preferred_time', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Your Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'your@email.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': '+91 98765 43210'}),
            'message': forms.Textarea(attrs={'class': 'form-input', 'rows': 4, 'placeholder': 'Tell us about your skin concerns...'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Your Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'your@email.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': '+91 98765 43210'}),
            'subject': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'How can we help?'}),
            'message': forms.Textarea(attrs={'class': 'form-input', 'rows': 5, 'placeholder': 'Your message...'}),
        }
