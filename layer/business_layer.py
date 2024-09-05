# business_layer.py
from data_layer import DataLayer

class BusinessLayer:
    def __init__(self):
        self.data_layer = DataLayer()

    def create_user(self, username, email):
        if self.data_layer.get_user(username):
            return f"Error: El usuario '{username}' ya existe."
        else:
            user = {'username': username, 'email': email}
            self.data_layer.add_user(user)
            return f"Usuario '{username}' creado exitosamente."

    def get_user_details(self, username):
        user = self.data_layer.get_user(username)
        if user:
            return user
        else:
            return f"Error: Usuario '{username}' no encontrado."

    def get_all_users(self):
        return self.data_layer.get_all_users()
