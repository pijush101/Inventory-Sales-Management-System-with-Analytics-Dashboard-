# GreenLeaf Grocers — Inventory & Sales Management System

A Flask + SQLite inventory and sales application with role-based access, billing, automatic stock deduction, CSV import/export, Pandas analytics, charts, PDF bills, and automated tests.

## Features

- Admin and cashier login
- Product CRUD and search
- Multi-item billing
- Automatic inventory deduction
- Stock validation
- Low-stock alerts
- Near-expiry alerts
- CSV product import/export
- Daily/monthly sales analysis
- Top-selling products
- Category sales share
- Slow-moving product analysis
- PDF bill generation
- Date-range reports
- 18+ pytest tests
- Separate SQLite test database

## Demo accounts

Admin:
- Username: `admin`
- Password: `Admin@123`

Cashier:
- Username: `cashier`
- Password: `Cashier@123`

Change these credentials before production deployment.

## Setup

Python 3.11+ is recommended.

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Install packages:

```bash
pip install -r requirements.txt
```

Generate the database and test data:

```bash
python seed_data.py
```

Run:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Run tests

```bash
pytest -q
```

The tests use a temporary SQLite database and do not modify the development database.

## Database

Main tables:

- users
- products
- suppliers
- sales
- sale_items

The schema follows the project specification. Sales and sale items are separated so one bill can contain multiple products.

## Analytics

Pandas is used for:

- Daily revenue
- Monthly revenue
- Top products
- Category sales share
- Slow-moving products

SQLAlchemy is used for transactional database operations.

## Validation

The application rejects:

- Negative quantities
- Zero quantities
- Invalid dates
- Missing products
- Non-existent products
- Sales above available stock
- Negative discounts
- Discounts above subtotal
- Invalid CSV product data

## Notes

This is an academic/portfolio project. For production deployment, use a production WSGI server, a strong secret key, HTTPS, CSRF protection, database migrations, and a production database.
