import os
import uuid
from django.db import models
from django.conf import settings

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('plant', 'Date Plant'),
        ('fresh', 'Fresh Dates'),
        ('dry', 'Dry Dates'),
    ]

    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='plant')
    badge = models.CharField(max_length=50, blank=True, null=True)
    badge_class = models.CharField(max_length=50, blank=True, null=True)
    desc = models.TextField(help_text="Short description shown on card")
    long_desc = models.TextField(help_text="Full description shown in modal")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=50, default="per plant")
    rating = models.FloatField(default=5.0)
    reviews = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    static_image_path = models.CharField(max_length=255, blank=True, null=True, help_text="Fallback static image path relative to images/")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        if self.image:
            try:
                return self.image.url
            except Exception:
                pass
        if self.static_image_path:
            path = str(self.static_image_path).strip()
            if path.startswith('http://') or path.startswith('https://') or path.startswith('/'):
                return path
            if path.startswith('static/'):
                path = path.replace('static/', '')
            if path.startswith('images/'):
                path = path.replace('images/', '')
            return f"/static/images/{path}"
        return "/static/images/Main_hero.jpeg"


class GalleryItem(models.Model):
    SECTION_CHOICES = [
        ('farm', 'Farm & Harvest'),
        ('chawara', 'Making Chawara'),
        ('kanjoor', 'Making Kanjor'),
    ]

    title = models.CharField(max_length=200, blank=True)
    section = models.CharField(max_length=20, choices=SECTION_CHOICES, default='farm')
    image = models.ImageField(upload_to='gallery/', blank=True, null=True)
    static_image_path = models.CharField(max_length=255, blank=True, null=True)
    alt_text = models.CharField(max_length=200, default="Gallery image")
    img_style = models.CharField(max_length=255, blank=True, null=True, help_text="Inline style like object-position")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.get_section_display()} - {self.title or self.id}"

    @property
    def image_url(self):
        if self.image:
            try:
                return self.image.url
            except Exception:
                pass
        if self.static_image_path:
            path = str(self.static_image_path).strip()
            if path.startswith('http://') or path.startswith('https://') or path.startswith('/'):
                return path
            if path.startswith('static/'):
                path = path.replace('static/', '')
            if path.startswith('images/'):
                path = path.replace('images/', '')

            # Check if chawara vs chwara filename resolution is needed
            full_path = os.path.join(settings.BASE_DIR, 'static', 'images', path)
            if not os.path.exists(full_path) and 'chawara' in path:
                alt_path = path.replace('chawara', 'chwara')
                if os.path.exists(os.path.join(settings.BASE_DIR, 'static', 'images', alt_path)):
                    path = alt_path

            return f"/static/images/{path}"
        return ""


class Testimonial(models.Model):
    author_name = models.CharField(max_length=100)
    author_role = models.CharField(max_length=100)
    author_initials = models.CharField(max_length=10)
    text = models.TextField()
    rating = models.FloatField(default=5.0)
    is_published = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.author_name} ({self.author_role})"


class Service(models.Model):
    title = models.CharField(max_length=200)
    icon_class = models.CharField(max_length=100, default='fa-solid fa-seedling', help_text='FontAwesome icon class')
    description = models.TextField()
    link_text = models.CharField(max_length=100, default='Learn More')
    link_url = models.CharField(max_length=255, default='/contact/')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.title


class SiteSetting(models.Model):
    site_title = models.CharField(max_length=200, default='Malik Dhakki Dates Nursery')
    phone_number = models.CharField(max_length=50, default='+923394027665')
    whatsapp_number = models.CharField(max_length=50, default='923469892120')
    email = models.EmailField(default='malik.dhakki.dates.nursery@gmail.com')
    address = models.CharField(max_length=255, default='Main chashma road Dhakki D.I.Khan, KPK, Pakistan')
    facebook_url = models.URLField(blank=True, default='https://www.facebook.com/itsdhakkidates')
    instagram_url = models.URLField(blank=True, default='#')
    youtube_url = models.URLField(blank=True, default='#')
    tiktok_url = models.URLField(blank=True, default='#')
    
    # Hero & Stats
    years_of_farming = models.CharField(max_length=20, default='30+')
    happy_customers = models.CharField(max_length=20, default='250+')
    export_cities = models.CharField(max_length=20, default='50+')
    organic_percentage = models.CharField(max_length=20, default='100%')

    class Meta:
        verbose_name = 'Site Setting'
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return self.site_title


class ContactInquiry(models.Model):
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    inquiry_type = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Contact Inquiries"

    def __str__(self):
        return f"Inquiry from {self.full_name} ({self.created_at.strftime('%Y-%m-%d %H:%M')})"


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-subscribed_at']

    def __str__(self):
        return self.email


class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Shipped', 'Shipped'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    order_number = models.CharField(max_length=50, unique=True, editable=False)
    customer_name = models.CharField(max_length=150, blank=True, default='WhatsApp Customer')
    customer_phone = models.CharField(max_length=50, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    notes = models.TextField(blank=True, help_text="Order items & instructions")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = f"ORD-{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.order_number} - Rs. {self.total_amount} ({self.status})"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    product_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product_name} x{self.quantity}"
