import uuid

class Category():
    def __init__(self, name, description) -> None:
        self.id = uuid.uuid4().hex
        self.name = name
        self.description = description

