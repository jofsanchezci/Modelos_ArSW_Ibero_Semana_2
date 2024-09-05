
# Implementación del Patrón de Capas en Python

Este proyecto es una implementación básica del **patrón de capas** en Python. El patrón de capas organiza el software en capas, donde cada capa tiene una responsabilidad específica. En este ejemplo, gestionamos usuarios en un sistema con tres capas:

1. **Capa de Datos (Data Layer)**: Se encarga de la gestión de los datos de los usuarios.
2. **Capa de Negocio (Business Layer)**: Contiene la lógica de negocio relacionada con los usuarios.
3. **Capa de Presentación (Presentation Layer)**: Interactúa con el usuario y utiliza la capa de negocio para realizar operaciones.

## Estructura del Proyecto:

- **data_layer.py**: Implementa la capa de datos, que almacena y recupera la información de los usuarios.
- **business_layer.py**: Implementa la lógica de negocio para crear y consultar usuarios.
- **presentation_layer.py**: Implementa la interfaz de usuario en consola que permite interactuar con el sistema.

## Archivos:

1. `data_layer.py`: Gestiona los datos, permitiendo añadir y recuperar usuarios.
2. `business_layer.py`: Valida y maneja la lógica de creación y consulta de usuarios.
3. `presentation_layer.py`: Proporciona un menú para interactuar con el usuario y acceder a las funcionalidades.

## Cómo ejecutar:

1. Crea los archivos `data_layer.py`, `business_layer.py` y `presentation_layer.py` en el mismo directorio.
2. Ejecuta el archivo `presentation_layer.py`:
   ```bash
   python presentation_layer.py
   ```

### Ejemplo en código:

#### Capa de Datos:

```python
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
```

#### Capa de Negocio:

```python
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
```

#### Capa de Presentación:

```python
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
```

## Descripción del funcionamiento:

- **Capa de Datos**: Se encarga de almacenar los usuarios y proporcionar métodos para obtener usuarios por su nombre de usuario.
- **Capa de Negocio**: Implementa la lógica de negocio para crear y recuperar usuarios, asegurando que no haya duplicados.
- **Capa de Presentación**: Proporciona una interfaz interactiva para que el usuario pueda crear y ver usuarios.

Este proyecto ilustra cómo estructurar una aplicación utilizando el patrón de capas para separar la lógica de presentación, negocio y datos.
