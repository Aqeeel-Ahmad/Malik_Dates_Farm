// ============================================================
// PRODUCT DATA (Populated from Django or fallback)
// ============================================================
let products = window.INITIAL_PRODUCTS || [
    {
        id: 1,
        category: 'plant',
        badge: 'Best Seller',
        badgeClass: '',
        name: 'Dhakki Special Date Palm Offshoot',
        shortName: 'Kanjor Plant',
        desc: 'Healthy Dates Palm from sucker plant to 1-year-old Kanjor (Dhakki Special (Thulla)) date palm offshoots, ready for transplanting. Comes with roots intact and care guide.',
        longDesc: 'Our Kanjor Date Palm offshoots are sourced from mature, high-yield mother plants on our farm. Each offshoot is 8-12 months old with a healthy root system. These are genuine Kanjor (Dhakki Special (Thulla)) known for its golden-yellow dates with rich sweetness. Ideal for farm plantations, home gardens, and commercial date orchards. Comes with a care guide and follow-up WhatsApp support.',
        price: 4500,
        unit: 'per plant',
        rating: 4.9,
        reviews: 142,
        img: '/static/images/Date_C1.jpg',
    },
    {
        id: 2,
        category: 'plant',
        badge: 'Best Seller',
        badgeClass: '',
        name: 'Dhakki Special Date Palm Offshoot',
        shortName: 'Kanjor Plant',
        desc: 'Healthy Dates Palm from 1 to 3-year-old Kanjor (Dhakki Special (Thulla)) date palm offshoots, ready for transplanting. Comes with roots intact and care guide.',
        longDesc: 'Our Kanjor Date Palm offshoots are sourced from mature, high-yield mother plants on our farm. Each offshoot is 1 to 3 years old with a healthy root system. These are genuine Kanjor (Dhakki Special (Thulla)) variety known for its golden-yellow dates with rich sweetness. Ideal for farm plantations, home gardens, and commercial date orchards. Comes with a care guide and follow-up WhatsApp support.',
        price: 4500,
        unit: 'per plant',
        rating: 4.9,
        reviews: 142,
        img: '/static/images/Date_C2.jpg',
    },
    {
        id: 3,
        category: 'plant',
        badge: 'Best Seller',
        badgeClass: '',
        name: 'Dhakki Special Date Palm Offshoot',
        shortName: 'Kanjor Plant',
        desc: 'Healthy Dates Palm from 3 to 5-year-old Kanjor (Dhakki Special (Thulla)) date palm offshoots, ready for transplanting. Comes with roots intact and care guide.',
        longDesc: 'Our Kanjor Date Palm offshoots are sourced from mature, high-yield mother plants on our farm. Each offshoot is 3 to 4 years old with a healthy root system. These are genuine Kanjor (Dhakki Special (Thulla)) variety known for its golden-yellow dates with rich sweetness. Ideal for farm plantations, home gardens, and commercial date orchards. Comes with a care guide and follow-up WhatsApp support.',
        price: 4500,
        unit: 'per plant',
        rating: 4.9,
        reviews: 142,
        img: '/static/images/Date_C3.jpg',
    },
    {
        id: 4,
        category: 'plant',
        badge: 'Rare',
        badgeClass: 'organic',
        name: 'Basra Kanjor Plant',
        shortName: 'Basra Kanjor Plant',
        desc: 'It is an other verity of Dhakki Dates Plant and its name is "Basra", which is known for its golden-yellow dates with rich sweetness',
        longDesc: 'It is an other verity of Dhakki Dates Plant and its name is "Basra", which is known for its golden-yellow dates with rich sweetness. All plants are produced under controlled laboratory conditions ensuring 100% authenticity of variety. They are smaller than offshoots but grow faster and produce consistent yields. Recommended for commercial farmers and serious plantation projects. Minimum order: 10 plants.',
        price: 3200,
        unit: 'per plant',
        rating: 4.8,
        reviews: 34,
        img: '/static/images/Tosha_Basra.jpeg',
    },
    {
        id: 5,
        category: 'plant',
        badge: 'Rare',
        badgeClass: 'organic',
        name: 'Shakri Kanjor Plant',
        shortName: 'Shakri Kanjor Plant',
        desc: 'It is an other verity of Dhakki Dates Plant and its name is "Shakri", which is known for its red dates with rich sweetness',
        longDesc: 'It is an other verity of Dhakki Dates Plant and its name is "Shakri", which is known for its red dates with rich sweetness. All plants are produced under controlled laboratory conditions ensuring 100% authenticity of variety. They are smaller than offshoots but grow faster and produce consistent yields. Recommended for commercial farmers and serious plantation projects. Minimum order: 10 plants.',
        price: 3200,
        unit: 'per plant',
        rating: 4.8,
        reviews: 34,
        img: '/static/images/Shakri.jpeg',
    },
    {
        id: 6,
        category: 'fresh',
        badge: 'Organic',
        badgeClass: 'organic',
        name: 'Fresh Dhakki Special Kanjor',
        shortName: 'Fresh Kanjor',
        desc: 'Sun-ripened fresh Kanjor dates harvested at peak sweetness. Soft, juicy, and full of natural flavour — straight from the farm.',
        longDesc: 'Our Fresh Kanjor dates are harvested at the peak of ripeness during the season. These golden-yellow are dried in sun light and turned in to redish color of special dates which have a soft, moist texture with a rich caramel-like sweetness. Free from any preservatives, artificial colours, or chemicals. Sold per kilogram in fresh condition. Best consumed within 2 weeks. Available in retail (1kg) and bulk (5kg, 10kg) packaging.',
        price: 1100,
        unit: 'per kg',
        rating: 4.8,
        reviews: 318,
        img: '/static/images/Date_C6.jpg',
    },
    {
        id: 7,
        category: 'dry',
        badge: 'Premium',
        badgeClass: '',
        name: 'Sun-Dried Chawara (Premium)',
        shortName: 'Premium Chawara',
        desc: 'Premium quality Chawara (dry dates) naturally sun-dried on the farm. Rich in nutrients, perfect for everyday use with or without milk its your choice and gifting.',
        longDesc: 'Our Premium Chawara are naturally sun-dried Kanjor dates with no added sugar or preservatives. The drying process concentrates their natural sweetness and nutrients. These are ideal for daily consumption, cooking, Ramadan, and gifting. Available in beautifully presented gift boxes and bulk export packaging. Shelf life: 6–12 months in a cool dry place.',
        price: 1100,
        unit: 'per kg',
        rating: 5.0,
        reviews: 204,
        img: '/static/images/Date_C7.jpg',
    },
    {
        id: 8,
        category: 'dry',
        badge: 'Export Quality',
        badgeClass: '',
        name: 'Chawara & Kanjor Gift Box (500g)',
        shortName: 'Chawara Gift Box',
        desc: 'Elegantly packaged Chawara & Kanjor gift box, perfect for Eid, weddings, and corporate gifting. Premium quality in a beautiful presentation.',
        longDesc: 'A luxurious gift box containing 500g of our finest Premium Chawara & Kanjor. The box is beautifully designed with traditional patterns and can be customised with a message card. Perfect for Eid gifts, wedding favours, corporate hampers, and special occasions. Custom branding and bulk gift orders also available.',
        price: 600,
        unit: 'per box',
        rating: 4.9,
        reviews: 88,
        img: '/static/images/Gift.jpg',
    },
];

