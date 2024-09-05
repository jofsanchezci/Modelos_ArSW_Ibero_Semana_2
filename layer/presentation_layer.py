# presentation_layer.py
from business_layer import BusinessLayer

class PresentationLayer:
    def __init__(self):
        self.business_layer = BusinessLayer()

    def run(self):
        while True:
            print("\nGestión de Usuarios")
            print("1. Crear Usuario")
            print("2. Ver Detalles de Usuario")
            print("3. Ver Todos los Usuarios")
            print("4. Salir")
            choice = input("Selecciona una opción: ")

            if choice == '1':
                username = input("Nombre de usuario: ")
                email = input("Correo electrónico: ")
                result = self.business_layer.create_user(username, email)
                print(result)
            elif choice == '2':
                username = input("Nombre de usuario: ")
                result = self.business_layer.get_user_details(username)
                print(result)
            elif choice == '3':
                users = self.business_layer.get_all_users()
                for user in users:
                    print(f"Usuario: {user['username']}, Email: {user['email']}")
            elif choice == '4':
                print("Saliendo...")
                break
            else:
                print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    presentation = PresentationLayer()
    presentation.run()
