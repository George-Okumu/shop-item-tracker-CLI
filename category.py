import uuid
from dbqueries import insert_categories

class Category():
    def __init__(self, name, description) -> None:
        self.id = uuid.uuid4().hex
        self.name = name
        self.description = description

    def __str__(self):
            return f"Category ID: {self.id}, Name: {self.name}, Description: {self.description}"
        
    def save(self):
        insert_categories(self.name, self.description)