from datetime import date, timedelta
from random import Random
from werkzeug.security import generate_password_hash
from app import create_app
from database.db import db
from models.models import User, Supplier, Product, Sale, SaleItem

rng = Random(42)

CATEGORIES = {
    "Fruits": ["Apple", "Banana", "Orange", "Mango", "Papaya", "Grapes", "Guava", "Pomegranate"],
    "Vegetables": ["Potato", "Tomato", "Onion", "Carrot", "Cabbage", "Spinach", "Cauliflower", "Beans"],
    "Dairy": ["Milk", "Curd", "Paneer", "Butter", "Cheese", "Cream"],
    "Beverages": ["Tea", "Coffee", "Juice", "Cola", "Lemon Drink", "Mineral Water"],
    "Snacks": ["Biscuits", "Chips", "Namkeen", "Cookies", "Chocolate", "Popcorn"],
    "Staples": ["Rice", "Wheat Flour", "Lentils", "Sugar", "Salt", "Cooking Oil", "Oats"],
}

def seed(app=None):
    app = app or create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()

        admin = User(username="admin", password_hash=generate_password_hash("Admin@123"), role="admin")
        cashier = User(username="cashier", password_hash=generate_password_hash("Cashier@123"), role="cashier")
        db.session.add_all([admin, cashier])

        suppliers = []
        for i in range(1, 9):
            supplier = Supplier(
                name=f"GreenLeaf Supplier {i}",
                phone=f"90000000{i:02d}",
                email=f"supplier{i}@greenleaf.local"
            )
            suppliers.append(supplier)
            db.session.add(supplier)
        db.session.flush()

        products = []
        product_id_counter = 1
        for category, names in CATEGORIES.items():
            for base in names:
                for variant in range(1, 3):
                    price = round(rng.uniform(20, 500), 2)
                    expiry = date.today() + timedelta(days=rng.randint(7, 365))
                    p = Product(
                        name=f"{base} {variant}",
                        category=category,
                        unit_price=price,
                        stock_qty=rng.randint(20, 150),
                        reorder_level=rng.randint(5, 20),
                        expiry_date=expiry,
                        supplier_id=rng.choice(suppliers).supplier_id
                    )
                    products.append(p)
                    db.session.add(p)
                    product_id_counter += 1

        db.session.flush()

        for sale_no in range(1, 501):
            sale_date = date.today() - timedelta(days=rng.randint(0, 179))
            sale = Sale(
                sale_date=sale_date,
                sale_time=__import__("datetime").time(rng.randint(8, 20), rng.randint(0, 59)),
                user_id=admin.user_id if sale_no % 5 == 0 else cashier.user_id,
            )
            db.session.add(sale)
            db.session.flush()

            chosen = rng.sample(products, rng.randint(1, 5))
            subtotal = 0
            for p in chosen:
                qty = rng.randint(1, 5)
                item = SaleItem(sale_id=sale.sale_id, product_id=p.product_id, quantity=qty, price=p.unit_price)
                db.session.add(item)
                subtotal += p.unit_price * qty

            discount = round(subtotal * rng.uniform(0, 0.10), 2)
            sale.subtotal = round(subtotal, 2)
            sale.discount = discount
            sale.total_amount = round(subtotal - discount, 2)

        db.session.commit()
        print(f"Seeded {len(products)} products and 500 sales.")
        print("Admin: admin / Admin@123")
        print("Cashier: cashier / Cashier@123")

if __name__ == "__main__":
    seed()
