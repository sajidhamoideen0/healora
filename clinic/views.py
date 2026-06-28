from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Service, Doctor, Testimonial, GalleryImage, FAQ
from .forms import AppointmentForm, ContactForm
from django.core.mail import send_mail


def home(request):
    featured_services = Service.objects.filter(is_featured=True)[:6]
    doctors = Doctor.objects.all()
    testimonials = Testimonial.objects.filter(is_featured=True)[:6]
    faqs = FAQ.objects.all()[:6]

    appointment_form = AppointmentForm()
    if request.method == 'POST' and 'appointment_submit' in request.POST:
        appointment_form = AppointmentForm(request.POST)
        if appointment_form.is_valid():
            appointment_form.save()
            messages.success(request, 'Your appointment request has been received! We will contact you shortly.')
            return redirect('home')

    context = {
        'featured_services': featured_services,
        'doctors': doctors,
        'testimonials': testimonials,
        'faqs': faqs,
        'appointment_form': appointment_form,
        'stats': [
            {'number': '15+', 'label': 'Years of Excellence'},
            {'number': '50,000+', 'label': 'Happy Patients'},
            {'number': '30+', 'label': 'Treatments Offered'},
            {'number': '10+', 'label': 'Expert Dermatologists'},
        ]
    }
    return render(request, 'clinic/home.html', context)


def services(request):
    category = request.GET.get('category', '')
    all_services = Service.objects.all()
    if category:
        all_services = all_services.filter(category=category)

    categories = Service.CATEGORY_CHOICES
    context = {
        'services': all_services,
        'categories': categories,
        'active_category': category,
    }
    return render(request, 'clinic/services.html', context)


def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    related = Service.objects.filter(category=service.category).exclude(pk=pk)[:3]
    appointment_form = AppointmentForm(initial={'service': service.title})
    context = {
        'service': service,
        'related': related,
        'appointment_form': appointment_form,
    }
    return render(request, 'clinic/service_detail.html', context)


def about(request):
    doctors = Doctor.objects.all()
    testimonials = Testimonial.objects.filter(is_featured=True)
    context = {
        'doctors': doctors,
        'testimonials': testimonials,
    }
    return render(request, 'clinic/about.html', context)


def gallery(request):
    category = request.GET.get('category', '')
    images = GalleryImage.objects.all()
    if category:
        images = images.filter(category=category)
    categories = GalleryImage.CATEGORY_CHOICES
    context = {
        'images': images,
        'categories': categories,
        'active_category': category,
    }
    return render(request, 'clinic/gallery.html', context)


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_msg = form.save()
            try:
                send_mail(
                    subject=f"New Contact: {contact_msg.subject}",
                    message=f"From: {contact_msg.name} ({contact_msg.email})\nPhone: {contact_msg.phone}\n\n{contact_msg.message}",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=True,
                )
            except Exception:
                pass
            messages.success(request, 'Thank you! Your message has been sent. We\'ll get back to you within 24 hours.')
            return redirect('contact')
    return render(request, 'clinic/contact.html', {'form': form})



from django.core.mail import send_mail

def book_appointment(request):
    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            
            # Send confirmation email
            send_mail(
                subject='Appointment Confirmed - Healora Homoeo Clinic',
                message=f'Dear {appointment.name},\n\nYour appointment has been booked for {appointment.preferred_date}.\n\nThank you,\nHealora Homoeo Clinic',
                from_email=None,
                recipient_list=[appointment.email],
            )
            
            messages.success(request, f'Appointment booked for {appointment.preferred_date}! We will confirm via email.')
            return redirect('book_appointment')
    return render(request, 'clinic/appointment.html', {'form': form})