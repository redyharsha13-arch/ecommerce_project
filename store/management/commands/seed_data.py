from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from store.models import Category, Product, UserProfile
from decimal import Decimal


class Command(BaseCommand):
    help = 'Seed database with sample data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding database...')

        # Categories
        cats = [
            ('Electronics', 'electronics'),
            ('Clothing', 'clothing'),
            ('Books', 'books'),
            ('Home & Kitchen', 'home-kitchen'),
            ('Sports', 'sports'),
            ('Beauty', 'beauty'),
        ]
        cat_objs = {}
        for name, slug in cats:
            cat, _ = Category.objects.get_or_create(name=name, slug=slug)
            cat_objs[slug] = cat

        # Products
        products = [
            # Electronics
            ('Wireless Bluetooth Headphones', 'wireless-bluetooth-headphones', 'electronics',
             '2499', '3999', 50,
             'Premium noise-cancelling wireless headphones with 30-hour battery life. Crystal clear sound with deep bass. Perfect for music lovers and remote workers alike.'),
            ('Smart Watch Pro', 'smart-watch-pro', 'electronics',
             '8999', '12999', 25,
             'Feature-packed smartwatch with heart rate monitoring, GPS, sleep tracking, and 7-day battery life. Compatible with iOS and Android.'),
            ('Mechanical Keyboard', 'mechanical-keyboard', 'electronics',
             '3499', None, 40,
             'Compact TKL mechanical keyboard with RGB backlight. Blue switches for satisfying tactile feedback. Perfect for programmers and gamers.'),
            ('USB-C Hub 7-in-1', 'usb-c-hub', 'electronics',
             '1799', '2499', 60,
             'Expand your laptop connectivity with HDMI 4K, 3× USB-A, SD card, microSD, and 100W PD charging in one sleek hub.'),

            # Clothing
            ('Classic Cotton T-Shirt', 'classic-cotton-tshirt', 'clothing',
             '599', '899', 200,
             '100% premium cotton unisex t-shirt. Pre-shrunk fabric, reinforced stitching, available in 12 colours. Soft, breathable, and durable for everyday wear.'),
            ('Slim Fit Chinos', 'slim-fit-chinos', 'clothing',
             '1299', '1999', 80,
             'Modern slim-fit chinos crafted from stretch cotton blend. Versatile enough for office or casual outings. Multiple colour options available.'),
            ('Running Jacket', 'running-jacket', 'clothing',
             '2199', '2999', 35,
             'Lightweight, water-resistant running jacket with reflective strips and zip pockets. Packable design for easy storage on the go.'),

            # Books
            ('Python for Data Science', 'python-data-science', 'books',
             '699', '999', 100,
             'A comprehensive guide to Python programming for data analysis, visualization, and machine learning. Includes real-world projects and exercises.'),
            ('The Pragmatic Programmer', 'pragmatic-programmer', 'books',
             '799', None, 75,
             'A classic software engineering book covering best practices, design principles, and career advice for developers. Essential reading for every programmer.'),
            ('Atomic Habits', 'atomic-habits', 'books',
             '499', '699', 120,
             'James Clear\'s bestselling guide to building good habits and breaking bad ones. Packed with actionable strategies based on behavioural science.'),

            # Home & Kitchen
            ('Stainless Steel Water Bottle', 'steel-water-bottle', 'home-kitchen',
             '799', '1199', 150,
             'Double-wall vacuum insulated 750ml bottle keeps drinks cold 24hr or hot 12hr. BPA-free, leak-proof lid, fits most cup holders.'),
            ('Air Fryer 4L', 'air-fryer-4l', 'home-kitchen',
             '4499', '6999', 20,
             'Rapid air technology cooks crispy food with up to 80% less oil. 4-litre capacity, 8 preset programs, non-stick basket, auto shut-off.'),

            # Sports
            ('Yoga Mat Premium', 'yoga-mat-premium', 'sports',
             '1299', '1799', 90,
             'Extra-thick 6mm non-slip yoga mat with alignment lines. Eco-friendly TPE material, moisture-resistant, includes carry strap.'),
            ('Resistance Bands Set', 'resistance-bands-set', 'sports',
             '699', '999', 110,
             'Set of 5 resistance bands (15–45 lbs). Suitable for strength training, stretching, and rehabilitation. Includes carry bag and exercise guide.'),

            # Beauty
            ('Vitamin C Serum', 'vitamin-c-serum', 'beauty',
             '899', '1499', 70,
             '20% Vitamin C + Hyaluronic Acid facial serum. Brightens skin, reduces dark spots, boosts collagen. Dermatologist tested, suitable for all skin types.'),
            ('Hydrating Face Cream', 'hydrating-face-cream', 'beauty',
             '649', '899', 85,
             '24-hour hydrating moisturiser with ceramides and niacinamide. Non-greasy formula that strengthens the skin barrier. For all skin types.'),
        ]

        for name, slug, cat_slug, price, orig_price, stock, desc in products:
            Product.objects.get_or_create(
                slug=slug,
                defaults={
                    'name': name,
                    'category': cat_objs[cat_slug],
                    'price': Decimal(price),
                    'original_price': Decimal(orig_price) if orig_price else None,
                    'stock': stock,
                    'description': desc,
                    'is_available': True,
                }
            )

        # Admin user
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@shopease.com', 'admin123')
            self.stdout.write('  Created superuser: admin / admin123')

        # Demo user
        if not User.objects.filter(username='demo').exists():
            u = User.objects.create_user('demo', 'demo@shopease.com', 'demo1234')
            UserProfile.objects.create(user=u, phone='9876543210', city='Hyderabad', state='Telangana', zip_code='500001')
            self.stdout.write('  Created demo user: demo / demo1234')

        self.stdout.write(self.style.SUCCESS(f'Done! {Product.objects.count()} products, {Category.objects.count()} categories.'))
