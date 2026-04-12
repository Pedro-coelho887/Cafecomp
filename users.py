class User:
    def __init__(self,permission=None):
        self.permission = permission
        self.drink = None

class Admin(User):
    def __init__(self):
        super().__init__("admin")

