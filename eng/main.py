import json
import os
from datetime import datetime

tasks = [
    '1 - Add a task',
    '2 - Delete a task',
    '3 - View tasks',
    '4 - Mark the task as COMPLETED/NOT COMPLETED',
    '5 - Exit'
]

TODO_FILE = 'data.json'

def load_tasks():
    """Loads tasks from data.json to the dictionary. If there is no file, returns an empty dictionary."""
    if not os.path.exists(TODO_FILE):
        return {}
    with open(TODO_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_tasks(tasks_dict):
    """Saves tasks from the dictionary to data.json"""
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks_dict, f, indent=4, ensure_ascii=False)

def add():
    """Adds a task"""
    tasks_dict = load_tasks()

    name = input('Enter a name: ').strip()
    if not name:
        print("The task name cannot be empty!")
        return
    if name in tasks_dict:
        print("A task with that name already exists!")
        return

    description = input('Enter a description (optional): ').strip()
    date = datetime.today().date().isoformat()

    task_data = {
        "description": description,
        "date": date,
        "isDone": False
    }

    tasks_dict[name] = task_data
    save_tasks(tasks_dict)
    print(f'Task "{name}" has been added!')
    print()
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')

def delete():
    """Deletes the task"""
    tasks_dict = load_tasks()

    name = input('Enter a name: ').strip()
    if name not in tasks_dict:
        print(f"Task '{name}' not found!")
        return

    del tasks_dict[name]
    save_tasks(tasks_dict)
    print(f'Task "{name}" has been deleted!')
    print()
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')

def view():
    """Views tasks"""
    tasks_dict = load_tasks()

    if not tasks_dict:
        print("The task list is empty.")
    else:
        for name, data in tasks_dict.items():
            status = 'Completed' if data["isDone"] else 'Not completed'
            print(f'- {name} - [{status}]')
            print(f'  Description: {data["description"]}')
            print(f'  Date added: {data["date"]}')
            print()

    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')

def correct():
    """Marks the task as completed/not completed"""
    tasks_dict = load_tasks()

    name = input('Enter a name: ').strip()
    if name not in tasks_dict:
        print(f"Task '{name}' not found!")
        return

    current_status = tasks_dict[name]["isDone"]
    new_status = not current_status
    tasks_dict[name]["isDone"] = new_status

    status_text = "Completed" if new_status else "Not completed"
    print(f'Task status "{name}" changed to "{status_text}"')

    save_tasks(tasks_dict)
    print()
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    print('=== ToDo Sheet (JSON) ===')
    print(*tasks, sep='\n')
    election = input('>> ').strip().lower()
    os.system('cls' if os.name == 'nt' else 'clear')
    return election

while True:
    election = main()
    if election in ['1', 'add task', 'add']:
        add()
    elif election in ['2', 'delete task', 'delete']:
        delete()
    elif election in ['3', 'view tasks', 'view']:
        view()
    elif election in ['4', 'mark task as completed/not completed', 'mark task as', 'mark']:
        correct()
    elif election in ['5', 'exit']:
        break
    else:
        print('Incorrect selection')
        input("Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')

input('\nPress [ENTER] to exit\n')
