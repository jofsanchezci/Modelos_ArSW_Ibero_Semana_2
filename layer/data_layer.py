# data_layer.py
class DataLayer:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def get_user(self, username):
        for user in self.users:
            if user['username'] == username:
                return user
        return None

    def get_all_users(self):
        return self.users
