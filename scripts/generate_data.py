"""
RetailPulse — Dataset Generation Script
Generates the required CSV files with realistic retail e-commerce data.
"""

import csv
import os
import random
from datetime import date, timedelta

# ─── Seed for reproducibility ──────────────────────────────────────
random.seed(42)

# ─── Output directory ──────────────────────────────────────────────
OUTPUT_DIR = r"c:\Users\Admin\Desktop\New folder (2)\dataset"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ─── Helper ────────────────────────────────────────────────────────
def random_date(start: date, end: date) -> date:
    delta = (end - start).days
    return start + timedelta(days=random.randint(0, delta))

def write_csv(filename, headers, rows):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
    print(f"  ✓ {filename}: {len(rows)} rows")

# ═══════════════════════════════════════════════════════════════════
# 1. CUSTOMERS  (~200)
# ═══════════════════════════════════════════════════════════════════
first_names = [
    "Aarav", "Aditi", "Aisha", "Amit", "Ananya", "Anika", "Arjun", "Bhavna",
    "Chirag", "Deepa", "Devika", "Dhruv", "Divya", "Farhan", "Gauri", "Harsh",
    "Isha", "Jatin", "Kavya", "Kiran", "Lakshmi", "Manish", "Meera", "Mohit",
    "Nandini", "Naveen", "Neha", "Nikhil", "Pallavi", "Pooja", "Priya", "Rahul",
    "Rajesh", "Ravi", "Rekha", "Ritika", "Rohan", "Sakshi", "Sandeep", "Sanjay",
    "Sapna", "Shivani", "Shruti", "Simran", "Sneha", "Sonia", "Sunil", "Tanvi",
    "Uday", "Varun", "Vidya", "Vikram", "Vinay", "Vivek", "Yash", "Zara",
    "Akhil", "Bharat", "Chitra", "Darshan", "Esha", "Gaurav", "Hemant", "Indira",
    "Jayesh", "Komal", "Lata", "Madhav", "Nisha", "Omkar"
]

last_names = [
    "Agarwal", "Bansal", "Bhatt", "Chandra", "Chauhan", "Chopra", "Das", "Desai",
    "Ghosh", "Gupta", "Iyer", "Jain", "Joshi", "Kapoor", "Khan", "Kumar",
    "Malhotra", "Mehta", "Menon", "Mishra", "Nair", "Pandey", "Patel", "Pillai",
    "Raj", "Rajan", "Rao", "Reddy", "Saxena", "Sen", "Shah", "Sharma",
    "Shukla", "Singh", "Sinha", "Srivastava", "Tiwari", "Verma", "Yadav", "Thakur"
]

cities_states = [
    ("Mumbai", "Maharashtra"), ("Delhi", "Delhi"), ("Bangalore", "Karnataka"),
    ("Hyderabad", "Telangana"), ("Chennai", "Tamil Nadu"), ("Kolkata", "West Bengal"),
    ("Pune", "Maharashtra"), ("Ahmedabad", "Gujarat"), ("Jaipur", "Rajasthan"),
    ("Lucknow", "Uttar Pradesh"), ("Chandigarh", "Punjab"), ("Bhopal", "Madhya Pradesh"),
    ("Patna", "Bihar"), ("Kochi", "Kerala"), ("Indore", "Madhya Pradesh"),
    ("Nagpur", "Maharashtra"), ("Coimbatore", "Tamil Nadu"), ("Surat", "Gujarat"),
    ("Visakhapatnam", "Andhra Pradesh"), ("Thiruvananthapuram", "Kerala")
]

NUM_CUSTOMERS = 200
customers = []
used_emails = set()

for cid in range(1, NUM_CUSTOMERS + 1):
    fn = random.choice(first_names)
    ln = random.choice(last_names)
    # Unique email
    email_base = f"{fn.lower()}.{ln.lower()}"
    email = f"{email_base}@email.com"
    suffix = 1
    while email in used_emails:
        email = f"{email_base}{suffix}@email.com"
        suffix += 1
    used_emails.add(email)
    phone = f"+91-{random.randint(70000, 99999)}{random.randint(10000, 99999)}"
    city, state = random.choice(cities_states)
    reg_date = random_date(date(2023, 1, 1), date(2025, 6, 30))
    customers.append([cid, fn, ln, email, phone, city, state, reg_date.isoformat()])

