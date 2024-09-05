# vista.py
class TaskView:
    @staticmethod
    def show_tasks(tasks):
        print("Current Tasks:")
        for task in tasks:
            print(f"- {task}")

    @staticmethod
    def task_added(task):
        print(f"Task '{task}' has been added.")

    @staticmethod
    def task_removed(task):
        print(f"Task '{task}' has been removed.")

    @staticmethod
    def show_message(message):
        print(message)
