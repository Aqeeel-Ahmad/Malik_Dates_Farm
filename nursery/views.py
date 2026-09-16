import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import Product, GalleryItem, Testimonial, Service, ContactInquiry, NewsletterSubscriber, Order, OrderItem

def home_view(request):
    search_query = request.GET.get('q', '').strip()
    category_query = request.GET.get('category', '').strip()

    try:
        products = Product.objects.filter(is_active=True)
        if search_query:
            products = products.filter(name__icontains=search_query) | products.filter(desc__icontains=search_query)
        if category_query and category_query != 'all':
            products = products.filter(category=category_query)
    except Exception:
        products = []

    products_list = []
    for p in products:
        products_list.append({
            'id': p.id,
            'category': p.category,
            'badge': p.badge or '',
            'badgeClass': p.badge_class or '',
            'name': p.name,
            'shortName': p.short_name,
            'desc': p.desc,
            'longDesc': p.long_desc,
            'price': float(p.price),
            'unit': p.unit,
            'rating': p.rating,
            'reviews': p.reviews,
            'img': p.image_url,
        })
    
    context = {
        'products': products,
        'products_json': json.dumps(products_list),
        'search_query': search_query,
        'selected_category': category_query or 'all',
    }
    return render(request, 'index.html', context)

def about_view(request):
    return render(request, 'about.html')

def services_view(request):
    try:
        services = Service.objects.filter(is_active=True)
    except Exception:
        services = []
    return render(request, 'services.html', {'services': services})

def gallery_view(request):
    try:
        farm_items = GalleryItem.objects.filter(section='farm')
        chawara_items = GalleryItem.objects.filter(section='chawara')
        kanjoor_items = GalleryItem.objects.filter(section='kanjoor')
        testimonials = Testimonial.objects.filter(is_published=True)
    except Exception:
        farm_items = []
        chawara_items = []
        kanjoor_items = []
        testimonials = []

    context = {
        'farm_items': farm_items,
        'chawara_items': chawara_items,
        'kanjoor_items': kanjoor_items,
        'testimonials': testimonials,
    }
    return render(request, 'gallery.html', context)

def contact_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('fName') or request.POST.get('full_name', '')
        phone = request.POST.get('fPhone') or request.POST.get('phone', '')
        email = request.POST.get('fEmail') or request.POST.get('email', '')
        inquiry_type = request.POST.get('fType') or request.POST.get('inquiry_type', '')
        message = request.POST.get('fMsg') or request.POST.get('message', '')

        if full_name and phone and message:
            ContactInquiry.objects.create(
                full_name=full_name,
                phone=phone,
                email=email,
                inquiry_type=inquiry_type,
                message=message
            )
            if request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.content_type == 'application/json':
                return JsonResponse({'status': 'success', 'message': 'Inquiry sent successfully!'})
            messages.success(request, 'Thank you! Your message has been received.')
            return redirect('contact')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.content_type == 'application/json':
                return JsonResponse({'status': 'error', 'message': 'Please fill required fields.'}, status=400)
            messages.error(request, 'Please fill in all required fields.')

    return render(request, 'contact.html')

@require_POST
def subscribe_newsletter_view(request):
    email = request.POST.get('email') or request.POST.get('nlEmail', '')
    if email and '@' in email:
        NewsletterSubscriber.objects.get_or_create(email=email.strip())
        return JsonResponse({'status': 'success', 'message': 'Subscribed successfully! Thank you.'})
    return JsonResponse({'status': 'error', 'message': 'Please enter a valid email address.'}, status=400)

@require_POST
def create_order_view(request):
    try:
        data = json.loads(request.body)
        cart_items = data.get('cart', [])
        customer_name = data.get('customer_name', 'WhatsApp Customer')
        customer_phone = data.get('customer_phone', '')

        if not cart_items:
            return JsonResponse({'status': 'error', 'message': 'Cart is empty'}, status=400)

        total_amount = 0
        order_notes = []
        for item in cart_items:
            qty = int(item.get('qty', 1))
            price = float(item.get('price', 0))
            subtotal = qty * price
            total_amount += subtotal
            order_notes.append(f"{item.get('name', 'Product')} x{qty} = Rs. {subtotal:,.2f}")

        order = Order.objects.create(
            customer_name=customer_name,
            customer_phone=customer_phone,
            total_amount=total_amount,
            notes="\n".join(order_notes)
        )

        for item in cart_items:
            product_id = item.get('id')
            product_obj = Product.objects.filter(id=product_id).first() if product_id else None
            qty = int(item.get('qty', 1))
            price = float(item.get('price', 0))
            subtotal = qty * price

            OrderItem.objects.create(
                order=order,
                product=product_obj,
                product_name=item.get('name', 'Product'),
                price=price,
                quantity=qty,
                subtotal=subtotal
            )

        return JsonResponse({'status': 'success', 'order_number': order.order_number})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