// ============================================================
// CART STATE & PERSISTENCE
// ============================================================
let cart = [];

function loadCart() {
    try {
        const saved = localStorage.getItem('nursery_cart');
        if (saved) {
            cart = JSON.parse(saved);
        }
    } catch (e) {
        cart = [];
    }
}

function saveCart() {
    try {
        localStorage.setItem('nursery_cart', JSON.stringify(cart));
    } catch (e) {}
}

function getCartTotal() {
    return cart.reduce((sum, item) => sum + item.price * item.qty, 0);
}

function updateCartUI() {
    const countEl = document.getElementById('cartCount');
    if (countEl) {
        const count = cart.reduce((sum, i) => sum + i.qty, 0);
        countEl.textContent = count;
    }

    const itemsEl = document.getElementById('cartItems');
    const footerEl = document.getElementById('cartFooter');
    const totalEl = document.getElementById('cartTotal');

    if (!itemsEl) return;

    if (cart.length === 0) {
        itemsEl.innerHTML = `<div class="cart-empty"><i class="fa-solid fa-bag-shopping"></i><p>Your cart is empty</p></div>`;
        if (footerEl) footerEl.style.display = 'none';
        return;
    }

    if (footerEl) footerEl.style.display = 'block';
    if (totalEl) totalEl.textContent = 'Rs. ' + getCartTotal().toLocaleString();

    itemsEl.innerHTML = cart.map(item => `
    <div class="cart-item">
      <div class="cart-item-img"><img src="${item.img}" alt="${item.name}"/></div>
      <div class="cart-item-info">
        <div class="cart-item-name">${item.name}</div>
        <div class="cart-item-price">Rs. ${(item.price * item.qty).toLocaleString()}</div>
        <div class="cart-item-qty">
          <button class="qty-btn" onclick="changeQty(${item.id}, -1)"><i class="fa-solid fa-minus"></i></button>
          <span class="qty-num">${item.qty}</span>
          <button class="qty-btn" onclick="changeQty(${item.id}, 1)"><i class="fa-solid fa-plus"></i></button>
        </div>
      </div>
      <button class="cart-item-remove" onclick="removeFromCart(${item.id})"><i class="fa-solid fa-trash-can"></i></button>
    </div>
  `).join('');
}

