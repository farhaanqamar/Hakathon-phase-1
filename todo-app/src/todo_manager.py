import uuid

class TodoManager:
    def __init__(self):
        self.tasks = {}
        self.next_id = 1

    def add_task(self, title, description=""):
        if not title:
            return None, "Task title cannot be empty."
        
        task_id = self.next_id
        self.next_id += 1
        task = {
            "id": task_id,
            "title": title,
            "description": description,
            "status": "Pending"
        }
        self.tasks[task_id] = task
        return task, None

    def get_all_tasks(self):
        return list(self.tasks.values())

    def update_task(self, task_id, new_title=None, new_description=None):
        task = self.tasks.get(task_id)
        if not task:
            return False, "Task not found."

        updated = False
        if new_title is not None and new_title != "":
            task["title"] = new_title
            updated = True
        if new_description is not None:
            task["description"] = new_description
            updated = True
        
        if not updated and new_title == "": # Handle case where user explicitly clears title
            task["title"] = ""
            updated = True

        return updated, None

    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True, None
        return False, "Task not found."

    def mark_task_status(self, task_id, is_complete):
        task = self.tasks.get(task_id)
        if not task:
            return False, "Task not found."
        
        task["status"] = "Complete" if is_complete else "Pending"
        return True, None