write_csv("customers.csv",
    ["customer_id", "first_name", "last_name", "email", "phone", "city", "state", "registration_date"],
    customers)

# ═══════════════════════════════════════════════════════════════════
# 2. PRODUCTS  (~50)
# ═══════════════════════════════════════════════════════════════════
product_catalog = {
    "Electronics": [
        ("Wireless Earbuds", 1499), ("Bluetooth Speaker", 2499), ("Smartphone Case", 399),
        ("USB-C Hub", 1899), ("Webcam HD", 2999), ("Portable Charger", 999),
        ("Keyboard Mechanical", 3499), ("Mouse Wireless", 899), ("LED Desk Lamp", 1299),
        ("Smartwatch Band", 599),
    ],
    "Clothing": [
        ("Cotton T-Shirt", 499), ("Denim Jeans", 1299), ("Hoodie Pullover", 1599),
        ("Formal Shirt", 999), ("Track Pants", 799), ("Sneakers", 2499),
        ("Sunglasses", 699), ("Leather Belt", 449), ("Winter Jacket", 2999),
        ("Cap Baseball", 299),
    ],
    "Home": [
        ("Bedsheet Set", 899), ("Cushion Cover Pack", 599), ("Wall Clock", 749),
        ("Photo Frame Set", 499), ("Scented Candle", 349), ("Storage Box", 649),
        ("Throw Blanket", 1199), ("Table Runner", 449), ("Flower Vase", 799),
        ("Door Mat", 249),
    ],
    "Sports": [
        ("Yoga Mat", 699), ("Resistance Bands", 499), ("Water Bottle Steel", 599),
        ("Jump Rope", 299), ("Dumbbells 5kg Pair", 1499), ("Sports Towel", 249),
        ("Running Armband", 399), ("Gym Gloves", 349), ("Fitness Tracker", 1999),
        ("Skipping Rope Pro", 449),
    ],
    "Books": [
        ("Python Programming", 549), ("Data Science Handbook", 699), ("SQL Mastery", 499),
        ("Business Analytics", 599), ("Machine Learning Intro", 749), ("Excel Advanced", 399),
        ("Statistics Basics", 449), ("Web Development", 649), ("Project Management", 549),
        ("Digital Marketing", 499),
    ],
}

products = []
pid = 1
for category, items in product_catalog.items():
    for name, price in items:
        stock = random.randint(20, 500)
        products.append([pid, name, category, price, stock])
        pid += 1

write_csv("products.csv",
    ["product_id", "product_name", "category", "price", "stock_quantity"],
    products)

NUM_PRODUCTS = len(products)

# ═══════════════════════════════════════════════════════════════════
# 3. EMPLOYEES  (~15)
# ═══════════════════════════════════════════════════════════════════
employee_data = [
    ("Arjun", "Sharma", "Manager"),
    ("Priya", "Patel", "Senior Sales Rep"),
    ("Rahul", "Gupta", "Senior Sales Rep"),
    ("Sneha", "Reddy", "Sales Rep"),
    ("Vikram", "Singh", "Sales Rep"),
    ("Ananya", "Das", "Sales Rep"),
    ("Mohit", "Jain", "Sales Rep"),
    ("Kavya", "Nair", "Sales Rep"),
    ("Deepa", "Mehta", "Sales Rep"),
    ("Rohan", "Kapoor", "Sales Rep"),
    ("Simran", "Kaur", "Sales Rep"),
    ("Harsh", "Tiwari", "Sales Rep"),
    ("Neha", "Bansal", "Sales Rep"),
    ("Varun", "Mishra", "Sales Rep"),
    ("Divya", "Rao", "Sales Rep"),
]

employees = []
for eid, (fn, ln, role) in enumerate(employee_data, start=1):
    hire_date = random_date(date(2020, 1, 1), date(2024, 12, 31))
    employees.append([eid, fn, ln, role, hire_date.isoformat()])

write_csv("employees.csv",
    ["employee_id", "first_name", "last_name", "role", "hire_date"],
    employees)

