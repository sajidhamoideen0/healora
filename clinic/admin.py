from django.contrib import admin
from .models import Service, Doctor, Testimonial, Appointment, ContactMessage, GalleryImage, FAQ


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_featured', 'order']
    list_editable = ['is_featured', 'order']
    list_filter = ['category', 'is_featured']
    search_fields = ['title']


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation', 'experience_years', 'order']
    list_editable = ['order']


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'service_taken', 'is_featured', 'created_at']
    list_editable = ['is_featured']
    list_filter = ['rating', 'is_featured']


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'service', 'preferred_date', 'preferred_time', 'status', 'created_at']
    list_editable = ['status']
    list_filter = ['status', 'preferred_date']
    search_fields = ['name', 'email', 'phone']
    readonly_fields = ['created_at']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'is_read', 'created_at']
    list_editable = ['is_read']
    readonly_fields = ['created_at']


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'order']
    list_editable = ['order']
    list_filter = ['category']


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'order']
    list_editable = ['order']
