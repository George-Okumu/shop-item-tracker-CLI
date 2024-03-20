import uuid
from dbqueries import save_items

class Item():
    def __init__(self, name, batch_number, price, category) -> None:
        self.id = uuid.uuid4().hex
        self.name = name
        self.batch_number = batch_number
        self.price = price
        self.category = category

    def __str__(self):
            return f"Item ID: {self.id}, Name: {self.name}, Batch Number: {self.batch_number}, Price: ${self.price}, Category: {self.category}"
    
    
    def save(self):
        save_items(self.name, self.batch_number, self.price, self.category)
        
    