function addToCart(productId, qty = 1) {
    const product = products.find(p => p.id === productId);
    if (!product) return;
    const existing = cart.find(i => i.id === productId);
    if (existing) { existing.qty += qty; }
    else { cart.push({ ...product, qty }); }
    saveCart();
    updateCartUI();
    showToast(`${product.shortName || product.name} added to cart!`);
}

function changeQty(productId, delta) {
    const item = cart.find(i => i.id === productId);
    if (!item) return;
    item.qty += delta;
    if (item.qty <= 0) removeFromCart(productId);
    else {
        saveCart();
        updateCartUI();
    }
}

function removeFromCart(productId) {
    cart = cart.filter(i => i.id !== productId);
    saveCart();
    updateCartUI();
}

function toggleCart() {
    const sidebar = document.getElementById('cartSidebar');
    const overlay = document.getElementById('cartOverlay');
    if (!sidebar || !overlay) return;
    sidebar.classList.toggle('open');
    overlay.classList.toggle('open');
    document.body.style.overflow = sidebar.classList.contains('open') ? 'hidden' : '';
}

function checkoutWhatsApp() {
    if (cart.length === 0) return;

    const csrftoken = getCookie('csrftoken');

    // Create order record in Django DB in background
    fetch('/create-order/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
            'X-Requested-With': 'XMLHttpRequest'
        },
        body: JSON.stringify({
            cart: cart,
            customer_name: 'WhatsApp Customer'
        })
    }).catch(err => console.log('Order log error:', err));

    let msg = 'Assalamu Alaikum! I want to order dates from Malik Dhakki Dates Nursery:\n\n';
    cart.forEach(item => {
        msg += `• ${item.name} x${item.qty} = Rs. ${(item.price * item.qty).toLocaleString()}\n`;
    });
    msg += `\nTotal: Rs. ${getCartTotal().toLocaleString()}\n\nPlease confirm availability.`;
    window.open('https://wa.me/923469892120?text=' + encodeURIComponent(msg), '_blank');
}

// ============================================================
// PRODUCTS RENDERING & LIVE SEARCH
// ============================================================
let currentFilter = 'all';

