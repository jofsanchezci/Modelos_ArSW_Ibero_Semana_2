
# Modelo-Vista-Controlador (MVC) en Python

Este proyecto es una implementación simple del patrón Modelo-Vista-Controlador (MVC) en Python. El ejemplo representa una pequeña aplicación que permite gestionar una lista de tareas.

## Estructura del Proyecto:

- **Modelo (Model)**: Gestiona los datos de la aplicación, en este caso, una lista de tareas.
- **Vista (View)**: Responsable de mostrar los datos al usuario y mostrar mensajes relevantes.
- **Controlador (Controller)**: El intermediario entre la vista y el modelo, maneja la lógica de la aplicación y responde a las interacciones del usuario.

## Archivos:
1. `modelo.py`: Implementa el modelo para gestionar la lista de tareas.
2. `vista.py`: Implementa la vista para mostrar las tareas y mensajes al usuario.
3. `controlador.py`: Implementa el controlador que gestiona la interacción entre la vista y el modelo.
4. `main.py`: El archivo principal que ejecuta la aplicación.

## Ejecución:

1. Para agregar una tarea, el controlador actualiza el modelo y la vista notifica que la tarea ha sido añadida.
2. Para eliminar una tarea, el controlador elimina la tarea del modelo y la vista muestra un mensaje de confirmación.
3. Puedes ver las tareas actuales usando el método `show_tasks()`.

### Ejemplo de uso:

```bash
# Ejecutar el archivo main.py para interactuar con la aplicación
python main.py
```

### Ejemplo en código:

```python
# main.py
if __name__ == "__main__":
    # Crear instancias del modelo, la vista y el controlador
    model = TaskModel()
    view = TaskView()
    controller = TaskController(model, view)

    # Añadir tareas
    controller.add_task("Comprar leche")
    controller.add_task("Ir al gimnasio")
    controller.add_task("Leer un libro")

    # Mostrar tareas actuales
    controller.show_tasks()

    # Eliminar una tarea
    controller.remove_task("Ir al gimnasio")

    # Mostrar tareas actualizadas
    controller.show_tasks()
```

## Explicación:

- **Modelo**: `TaskModel` es responsable de mantener y gestionar la lista de tareas.
- **Vista**: `TaskView` presenta los datos y muestra mensajes sobre las tareas.
- **Controlador**: `TaskController` es responsable de interactuar con el modelo y la vista para coordinar la adición, eliminación y visualización de tareas.

