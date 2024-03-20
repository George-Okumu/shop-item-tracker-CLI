import uuid

class Item():
    def __init__(self, name, batchnumber, price, category) -> None:
        self.id = uuid.uuid4().hex
        self.name = name
        self.batchnumber = batchnumber
        self.price = price
        self.category = category