from django.db import models


class Service(models.Model):
    CATEGORY_CHOICES = [
        ('skin', 'Skin Treatments'),
        ('hair', 'Hair Treatments'),
        ('laser', 'Laser Treatments'),
        ('anti_aging', 'Anti-Aging'),
        ('body', 'Body Treatments'),
    ]
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='skin')
    short_description = models.CharField(max_length=300)
    full_description = models.TextField()
    icon = models.CharField(max_length=100, default='✨')  # emoji or icon class
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Doctor(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    specialization = models.CharField(max_length=300)
    bio = models.TextField()
    photo = models.ImageField(upload_to='doctors/', blank=True, null=True)
    experience_years = models.IntegerField(default=0)
    linkedin = models.URLField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    review = models.TextField()
    rating = models.IntegerField(default=5)
    service_taken = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    is_featured = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.rating}★"


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    service = models.CharField(max_length=200)
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.preferred_date} ({self.status})"


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    subject = models.CharField(max_length=300)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"


class GalleryImage(models.Model):
    CATEGORY_CHOICES = [
        ('before_after', 'Before & After'),
        ('clinic', 'Clinic'),
        ('team', 'Team'),
        ('treatment', 'Treatment'),
    ]
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='treatment')
    image = models.ImageField(upload_to='gallery/')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.CharField(max_length=400)
    answer = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.question