# ═══════════════════════════════════════════════════════════════════
# 4. ORDERS  (~1000)
# ═══════════════════════════════════════════════════════════════════
NUM_ORDERS = 1000
ORDER_START = date(2025, 1, 1)
ORDER_END = date(2025, 12, 31)

# Deliberate pattern: ~30 customers will have ZERO orders
active_customer_ids = [c[0] for c in customers]
zero_order_customers = set(random.sample(active_customer_ids, 30))
orderable_customers = [cid for cid in active_customer_ids if cid not in zero_order_customers]

# Some customers order more frequently (repeat buyers)
repeat_buyers = random.sample(orderable_customers, 40)

statuses = ["Completed", "Completed", "Completed", "Completed",
            "Completed", "Completed", "Completed",
            "Cancelled", "Returned"]  # ~78% completed, ~11% cancelled, ~11% returned

orders = []
for oid in range(1, NUM_ORDERS + 1):
    # Weighted: repeat buyers get picked more often
    if random.random() < 0.35:
        cust_id = random.choice(repeat_buyers)
    else:
        cust_id = random.choice(orderable_customers)

    emp_id = random.randint(1, len(employees))

    # Seasonal spike: more orders in Oct-Dec
    if random.random() < 0.3:
        order_date = random_date(date(2025, 10, 1), date(2025, 12, 31))
    else:
        order_date = random_date(ORDER_START, ORDER_END)

    status = random.choice(statuses)
    orders.append([oid, cust_id, emp_id, order_date.isoformat(), status])

write_csv("orders.csv",
    ["order_id", "customer_id", "employee_id", "order_date", "status"],
    orders)

# ═══════════════════════════════════════════════════════════════════
# 5. ORDER_ITEMS  (~2500)
# ═══════════════════════════════════════════════════════════════════
# Deliberate: ~5 products will NEVER appear in any order
never_purchased = set(random.sample(range(1, NUM_PRODUCTS + 1), 5))
purchasable_products = [p[0] for p in products if p[0] not in never_purchased]
product_prices = {p[0]: p[3] for p in products}

order_items = []
item_id = 1
for order in orders:
    oid = order[0]
    num_items = random.choices([1, 2, 3, 4, 5], weights=[30, 35, 20, 10, 5])[0]
    chosen_products = random.sample(purchasable_products, min(num_items, len(purchasable_products)))
    for prod_id in chosen_products:
        qty = random.choices([1, 2, 3, 4], weights=[50, 30, 15, 5])[0]
        unit_price = product_prices[prod_id]
        total_price = qty * unit_price
        order_items.append([item_id, oid, prod_id, qty, unit_price, total_price])
        item_id += 1

write_csv("order_items.csv",
    ["item_id", "order_id", "product_id", "quantity", "unit_price", "total_price"],
    order_items)

# ═══════════════════════════════════════════════════════════════════
# 6. PAYMENTS  (~1000, one per order)
# ═══════════════════════════════════════════════════════════════════
payment_methods = ["UPI", "Credit Card", "Debit Card", "Net Banking", "COD"]
payment_weights = [35, 25, 20, 10, 10]

# Build order totals from order_items
order_totals = {}
for item in order_items:
    oid = item[1]
    order_totals[oid] = order_totals.get(oid, 0) + item[5]

payments = []
for pay_id, order in enumerate(orders, start=1):
    oid = order[0]
    order_date = date.fromisoformat(order[3])
    # Payment date = order date or up to 2 days later
    pay_date = order_date + timedelta(days=random.randint(0, 2))
    amount = order_totals.get(oid, 0)
    method = random.choices(payment_methods, weights=payment_weights)[0]
    payments.append([pay_id, oid, pay_date.isoformat(), amount, method])

write_csv("payments.csv",
    ["payment_id", "order_id", "payment_date", "amount", "payment_method"],
    payments)

print(f"\n✅ All 6 CSV files generated in: {OUTPUT_DIR}")
print(f"   Customers with zero orders: {len(zero_order_customers)}")
print(f"   Products never purchased: {len(never_purchased)} — IDs: {sorted(never_purchased)}")
print(f"   Repeat buyers pool: {len(repeat_buyers)}")