function renderProducts(filter = 'all', searchQuery = '') {
    currentFilter = filter;
    const grid = document.getElementById('productsGrid');
    if (!grid) return;

    if (window.INITIAL_PRODUCTS && window.INITIAL_PRODUCTS.length > 0) {
        products = window.INITIAL_PRODUCTS;
    }

    let filtered = filter === 'all' ? products : products.filter(p => p.category === filter);

    if (searchQuery.trim() !== '') {
        const q = searchQuery.toLowerCase().trim();
        filtered = filtered.filter(p => 
            p.name.toLowerCase().includes(q) || 
            (p.desc && p.desc.toLowerCase().includes(q)) ||
            (p.shortName && p.shortName.toLowerCase().includes(q))
        );
    }

    if (filtered.length === 0) {
        grid.innerHTML = `<div style="grid-column:1/-1;text-align:center;padding:40px 0;color:var(--text-light);"><i class="fa-solid fa-magnifying-glass" style="font-size:2rem;margin-bottom:12px;color:var(--gold-main);"></i><p>No products found matching your search.</p></div>`;
        return;
    }

    grid.innerHTML = filtered.map((p, i) => `
    <div class="product-card reveal delay-${i % 4}" style="transition-delay:${(i % 4) * 0.1}s">
      <div class="product-img">
        <img src="${p.img}" alt="${p.name}" loading="lazy"/>
        ${p.badge ? `<span class="product-badge ${p.badgeClass || ''}">${p.badge}</span>` : ''}
        <button class="product-wishlist" onclick="event.stopPropagation(); showToast('Added to wishlist!')">
          <i class="fa-regular fa-heart"></i>
        </button>
      </div>
      <div class="product-info" onclick="openModal(${p.id})" style="cursor:pointer;">
        <span class="product-category">${p.category === 'plant' ? 'Date Plant' : p.category === 'fresh' ? 'Fresh Dates' : 'Dry Dates'}</span>
        <h3 class="product-name">${p.name}</h3>
        <p class="product-desc">${p.desc ? p.desc.substring(0, 90) : ''}…</p>
        <div class="product-rating">
          <div class="stars">${'<i class="fa-solid fa-star"></i>'.repeat(Math.floor(p.rating || 5))}${(p.rating || 5) % 1 >= 0.5 ? '<i class="fa-solid fa-star-half-stroke"></i>' : ''}</div>
          <span class="rating-count">${p.rating || 5} (${p.reviews || 0})</span>
        </div>
      </div>
      <div class="product-footer" style="padding:0 22px 22px;">
        <div class="product-price">
          <span class="price-main">Rs. ${parseFloat(p.price).toLocaleString()}</span>
          <span class="price-unit">${p.unit}</span>
        </div>
        <button class="add-cart-btn" onclick="addToCart(${p.id})">
          <i class="fa-solid fa-plus"></i> Add
        </button>
      </div>
    </div>
  `).join('');

    setTimeout(() => {
        grid.querySelectorAll('.reveal').forEach(el => {
            if (typeof observer !== 'undefined') observer.observe(el);
            el.classList.add('active');
        });
    }, 50);
}

function handleLiveSearch(query) {
    renderProducts(currentFilter, query);
}

function filterProducts(filter, btn) {
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    if (btn) btn.classList.add('active');
    const searchInput = document.getElementById('productSearchInput');
    const query = searchInput ? searchInput.value : '';
    renderProducts(filter, query);
}

// ============================================================
// MODAL
// ============================================================
let modalQty = 1;
let modalProduct = null;

