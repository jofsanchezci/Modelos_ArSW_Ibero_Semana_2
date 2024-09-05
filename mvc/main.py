# main.py
from modelo import TaskModel
from vista import TaskView
from controlador import TaskController
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
    controller.remove_task("Comprar leche")

    # Mostrar tareas actualizadas
    controller.show_tasks()