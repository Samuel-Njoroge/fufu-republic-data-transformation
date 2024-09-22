import csv
from faker import Faker
from random import choice, randint, uniform, choices
from datetime import datetime, timedelta

# Initialize Faker with US locale
fake = Faker('en_US')

# Set random seed for reproducibility
Faker.seed(12345)

# Nigerian-specific data
nigerian_first_names = ['Adebayo', 'Chinyere', 'Oluwaseun', 'Ngozi', 'Emeka', 'Oluwadamilola', 'Chinwe', 'Ikechukwu', 'Oluwadamilare', 'Adaobi']
nigerian_last_names = ['Okafor', 'Adeyemi', 'Okonkwo', 'Eze', 'Nnamani', 'Okorie', 'Afolabi', 'Nwosu', 'Ogbu', 'Okeke']
nigerian_cities = ['Lagos', 'Abuja', 'Port Harcourt', 'Kano', 'Ibadan', 'Kaduna', 'Enugu', 'Benin City', 'Owerri', 'Calabar']

# Helper functions
def generate_customer_id():
    return fake.uuid4()[:8]

def generate_email(first_name, last_name):
    return f"{first_name.lower()}.{last_name.lower()}@{fake.free_email_domain()}"

def generate_branch_id():
    return choice(['1', '2', '3', '4'])

def generate_payment_method_id():
    return fake.uuid4()[:20]

def generate_order_id():
    return fake.uuid4()[:20]

def generate_menu_item_id():
    return fake.uuid4()[:32]

def generate_order_item_id():
    return fake.uuid4()[:32]

def generate_inventory_id():
    return fake.uuid4()[:20]

# Generate data for each table
def generate_customers(num_rows):
    customers = []
    customer_ids = [generate_customer_id() for _ in range(32)]  # Generate 32 unique customer IDs
    for _ in range(num_rows):
        first_name = choice(nigerian_first_names)
        last_name = choice(nigerian_last_names)
        customer = {
            'customer_id': choice(customer_ids),
            'first_name': first_name,
            'last_name': last_name,
            'email_address': generate_email(first_name, last_name),
            'phone_number': f"+234{fake.msisdn()[4:]}"  # Nigerian phone number format
        }
        customers.append(customer)
    return customers

def generate_branches(num_rows):
    branches = []
    for _ in range(num_rows):
        branch = {
            'branch_id': generate_branch_id(),
            'name': f"{choice(nigerian_last_names)} Restaurant",
            'location': choice(['Ikeja', 'Agege', 'Lekki', 'Lagos']),
            'type': choice(['Larger', 'Small'])
        }
        branches.append(branch)
    return branches

def generate_payment_methods(num_rows):
    payment_methods = []
    for _ in range(num_rows):
        payment_method = {
            'payment_method_id': generate_payment_method_id(),
            'name': choice(['Cash', 'Debit Card', 'Online Payments'])
        }
        payment_methods.append(payment_method)
    return payment_methods

def generate_orders(num_rows, customer_ids, branch_ids, payment_method_ids):
    orders = []
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2024, 12, 31)
    for _ in range(num_rows):
        order = {
            'order_id': generate_order_id(),
            'branch_id': choice(branch_ids),
            'customer_id': choice(customer_ids),
            'payment_method_id': choice(payment_method_ids),
            'order_date_time': fake.date_time_between(start_date=start_date, end_date=end_date).isoformat(),
            'order_type': choice(['walk in', 'delivery']),
            'total_amount': round(uniform(1000, 50000), 2)
        }
        orders.append(order)
    return orders

def generate_menu_items(num_rows):
    nigerian_dishes = [
        'Jollof Rice', 'Pounded Yam', 'Egusi Soup', 'Suya', 'Akara', 'Moin Moin', 'Eba', 'Ofada Rice',
        'Pepper Soup', 'Puff Puff', 'Chin Chin', 'Asun', 'Efo Riro', 'Banga Soup', 'Ogbono Soup',
        'Fried Rice', 'Dodo', 'Kilishi', 'Amala', 'Ewedu Soup'
    ]
    categories = ['Main Course', 'Appetizer', 'Dessert', 'Soup', 'Side Dish', 'Snack']
    menu_items = []
    for _ in range(num_rows):
        menu_item = {
            'menu_item_id': generate_menu_item_id(),
            'item_name': choice(nigerian_dishes),
            'category': choice(categories),
            'price': round(uniform(500, 5000), 2),
            'is_standard': choice(['Yes', 'No'])
        }
        menu_items.append(menu_item)
    return menu_items

def generate_order_items(num_rows, order_ids, menu_item_ids):
    order_items = []
    for _ in range(num_rows):
        order_item = {
            'order_item_id': generate_order_item_id(),
            'order_id': choice(order_ids),
            'menu_item_id': choice(menu_item_ids),
            'quantity': randint(1, 10)
        }
        order_items.append(order_item)
    return order_items

def generate_inventory(num_rows, branch_ids, menu_item_ids):
    inventory = []
    for _ in range(num_rows):
        inventory_item = {
            'inventory_id': generate_inventory_id(),
            'branch_id': choice(branch_ids),
            'menu_item_id': choice(menu_item_ids),
            'quantity': randint(0, 1000)
        }
        inventory.append(inventory_item)
    return inventory

# Generate data for all tables
num_rows = 20000

customers = generate_customers(num_rows)
branches = generate_branches(num_rows)
payment_methods = generate_payment_methods(num_rows)

customer_ids = [customer['customer_id'] for customer in customers]
branch_ids = [branch['branch_id'] for branch in branches]
payment_method_ids = [pm['payment_method_id'] for pm in payment_methods]

orders = generate_orders(num_rows, customer_ids, branch_ids, payment_method_ids)
menu_items = generate_menu_items(num_rows)

order_ids = [order['order_id'] for order in orders]
menu_item_ids = [item['menu_item_id'] for item in menu_items]

order_items = generate_order_items(num_rows, order_ids, menu_item_ids)
inventory = generate_inventory(num_rows, branch_ids, menu_item_ids)

# Save data to CSV files
def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

save_to_csv(customers, 'customers.csv')
save_to_csv(branches, 'branches.csv')
save_to_csv(payment_methods, 'payment_methods.csv')
save_to_csv(orders, 'orders.csv')
save_to_csv(menu_items, 'menu_items.csv')
save_to_csv(order_items, 'order_items.csv')
save_to_csv(inventory, 'inventory.csv')

print("Data generation complete. CSV files have been created.")