function openModal(productId) {
    modalProduct = products.find(p => p.id === productId);
    modalQty = 1;
    if (!modalProduct) return;

    const modalImg = document.getElementById('modalImg');
    const modalInfo = document.getElementById('modalInfo');
    if (!modalImg || !modalInfo) return;

    modalImg.innerHTML = `<img src="${modalProduct.img}" alt="${modalProduct.name}"/>`;
    modalInfo.innerHTML = `
    <button class="modal-close" onclick="closeModal()"><i class="fa-solid fa-xmark"></i></button>
    <div class="modal-cat">${modalProduct.category === 'plant' ? 'Date Plant' : modalProduct.category === 'fresh' ? 'Fresh Dates' : 'Dry Dates'}</div>
    <h2 class="modal-name">${modalProduct.name}</h2>
    <div class="modal-rating">
      <div class="stars">${'<i class="fa-solid fa-star"></i>'.repeat(Math.floor(modalProduct.rating || 5))}${(modalProduct.rating || 5) % 1 >= 0.5 ? '<i class="fa-solid fa-star-half-stroke"></i>' : ''}</div>
      <span style="font-size:0.85rem;color:var(--text-light);margin-left:6px;">${modalProduct.rating || 5} (${modalProduct.reviews || 0} reviews)</span>
    </div>
    <div class="modal-price">Rs. ${parseFloat(modalProduct.price).toLocaleString()} <span style="font-size:1rem;color:var(--text-light);font-family:'Outfit',sans-serif;font-weight:400;">${modalProduct.unit}</span></div>
    <p class="modal-desc">${modalProduct.longDesc || modalProduct.desc}</p>
    <div class="modal-qty-section">
      <span class="modal-qty-label">Quantity:</span>
      <div class="modal-qty-ctrl">
        <button class="qty-btn" onclick="changeModalQty(-1)"><i class="fa-solid fa-minus"></i></button>
        <span class="modal-qty-num qty-num" id="modalQtyDisplay">1</span>
        <button class="qty-btn" onclick="changeModalQty(1)"><i class="fa-solid fa-plus"></i></button>
      </div>
    </div>
    <div class="modal-actions">
      <button class="btn-primary modal-add-cart" onclick="addToCart(${modalProduct.id}, modalQty); closeModal()">
        <i class="fa-solid fa-bag-shopping"></i> Add to Cart
      </button>
      <a href="https://wa.me/923469892120?text=${encodeURIComponent('Assalamu Alaikum! I want to order: ' + modalProduct.name + ' x1. Please confirm price and availability.')}" target="_blank" class="btn-whatsapp modal-wa-btn">
        <i class="fa-brands fa-whatsapp"></i> Order via WhatsApp
      </a>
    </div>
  `;

    const productModal = document.getElementById('productModal');
    if (productModal) {
        productModal.classList.add('open');
        document.body.style.overflow = 'hidden';
    }
}

function changeModalQty(delta) {
    modalQty = Math.max(1, modalQty + delta);
    const el = document.getElementById('modalQtyDisplay');
    if (el) el.textContent = modalQty;
}

function closeModal(event) {
    if (event && event.target !== document.getElementById('productModal')) return;
    const modal = document.getElementById('productModal');
    if (modal) modal.classList.remove('open');
    document.body.style.overflow = '';
}

// ============================================================
// NAVBAR SCROLL & MOBILE NAV
// ============================================================
window.addEventListener('scroll', () => {
    const navbar = document.getElementById('navbar');
    if (navbar) {
        if (window.scrollY > 60) navbar.classList.add('scrolled');
        else navbar.classList.remove('scrolled');
    }
});

function toggleMobileNav() {
    const nav = document.getElementById('mobileNav');
    const overlay = document.getElementById('mobileNavOverlay');
    if (!nav || !overlay) return;
    nav.classList.toggle('open');
    overlay.classList.toggle('open');
    document.body.style.overflow = nav.classList.contains('open') ? 'hidden' : '';
}

// ============================================================
// SCROLL REVEAL & TOAST
// ============================================================
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('active');
        }
    });
}, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

function initReveal() {
    document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale').forEach(el => {
        observer.observe(el);
    });
}

let toastTimer;
function showToast(msg) {
    const toast = document.getElementById('toast');
    const toastMsg = document.getElementById('toastMsg');
    if (!toast || !toastMsg) return;
    clearTimeout(toastTimer);
    toastMsg.textContent = msg;
    toast.classList.add('show');
    toastTimer = setTimeout(() => toast.classList.remove('show'), 3000);
}

// ============================================================
// FORM SUBMIT / NEWSLETTER AJAX
// ============================================================
function handleFormSubmit(event) {
    return true;
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function subscribeNewsletter() {
    const emailInput = document.getElementById('nlEmail');
    if (!emailInput) return;
    const email = emailInput.value.trim();
    if (!email || !email.includes('@')) {
        showToast('Please enter a valid email.');
        return;
    }

    const csrftoken = getCookie('csrftoken');
    const formData = new FormData();
    formData.append('email', email);

    fetch('/subscribe/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
            'X-Requested-With': 'XMLHttpRequest'
        },
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        if (data.status === 'success') {
            showToast(data.message);
            emailInput.value = '';
        } else {
            showToast(data.message || 'Subscription failed.');
        }
    })
    .catch(() => {
        showToast('Subscribed successfully! Thank you.');
        emailInput.value = '';
    });
}

// ============================================================
// INIT
// ============================================================
document.addEventListener('DOMContentLoaded', () => {
    loadCart();
    updateCartUI();
    renderProducts();
    initReveal();
});
