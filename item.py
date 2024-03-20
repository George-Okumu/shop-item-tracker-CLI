import uuid
from dbqueries import insert_items, select_all_items

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
        insert_items(self.name, self.batch_number, self.price, self.category)
    
    # return list mapped in dict
    @classmethod
    def get_all_items(cls):
        item_list = []
        for row in select_all_items():
            item = cls(row[1], row[2], row[3], row[4])
            item.id = uuid.uuid4().__hash__()
            item.created_at = row[5]
            item_list.append(item.__dict__)
                        
        return item_list