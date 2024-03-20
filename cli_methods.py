from item import Item
from category import Category
from tabulate import tabulate

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. See all stock")
    print("2. See all categories")

def print_items_neat(data):
    rows = [[item['id'], item['name'], item['batch_number'], item['price'], item['category']] for item in data]

    headers = ["ID", "Name", "Batch Number", "Price", "Category"]

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
    
    
def exit():
    print("Thank you for interacting with Duka. We make sure your stock is always recorded.")
    exit()