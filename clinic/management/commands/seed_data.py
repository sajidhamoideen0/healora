from django.core.management.base import BaseCommand
from clinic.models import Service, Doctor, Testimonial, FAQ


class Command(BaseCommand):
    help = 'Seed the database with sample clinic data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')

        # Services
        services_data = [
            {
                'title': 'HydraFacial',
                'category': 'skin',
                'short_description': 'Deep cleanse, exfoliate and hydrate for instantly radiant, glowing skin in 30 minutes.',
                'full_description': 'HydraFacial is a multi-step facial treatment that cleanses, exfoliates, extracts, and hydrates the skin simultaneously using a patented Vortex-Fusion delivery system.\n\nThe treatment is suitable for all skin types and addresses concerns like fine lines, wrinkles, oily and congested skin, hyperpigmentation, and dull skin.\n\nExpect a visible glow immediately after your first session, with results improving over a course of treatments.',
                'icon': '✨',
                'is_featured': True,
                'order': 1,
            },
            {
                'title': 'Chemical Peels',
                'category': 'skin',
                'short_description': 'Resurface and renew with targeted peels that fade pigmentation, scars and uneven skin tone.',
                'full_description': 'Chemical peels use clinically formulated acids to exfoliate the outer layers of skin, revealing fresher, brighter skin underneath.\n\nWe offer a range of peels — from superficial glycolic peels with zero downtime to deeper TCA peels for significant skin resurfacing.\n\nIdeal for acne scars, sun damage, fine lines, and hyperpigmentation.',
                'icon': '💆',
                'is_featured': True,
                'order': 2,
            },
            {
                'title': 'Laser Hair Removal',
                'category': 'laser',
                'short_description': 'Long-lasting hair reduction using FDA-approved laser technology safe for all skin types.',
                'full_description': 'Our Nd:YAG and Diode laser systems are safe and effective for all Fitzpatrick skin types, including darker Indian skin tones.\n\nMost patients achieve 70–90% permanent reduction after a recommended course of 6–8 sessions.\n\nTreatment areas include full body, face, underarms, bikini line, and more.',
                'icon': '⚡',
                'is_featured': True,
                'order': 3,
            },
            {
                'title': 'Acne Treatment',
                'category': 'skin',
                'short_description': 'Comprehensive acne management from mild breakouts to severe cystic conditions.',
                'full_description': 'Our dermatologists take a root-cause approach to acne — assessing hormonal factors, diet, lifestyle, and skin type before recommending a treatment plan.\n\nTreatments may include topical and oral medications, chemical peels, laser therapy, comedone extractions, and LED light therapy.\n\nWe also offer scar reduction treatments for post-acne marks.',
                'icon': '🌿',
                'is_featured': True,
                'order': 4,
            },
            {
                'title': 'Botox & Fillers',
                'category': 'anti_aging',
                'short_description': 'Subtle, natural-looking anti-aging treatments administered by expert aesthetic doctors.',
                'full_description': 'Our aesthetic doctors use FDA-approved neurotoxins and hyaluronic acid fillers to soften fine lines, restore volume, and enhance facial contours.\n\nWe believe in natural results — you should look refreshed, not done. Every procedure is tailored to your facial anatomy and aesthetic goals.\n\nDowntime is minimal, with most patients resuming normal activities the same day.',
                'icon': '💉',
                'is_featured': True,
                'order': 5,
            },
            {
                'title': 'PRP Hair Therapy',
                'category': 'hair',
                'short_description': 'Stimulate natural hair regrowth using your own platelet-rich plasma for thicker, fuller hair.',
                'full_description': 'Platelet-Rich Plasma (PRP) therapy involves drawing a small amount of your blood, concentrating the platelets, and injecting them into your scalp.\n\nGrowth factors in platelets stimulate hair follicles, promoting regrowth and reducing hair fall.\n\nIdeal for androgenetic alopecia, telogen effluvium, and general hair thinning. Results visible within 3–6 months.',
                'icon': '🔬',
                'is_featured': True,
                'order': 6,
            },
        ]

        for s in services_data:
            Service.objects.get_or_create(title=s['title'], defaults=s)

        # Doctors
        doctors_data = [
            {
                'name': 'Priya Sharma',
                'designation': 'Senior Dermatologist & Cosmetologist',
                'specialization': 'Medical Dermatology, Acne, Pigmentation',
                'bio': 'MBBS, MD Dermatology (AIIMS Delhi). Dr. Priya has over 12 years of experience in clinical and cosmetic dermatology. She specialises in acne management, pigmentation disorders, and cosmetic procedures.',
                'experience_years': 12,
                'order': 1,
            },
            {
                'name': 'Anil Mehta',
                'designation': 'Laser & Aesthetic Specialist',
                'specialization': 'Laser Dermatology, Body Contouring',
                'bio': 'MBBS, DNB Dermatology. Internationally trained in laser dermatology with fellowships in the USA and Germany. Dr. Anil specialises in advanced laser treatments and non-surgical aesthetic procedures.',
                'experience_years': 9,
                'order': 2,
            },
            {
                'name': 'Neha Kapoor',
                'designation': 'Trichologist & Hair Restoration Expert',
                'specialization': 'Hair Loss, PRP Therapy, Scalp Disorders',
                'bio': 'MBBS, MD Dermatology with advanced trichology training. Dr. Neha is a pioneer in PRP therapy and has helped thousands of patients regain their confidence through effective hair restoration.',
                'experience_years': 8,
                'order': 3,
            },
        ]

        for d in doctors_data:
            Doctor.objects.get_or_create(name=d['name'], defaults=d)

        # Testimonials
        testimonials_data = [
            {'name': 'Priya M.', 'review': 'I struggled with acne for years. After just 3 sessions at The Glow Clinic, my skin is completely transformed. The doctors truly listen and care about your wellbeing.', 'rating': 5, 'service_taken': 'Acne Treatment', 'location': 'Bangalore', 'is_featured': True},
            {'name': 'Rohit K.', 'review': 'The laser hair removal was painless and incredibly effective. I\'m so glad I chose this clinic — professional, hygienic and genuinely caring staff throughout.', 'rating': 5, 'service_taken': 'Laser Hair Removal', 'location': 'Mumbai', 'is_featured': True},
            {'name': 'Sunita J.', 'review': 'Dr. Priya\'s expertise with anti-aging treatments is unmatched. Natural-looking results that have taken years off my appearance. I look refreshed, not overdone!', 'rating': 5, 'service_taken': 'Botox & Fillers', 'location': 'Delhi', 'is_featured': True},
            {'name': 'Arjun V.', 'review': 'My hair loss had been a source of anxiety for two years. The PRP therapy here has genuinely changed my life. I finally have my confidence back.', 'rating': 5, 'service_taken': 'PRP Hair Therapy', 'location': 'Bangalore', 'is_featured': True},
            {'name': 'Meena T.', 'review': 'The HydraFacial left my skin glowing for weeks. The ambience is so calm and luxurious — feels like a high-end spa with medical-grade results.', 'rating': 5, 'service_taken': 'HydraFacial', 'location': 'Chennai', 'is_featured': True},
            {'name': 'Kiran D.', 'review': 'I\'ve tried so many clinics but none matched the personalised attention I received here. They don\'t just treat symptoms — they understand the root cause.', 'rating': 5, 'service_taken': 'Skin Consultation', 'location': 'Hyderabad', 'is_featured': True},
        ]

        for t in testimonials_data:
            Testimonial.objects.get_or_create(name=t['name'], defaults=t)

        # FAQs
        faqs_data = [
            {'question': 'How do I know which treatment is right for me?', 'answer': 'We recommend starting with a thorough consultation. Our dermatologists assess your skin type, concerns and medical history to create a fully personalised treatment plan that delivers safe, effective results.', 'order': 1},
            {'question': 'Are the treatments safe for all skin types?', 'answer': 'Yes. We use clinically validated, FDA-approved equipment and products suitable for all Fitzpatrick skin types, including darker Indian skin tones. Your safety is our highest priority at every step.', 'order': 2},
            {'question': 'How many sessions will I need?', 'answer': 'The number of sessions varies depending on your condition and treatment. During your consultation, your doctor will outline a clear treatment plan with realistic timelines and expected outcomes.', 'order': 3},
            {'question': 'Is there any downtime after treatments?', 'answer': 'Many of our treatments have minimal to no downtime. For procedures like laser treatments or chemical peels, you may experience mild redness for 24–48 hours. We will guide you on aftercare for every treatment.', 'order': 4},
            {'question': 'How do I book an appointment?', 'answer': 'You can book online via our website, call us at +91 98765 43210, or walk into our clinic. We offer flexible appointment slots including early mornings and Saturdays.', 'order': 5},
            {'question': 'Do you offer payment plans or EMI?', 'answer': 'Yes, we offer convenient EMI options through major credit cards and select financing partners. Speak to our front desk team at the time of your consultation to learn more.', 'order': 6},
        ]

        for f in faqs_data:
            FAQ.objects.get_or_create(question=f['question'], defaults=f)

        self.stdout.write(self.style.SUCCESS('✅ Database seeded successfully!'))
