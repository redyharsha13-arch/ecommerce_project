# 🛍️ ShopEase — Full-Stack E-Commerce Store

A complete, production-ready e-commerce web application built with **Django** (Python) + **Vanilla JS/CSS**.

---

## ✨ Features

| Feature | Details |
|---|---|
| 🛒 **Shopping Cart** | Session-based cart, add/update/remove items, live item count badge |
| 📦 **Product Listings** | Grid layout with search, filter by category, sort, price range |
| 📄 **Product Detail** | Full page with gallery, ratings, reviews, related products |
| ✅ **Order Processing** | Checkout form, order confirmation, order history & detail pages |
| 👤 **User Auth** | Register, login, logout, profile management |
| 💾 **Database** | SQLite (dev) — easily swappable to PostgreSQL for production |
| 🔐 **Admin Panel** | Full Django admin for managing products, orders, users |
| ⭐ **Reviews** | Authenticated users can leave star ratings and comments |
| 📱 **Responsive** | Mobile-friendly layout |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9+

### Option 1: One-command setup
```bash
cd ecommerce
chmod +x setup.sh
./setup.sh
```

### Option 2: Manual setup
```bash
cd ecommerce

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate       # Linux/Mac
# venv\Scripts\activate        # Windows

# Install dependencies
pip install -r requirements.txt

# Database migrations
python manage.py migrate

# Seed sample data (16 products, 6 categories, admin + demo users)
python manage.py seed_data

# Run the server
python manage.py runserver
```

Open **http://127.0.0.1:8000** in your browser.

---
## Troubleshooting

If CSS/styling does not load correctly in Chrome due to cached static files:

- Hard refresh: `Ctrl + Shift + R`
- Or clear browser cache / site data
- If needed, try opening once in Incognito mode

## 👤 Default Accounts

| Role | Username | Password | URL |
|---|---|---|---|
| Admin | `admin` | `admin123` | `/admin/` |
| Demo User | `demo` | `demo1234` | `/login/` |

---

## 🗂️ Project Structure

```
ecommerce/
├── ecommerce/               # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── store/                   # Main app
│   ├── models.py            # Product, Category, Order, Review, UserProfile
│   ├── views.py             # All views (home, products, cart, checkout, auth)
│   ├── urls.py              # URL routing
│   ├── forms.py             # Register, Login, Checkout, Review, Profile
│   ├── admin.py             # Django admin configuration
│   ├── context_processors.py
│   └── management/
│       └── commands/
│           └── seed_data.py  # Sample data seeder
├── templates/
│   └── store/
│       ├── base.html         # Layout with navbar, footer, messages
│       ├── home.html         # Homepage with hero, categories, featured
│       ├── product_list.html # Products grid with filters & sorting
│       ├── product_detail.html
│       ├── cart.html
│       ├── checkout.html
│       ├── order_success.html
│       ├── order_list.html
│       ├── order_detail.html
│       ├── register.html
│       ├── login.html
│       ├── profile.html
│       └── partials/
│           └── product_card.html
├── static/
│   ├── css/style.css        # ~600 lines of custom CSS
│   └── js/main.js
├── media/                   # Uploaded product images
├── requirements.txt
├── setup.sh
└── manage.py
```

---

## 🗄️ Database Models

- **Category** — Product categories with slugs
- **Product** — Name, description, price, original_price, stock, image, category
- **Review** — Star rating + comment, one per user per product
- **Order** — Shipping details, status (pending/processing/shipped/delivered/cancelled)
- **OrderItem** — Product, quantity, price snapshot at time of order
- **UserProfile** — Extended user info (phone, address)

---

## 🔧 Switching to PostgreSQL

In `settings.py`, replace the DATABASES block:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'shopease_db',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Then: `pip install psycopg2-binary`

---

## 📸 Adding Product Images

1. Go to `/admin/` → Products → Add/Edit a product
2. Upload an image in the Image field
3. Images are stored in `media/products/`

---

## 🌐 Pages Reference

| URL | Description |
|---|---|
| `/` | Homepage |
| `/products/` | Product listing with filters |
| `/products/<slug>/` | Product detail |
| `/cart/` | Shopping cart |
| `/checkout/` | Checkout form |
| `/orders/` | Order history |
| `/orders/<id>/` | Order detail |
| `/register/` | User registration |
| `/login/` | Login |
| `/profile/` | User profile |
| `/admin/` | Django admin |
