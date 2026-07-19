import datetime as dt
from os import path
import json

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = {}

        ## loading and saving the tasks

    def load_tasks(self):
        if not path.exists(self.filename):
            self.tasks = {}
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump(self.tasks, f)
            return

        with open(self.filename, "r", encoding="utf-8") as f:
            try:
                self.tasks = json.load(f)
            except json.JSONDecodeError:
                self.tasks = {}

    def save_tasks(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.tasks, f, indent=2)

    ## geting the next-id
    def get_next_id(self):
        ...

    ## operations

    def add_tasks(self,task):
        next_id = self.get_next_id
        self.tasks[next_id] = {
            self.description : task,
            self.status : "todo",
            self.createdAt : str(dt.datetime.now()),
            self.updatedAt : str(dt.datetime.now())
        }

    def update_tasks(self,task_id,task):

        if task_id not in self.tasks:
            print(f"task with task ID {task_id} does not exits")

        self.tasks[task_id]["description"] = task
        self.tasks[task_id]["updatedAt"] = str(dt.datetime.now())

    def delete_tasks(self,task_id):
        if task_id not in self.tasks:
            print(f"task with task ID {task_id} does not exits")
        else:
            del self.tasks[task_id]
            print("Task Deleted")

    def modify_status(self,status,task_id):
        if task_id not in self.tasks:
            print(f"task with task ID {task_id} does not exits")

        self.tasks[task_id]["status"] = status
        self.tasks[task_id]["updatedAt"] = str(dt.datetime.now())

    def listing(self):
        print(self.tasks)

    def listing_by_status(self,status):
        for key,value in self.tasks.values():
            if self.tasks[key]["status"] == status:
                print(key,value)
        
