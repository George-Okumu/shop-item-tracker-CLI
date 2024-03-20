from item import Item
from category import Category
from tabulate import tabulate

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. See all stock")
    print("2. See all categories")
    print("3: Add Category")
    print("4: Add stock")

def print_items_neat(data):
    rows = [[item['id'], item['name'], item['batch_number'], item['price'], item['category'],item['quantity'],item['price_per_piece'],item['unit'], item['created_at']] for item in data]

    headers = ["ID", "Name", "Batch Number", "Price", "Unit","Quantity", "Price Per Piece","Category",  "Created On"]

    table = tabulate(rows, headers=headers, tablefmt="pretty")
    print(table)

def print_categories_neat(data):
    rows = [[item['id'], item['name'], item['description']] for item in data]
    headers = ["ID", "Name", "Description"]
    table = tabulate(rows, headers=headers, tablefmt="pretty")
    print(table)
    

def print_all_items():
    print("Here are all stock you have:")
    print_items_neat(Item.get_all_items())
    
def print_all_categories():
    print("Below are available category:")
    print_categories_neat(Category.get_all_items())
    
def get_item_details_from_cli():
    name = input("Enter item name: ").capitalize()
    batch = input("Enter batch number: ").upper()
    price = float(input("Enter price: "))
    quan = input("Enter item quantity: ")
    price_per_each = input("Enter Price per each item: ")
    unit = input("Enter unit of measure: ").upper()
    cat = input("Enter category: ")
    add_stock(name, batch, price,quan, price_per_each,cat, unit)
    
def add_stock(name, batch, price,quan, price_per_each, cat, unit):
    item = Item(name=name, batch_number=batch, price=price,quantity=quan, price_per_piece=price_per_each, category=cat, unit=unit)
    item.save()

def get_category_details_from_cli():
    name = input("Enter category name: ")
    descr = input("Provide a brief description of this category: ") 
    add_category(name, descr)
    
def add_category(name, descr):
    cat = Category(name=name, description=descr)
    cat.save()
    print("Category saved successfully")
    print("                                     ")
    print("                                     ")
    
    
def exit():
    print("Thank you for interacting with Duka. We make sure your stock is always recorded.")
    quit()