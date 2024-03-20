import uuid
from dbqueries import insert_categories, select_all_categories

class Category():
    def __init__(self, name, description) -> None:
        self.id = uuid.uuid4().hex
        self.name = name
        self.description = description

    def __str__(self):
            return f"Category ID: {self.id}, Name: {self.name}, Description: {self.description}"
        
    def save(self):
        insert_categories(self.name, self.description)
        
        
    @classmethod
    def get_all_items(cls):
        category_list = []
        for row in select_all_categories():
            item = cls(row[1], row[2])
            item.id = uuid.uuid4().__hash__()
            category_list.append(item.__dict__)
                        
        return category_list