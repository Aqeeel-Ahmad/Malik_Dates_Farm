from django.contrib import admin
from .models import Product, GalleryItem, Testimonial, Service, SiteSetting, ContactInquiry, NewsletterSubscriber, Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product_name', 'price', 'quantity', 'subtotal')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'customer_name', 'customer_phone', 'total_amount', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('order_number', 'customer_name', 'customer_phone', 'notes')
    list_editable = ('status',)
    inlines = [OrderItemInline]
    readonly_fields = ('order_number', 'total_amount', 'created_at')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_name', 'category', 'price', 'unit', 'rating', 'reviews', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('name', 'short_name', 'desc')
    list_editable = ('price', 'is_active', 'rating')
    exclude = ('static_image_path',)

@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'section', 'order', 'alt_text')
    list_filter = ('section',)
    search_fields = ('title', 'alt_text')
    list_editable = ('order',)
    exclude = ('static_image_path',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'author_name', 'author_role', 'rating', 'is_published', 'order')
    list_filter = ('is_published', 'rating')
    search_fields = ('author_name', 'text')
    list_editable = ('is_published', 'order')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'icon_class', 'order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')
    list_editable = ('order', 'is_active')

@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('site_title', 'phone_number', 'whatsapp_number', 'email')
    
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone', 'email', 'inquiry_type', 'created_at')
    list_filter = ('inquiry_type', 'created_at')
    search_fields = ('full_name', 'phone', 'email', 'message')
    readonly_fields = ('full_name', 'phone', 'email', 'inquiry_type', 'message', 'created_at')

@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'subscribed_at')
    search_fields = ('email',)
    readonly_fields = ('email', 'subscribed_at')
