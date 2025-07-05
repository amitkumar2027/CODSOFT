class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if task.strip():
            self.tasks.append(task.strip())
            return True
        return False

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            return self.tasks.pop(index)
        return None

    def get_tasks(self):
        return self.tasks

    def clear_all(self):
        self.tasks.clear()
