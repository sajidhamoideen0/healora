# 🌸 The Glow Clinic — Django Website

A full-featured skin clinic website built with Django.

## Pages Included
- **Home** — Hero, Services, Stats, Doctors, Testimonials, FAQ, CTA
- **Services** — Filterable treatment list
- **Service Detail** — Full description + inline booking form
- **About** — Story, team, testimonials
- **Gallery** — Filterable image gallery
- **Contact** — Contact form + clinic info
- **Book Appointment** — Full booking form

## Quick Setup

```bash
# 1. Create virtual environment
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run migrations
python manage.py makemigrations
python manage.py migrate

# 4. Seed sample data (services, doctors, testimonials, FAQs)
python manage.py seed_data

# 5. Create admin user
python manage.py createsuperuser

# 6. Start the server
python manage.py runserver
```

## Open in Browser
- **Website:** http://127.0.0.1:8000/
- **Admin Panel:** http://127.0.0.1:8000/admin/

## Manage Content via Admin
Log in to the admin panel to add/edit:
- Services (with images, descriptions, categories)
- Doctors (with photos and bios)
- Testimonials
- Gallery images
- FAQs
- View all appointment requests and contact messages

## Pages & URLs
| Page | URL |
|------|-----|
| Home | / |
| Services | /services/ |
| Service Detail | /services/<id>/ |
| About | /about/ |
| Gallery | /gallery/ |
| Contact | /contact/ |
| Book Appointment | /book-appointment/ |
| Admin | /admin/ |

## Adding Your Images
Upload images through the Django Admin panel for:
- Doctor photos → Doctors section
- Service images → Services section
- Gallery images → Gallery section

## Customisation
- **Clinic name/details** → Edit `base.html`
- **Colors** → Edit CSS variables in `style.css` (`:root` section)
- **Contact info** → Edit `contact.html` and `base.html` footer
- **Email** → Update `EMAIL_HOST_*` settings in `settings.py`
