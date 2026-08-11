from django.core.management.base import BaseCommand
from nursery.models import Product, GalleryItem, Testimonial, Service, SiteSetting

class Command(BaseCommand):
    help = 'Seed database with initial products, gallery items, testimonials, services, and site settings'

    def handle(self, *args, **options):
        self.stdout.write('Seeding initial data...')

        # Site Setting
        SiteSetting.objects.get_or_create(
            id=1,
            defaults={
                'site_title': 'Malik Dhakki Dates Nursery',
                'phone_number': '+923394027665',
                'whatsapp_number': '923469892120',
                'email': 'malik.dhakki.dates.nursery@gmail.com',
                'address': 'Main chashma road Dhakki D.I.Khan, KPK, Pakistan',
                'years_of_farming': '30+',
                'happy_customers': '250+',
                'export_cities': '50+',
                'organic_percentage': '100%',
            }
        )

        # Services
        services_data = [
            {'id': 1, 'title': 'Plantation Guidance', 'icon_class': 'fa-solid fa-seedling', 'description': 'Complete step-by-step guidance for setting up your own date palm plantation — from soil preparation to irrigation and care schedules.', 'link_text': 'Learn More', 'link_url': '/contact/', 'order': 1},
            {'id': 2, 'title': 'Farming Consultancy', 'icon_class': 'fa-solid fa-person-chalkboard', 'description': 'Expert agricultural consultation for established farms struggling with yield, disease, or quality. One-on-one sessions available on-site or via WhatsApp.', 'link_text': 'Book Session', 'link_url': '/contact/', 'order': 2},
            {'id': 3, 'title': 'Bulk Orders & Export', 'icon_class': 'fa-solid fa-boxes-packing', 'description': 'We handle large-scale orders for wholesalers and exporters with export-quality packaging, documentation support, and competitive pricing for high volumes.', 'link_text': 'Get Quote', 'link_url': '/contact/', 'order': 3},
            {'id': 4, 'title': 'Nationwide Delivery', 'icon_class': 'fa-solid fa-truck-ramp-box', 'description': 'Safe and timely delivery of date plants and produce across the country with proper packaging to maintain freshness and plant vitality.', 'link_text': 'Track Order', 'link_url': '/contact/', 'order': 4},
            {'id': 5, 'title': 'Retail & Gifting', 'icon_class': 'fa-solid fa-store', 'description': 'Beautifully packaged premium date gift boxes perfect for Eid, weddings, and corporate gifting. Custom branding available for businesses.', 'link_text': 'Order Gifts', 'link_url': '/contact/', 'order': 5},
            {'id': 6, 'title': 'Plant Nursery', 'icon_class': 'fa-solid fa-leaf', 'description': 'Select from our curated nursery of healthy, certified Kanjor offshoots and tissue-cultured plants. Each plant comes with a care guide.', 'link_text': 'Shop Plants', 'link_url': '/#products', 'order': 6},
        ]

        for s in services_data:
            Service.objects.update_or_create(id=s['id'], defaults=s)

        # Products
        products_data = [
            {
                'id': 1,
                'category': 'plant',
                'badge': 'Best Seller',
                'badge_class': '',
                'name': 'Dhakki Special Date Palm Offshoot',
                'short_name': 'Kanjor Plant',
                'desc': 'Healthy Dates Palm from sucker plant to 1-year-old Kanjor (Dhakki Special (Thulla)) date palm offshoots, ready for transplanting. Comes with roots intact and care guide.',
                'long_desc': 'Our Kanjor Date Palm offshoots are sourced from mature, high-yield mother plants on our farm. Each offshoot is 8-12 months old with a healthy root system. These are genuine Kanjor (Dhakki Special (Thulla)) known for its golden-yellow dates with rich sweetness. Ideal for farm plantations, home gardens, and commercial date orchards. Comes with a care guide and follow-up WhatsApp support.',
                'price': 4500,
                'unit': 'per plant',
                'rating': 4.9,
                'reviews': 142,
                'static_image_path': 'Date_C1.jpg',
            },
            {
                'id': 2,
                'category': 'plant',
                'badge': 'Best Seller',
                'badge_class': '',
                'name': 'Dhakki Special Date Palm Offshoot',
                'short_name': 'Kanjor Plant',
                'desc': 'Healthy Dates Palm from 1 to 3-year-old Kanjor (Dhakki Special (Thulla)) date palm offshoots, ready for transplanting. Comes with roots intact and care guide.',
                'long_desc': 'Our Kanjor Date Palm offshoots are sourced from mature, high-yield mother plants on our farm. Each offshoot is 1 to 3 years old with a healthy root system. These are genuine Kanjor (Dhakki Special (Thulla)) variety known for its golden-yellow dates with rich sweetness. Ideal for farm plantations, home gardens, and commercial date orchards. Comes with a care guide and follow-up WhatsApp support.',
                'price': 4500,
                'unit': 'per plant',
                'rating': 4.9,
                'reviews': 142,
                'static_image_path': 'Date_C2.jpg',
            },
            {
                'id': 3,
                'category': 'plant',
                'badge': 'Best Seller',
                'badge_class': '',
                'name': 'Dhakki Special Date Palm Offshoot',
                'short_name': 'Kanjor Plant',
                'desc': 'Healthy Dates Palm from 3 to 5-year-old Kanjor (Dhakki Special (Thulla)) date palm offshoots, ready for transplanting. Comes with roots intact and care guide.',
                'long_desc': 'Our Kanjor Date Palm offshoots are sourced from mature, high-yield mother plants on our farm. Each offshoot is 3 to 4 years old with a healthy root system. These are genuine Kanjor (Dhakki Special (Thulla)) variety known for its golden-yellow dates with rich sweetness. Ideal for farm plantations, home gardens, and commercial date orchards. Comes with a care guide and follow-up WhatsApp support.',
                'price': 4500,
                'unit': 'per plant',
                'rating': 4.9,
                'reviews': 142,
                'static_image_path': 'Date_C3.jpg',
            },
            {
                'id': 4,
                'category': 'plant',
                'badge': 'Rare',
                'badge_class': 'organic',
                'name': 'Basra Kanjor Plant',
                'short_name': 'Basra Kanjor Plant',
                'desc': 'It is an other verity of Dhakki Dates Plant and its name is "Basra", which is known for its golden-yellow dates with rich sweetness',
                'long_desc': 'It is an other verity of Dhakki Dates Plant and its name is "Basra", which is known for its golden-yellow dates with rich sweetness. All plants are produced under controlled laboratory conditions ensuring 100% authenticity of variety. They are smaller than offshoots but grow faster and produce consistent yields. Recommended for commercial farmers and serious plantation projects. Minimum order: 10 plants.',
                'price': 3200,
                'unit': 'per plant',
                'rating': 4.8,
                'reviews': 34,
                'static_image_path': 'Tosha_Basra.jpeg',
            },
            {
                'id': 5,
                'category': 'plant',
                'badge': 'Rare',
                'badge_class': 'organic',
                'name': 'Shakri Kanjor Plant',
                'short_name': 'Shakri Kanjor Plant',
                'desc': 'It is an other verity of Dhakki Dates Plant and its name is "Shakri", which is known for its red dates with rich sweetness',
                'long_desc': 'It is an other verity of Dhakki Dates Plant and its name is "Shakri", which is known for its red dates with rich sweetness. All plants are produced under controlled laboratory conditions ensuring 100% authenticity of variety. They are smaller than offshoots but grow faster and produce consistent yields. Recommended for commercial farmers and serious plantation projects. Minimum order: 10 plants.',
                'price': 3200,
                'unit': 'per plant',
                'rating': 4.8,
                'reviews': 34,
                'static_image_path': 'Shakri.jpeg',
            },
            {
                'id': 6,
                'category': 'fresh',
                'badge': 'Organic',
                'badge_class': 'organic',
                'name': 'Fresh Dhakki Special Kanjor',
                'short_name': 'Fresh Kanjor',
                'desc': 'Sun-ripened fresh Kanjor dates harvested at peak sweetness. Soft, juicy, and full of natural flavour — straight from the farm.',
                'long_desc': 'Our Fresh Kanjor dates are harvested at the peak of ripeness during the season. These golden-yellow are dried in sun light and turned in to redish color of special dates which have a soft, moist texture with a rich caramel-like sweetness. Free from any preservatives, artificial colours, or chemicals. Sold per kilogram in fresh condition. Best consumed within 2 weeks. Available in retail (1kg) and bulk (5kg, 10kg) packaging.',
                'price': 1100,
                'unit': 'per kg',
                'rating': 4.8,
                'reviews': 318,
                'static_image_path': 'Date_C6.jpg',
            },
            {
                'id': 7,
                'category': 'dry',
                'badge': 'Premium',
                'badge_class': '',
                'name': 'Sun-Dried Chawara (Premium)',
                'short_name': 'Premium Chawara',
                'desc': 'Premium quality Chawara (dry dates) naturally sun-dried on the farm. Rich in nutrients, perfect for everyday use with or without milk its your choice and gifting.',
                'long_desc': 'Our Premium Chawara are naturally sun-dried Kanjor dates with no added sugar or preservatives. The drying process concentrates their natural sweetness and nutrients. These are ideal for daily consumption, cooking, Ramadan, and gifting. Available in beautifully presented gift boxes and bulk export packaging. Shelf life: 6–12 months in a cool dry place.',
                'price': 1100,
                'unit': 'per kg',
                'rating': 5.0,
                'reviews': 204,
                'static_image_path': 'Date_C7.jpg',
            },
            {
                'id': 8,
                'category': 'dry',
                'badge': 'Export Quality',
                'badge_class': '',
                'name': 'Chawara & Kanjor Gift Box (500g)',
                'short_name': 'Chawara Gift Box',
                'desc': 'Elegantly packaged Chawara & Kanjor gift box, perfect for Eid, weddings, and corporate gifting. Premium quality in a beautiful presentation.',
                'long_desc': 'A luxurious gift box containing 500g of our finest Premium Chawara & Kanjor. The box is beautifully designed with traditional patterns and can be customised with a message card. Perfect for Eid gifts, wedding favours, corporate hampers, and special occasions. Custom branding and bulk gift orders also available.',
                'price': 600,
                'unit': 'per box',
                'rating': 4.9,
                'reviews': 88,
                'static_image_path': 'Gift.jpg',
            },
        ]

        for p_data in products_data:
            Product.objects.update_or_create(id=p_data['id'], defaults=p_data)

        self.stdout.write(f'Seeded {len(products_data)} products.')

        # Gallery Items
        gallery_data = [
            {'section': 'farm', 'static_image_path': 'Gallery1.jpg', 'alt_text': 'Date palm grove', 'img_style': 'object-position: bottom;', 'order': 1},
            {'section': 'farm', 'static_image_path': 'Gallery2.jpg', 'alt_text': 'Fresh dates on branch', 'img_style': 'object-position: bottom;', 'order': 2},
            {'section': 'farm', 'static_image_path': 'Gallery3.jpg', 'alt_text': 'Date harvest', 'img_style': '', 'order': 3},
            {'section': 'farm', 'static_image_path': 'Gallery4.jpg', 'alt_text': 'Date products', 'img_style': '', 'order': 4},
            {'section': 'farm', 'static_image_path': 'Gallery5.jpg', 'alt_text': 'Dry dates', 'img_style': '', 'order': 5},
            {'section': 'farm', 'static_image_path': 'Gallery6.jpg', 'alt_text': 'Dry dates', 'img_style': '', 'order': 6},
            {'section': 'farm', 'static_image_path': 'Gallery15.jpg', 'alt_text': 'Dry dates', 'img_style': 'object-position: bottom;', 'order': 7},
            {'section': 'farm', 'static_image_path': 'Gallery16.jpg', 'alt_text': 'Dry dates', 'img_style': 'object-fit: cover; object-position: bottom;', 'order': 8},
            {'section': 'farm', 'static_image_path': 'Gallery17.jpg', 'alt_text': 'Date palm grove', 'img_style': 'object-position: bottom;', 'order': 9},
            {'section': 'farm', 'static_image_path': 'Gallery7.jpg', 'alt_text': 'Fresh dates on branch', 'img_style': '', 'order': 10},
            {'section': 'farm', 'static_image_path': 'Gallery8.jpg', 'alt_text': 'Date harvest', 'img_style': 'object-position: top;', 'order': 11},
            {'section': 'farm', 'static_image_path': 'Gallery9.jpg', 'alt_text': 'Date products', 'img_style': 'object-position: bottom;', 'order': 12},

            {'section': 'chawara', 'static_image_path': 'chwara4.jpg', 'alt_text': 'Date palm grove', 'img_style': 'object-position: bottom;', 'order': 1},
            {'section': 'chawara', 'static_image_path': 'chwara5.jpg', 'alt_text': 'Fresh dates on branch', 'img_style': 'object-position: bottom;', 'order': 2},
            {'section': 'chawara', 'static_image_path': 'chwara6.jpg', 'alt_text': 'Date harvest', 'img_style': '', 'order': 3},
            {'section': 'chawara', 'static_image_path': 'chwara2.jpg', 'alt_text': 'Date products', 'img_style': 'object-fit: cover;', 'order': 4},
            {'section': 'chawara', 'static_image_path': 'chwara7.jpg', 'alt_text': 'Dry dates', 'img_style': '', 'order': 5},
            {'section': 'chawara', 'static_image_path': 'chwara1.jpg', 'alt_text': 'Dry dates', 'img_style': '', 'order': 6},
            {'section': 'chawara', 'static_image_path': 'chwara3.jpg', 'alt_text': 'Dry dates', 'img_style': 'object-position: bottom;', 'order': 7},
            {'section': 'chawara', 'static_image_path': 'chwara8.jpg', 'alt_text': 'Dry dates', 'img_style': 'object-fit: cover; object-position: bottom;', 'order': 8},

            {'section': 'kanjoor', 'static_image_path': 'kanjoor3.jpg', 'alt_text': 'Date palm grove', 'img_style': 'object-position: bottom;', 'order': 1},
            {'section': 'kanjoor', 'static_image_path': 'kanjoor1.jpg', 'alt_text': 'Fresh dates on branch', 'img_style': 'object-position: bottom;', 'order': 2},
            {'section': 'kanjoor', 'static_image_path': 'kanjoor2.jpg', 'alt_text': 'Date harvest', 'img_style': '', 'order': 3},
            {'section': 'kanjoor', 'static_image_path': 'kanjoor5.jpg', 'alt_text': 'Date products', 'img_style': 'object-fit: cover;', 'order': 4},
            {'section': 'kanjoor', 'static_image_path': 'kanjoor6.jpg', 'alt_text': 'Dry dates', 'img_style': '', 'order': 5},
            {'section': 'kanjoor', 'static_image_path': 'kanjoor4.jpg', 'alt_text': 'Dry dates', 'img_style': '', 'order': 6},
            {'section': 'kanjoor', 'static_image_path': 'kanjoor7.jpg', 'alt_text': 'Dry dates', 'img_style': 'object-position: bottom;', 'order': 7},
            {'section': 'kanjoor', 'static_image_path': 'kanjoor8.jpg', 'alt_text': 'Dry dates', 'img_style': 'object-fit: cover; object-position: bottom;', 'order': 8},
        ]

        GalleryItem.objects.all().delete()
        for idx, g_data in enumerate(gallery_data, start=1):
            GalleryItem.objects.create(
                id=idx,
                section=g_data['section'],
                static_image_path=g_data['static_image_path'],
                alt_text=g_data['alt_text'],
                img_style=g_data['img_style'],
                order=g_data['order']
            )

        self.stdout.write(f'Seeded {len(gallery_data)} gallery items.')

        # Testimonials
        testimonials_data = [
            {
                'id': 1,
                'author_name': 'Ahmed Hassan',
                'author_role': 'Date Farmer, Sindh',
                'author_initials': 'AH',
                'text': 'Malik Dhakki Dates Nursery ki kanjor plants bohot healthy hain. Maine 50 plants order kiye the, sab excellent condition mein aaye. Highly recommended for farmers!',
                'rating': 5.0,
                'order': 1
            },
            {
                'id': 2,
                'author_name': 'Zafar Khan',
                'author_role': 'Exporter, Karachi',
                'author_initials': 'ZK',
                'text': "We export dates to UAE and Europe. Malik Dhakki Dates Nursery's Chawara quality is exceptional — consistent size, natural sweetness, and beautiful color. Our clients love it.",
                'rating': 5.0,
                'order': 2
            },
            {
                'id': 3,
                'author_name': 'Fatima Noor',
                'author_role': 'Retail Customer, Lahore',
                'author_initials': 'FN',
                'text': "Fresh Kanjor dates se behtar kuch nahi. We order every season for our family. The taste is unmatched — you can tell they're truly farm-fresh. Jazakallah!",
                'rating': 4.5,
                'order': 3
            },
        ]

        for t_data in testimonials_data:
            Testimonial.objects.update_or_create(id=t_data['id'], defaults=t_data)

        self.stdout.write(f'Seeded {len(testimonials_data)} testimonials.')
        self.stdout.write(self.style.SUCCESS('Successfully seeded all initial data!'))
