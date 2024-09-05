# controlador.py
class TaskController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_task(self, task):
        if task not in self.model.get_tasks():
            self.model.add_task(task)
            self.view.task_added(task)
        else:
            self.view.show_message(f"Task '{task}' already exists.")

    def remove_task(self, task):
        if task in self.model.get_tasks():
            self.model.remove_task(task)
            self.view.task_removed(task)
        else:
            self.view.show_message(f"Task '{task}' not found.")

    def show_tasks(self):
        tasks = self.model.get_tasks()
        if tasks:
            self.view.show_tasks(tasks)
        else:
            self.view.show_message("No tasks available.")