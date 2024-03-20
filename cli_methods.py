from item import Item
from category import Category

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. See all stock")
    print("2. See all categories")


def print_all_items():
    print("Here are all stock you have:")
    print(Item.get_all_items())
    
def print_all_categories():
    print("Below are available category:")
    print(Category.get_all_items())
    
    
def exit():
    print("Thank you for interacting with Duka. We make sure your stock is always recorded.")
    exit()