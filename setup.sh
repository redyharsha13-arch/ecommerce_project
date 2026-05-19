#!/usr/bin/env bash
set -e

echo "============================================"
echo "  ShopEase E-Commerce Setup"
echo "============================================"

# Create virtual environment
if [ ! -d "venv" ]; then
  echo "[1/5] Creating virtual environment..."
  python3 -m venv venv
fi

# Activate
source venv/bin/activate

# Install dependencies
echo "[2/5] Installing dependencies..."
pip install -q -r requirements.txt

# Migrations
echo "[3/5] Running migrations..."
python manage.py migrate

# Seed data
echo "[4/5] Seeding sample products..."
python manage.py seed_data

# Collect static (optional)
# python manage.py collectstatic --noinput

echo ""
echo "============================================"
echo "  ✅  Setup Complete!"
echo "============================================"
echo ""
echo "  🚀  Run the server:"
echo "      source venv/bin/activate"
echo "      python manage.py runserver"
echo ""
echo "  🌐  Open: http://127.0.0.1:8000"
echo ""
echo "  👤  Admin:  http://127.0.0.1:8000/admin"
echo "      Login:  admin / admin123"
echo ""
echo "  👤  Demo user: demo / demo1234"
echo "============================================"

# Auto-start server
echo "[5/5] Starting development server..."
python manage.py runserver
