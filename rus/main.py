import json
import os
from datetime import datetime

tasks = [
    '1 - Добавить задачу',
    '2 - Удалить задачу',
    '3 - Просмотреть задачи',
    '4 - Отметить задачу как ВЫПОЛНЕНО/НЕ ВЫПОЛНЕНО',
    '5 - Выход'
]

TODO_FILE = 'data.json'

def load_tasks():
    """Загружает задачи из data.json в словарь. Если файла нет, возвращает пустой словарь."""
    if not os.path.exists(TODO_FILE):
        return {}
    with open(TODO_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_tasks(tasks_dict):
    """Сохраняет задачи из словаря в data.json"""
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks_dict, f, indent=4, ensure_ascii=False)

def add():
    """Добавляет задачу"""
    tasks_dict = load_tasks()

    name = input('Введите название: ').strip()
    if not name:
        print("Название задачи не может быть пустым!")
        return
    if name in tasks_dict:
        print("Задача с таким названием уже существует!")
        return

    description = input('Введите описание (опционально): ').strip()
    date = datetime.today().date().isoformat()

    task_data = {
        "description": description,
        "date": date,
        "isDone": False
    }

    tasks_dict[name] = task_data
    save_tasks(tasks_dict)
    print(f'Задача "{name}" добавлена!')
    print()
    input("Нажмите Enter для продолжения...")

def delete():
    """Удаляет задачу"""
    tasks_dict = load_tasks()

    name = input('Введите название: ').strip()
    if name not in tasks_dict:
        print(f"Задача '{name}' не найдена!")
        return

    del tasks_dict[name]
    save_tasks(tasks_dict)
    print(f'Задача "{name}" удалена!')
    print()
    input("Нажмите Enter для продолжения...")

def view():
    """Просматривает задачи"""
    tasks_dict = load_tasks()

    if not tasks_dict:
        print("Список задач пуст.")
        input("Нажмите Enter для продолжения...")
        return

    for name, data in tasks_dict.items():
        status = 'Выполнено' if data["isDone"] else 'Не выполнено'
        print(f'- {name} - [{status}]')
        print(f'  Описание: {data["description"]}')
        print(f'  Дата добавления: {data["date"]}')
        print()

    input("Нажмите Enter для продолжения...")

def correct():
    """Отмечает задачу как выполненную/не выполненную"""
    tasks_dict = load_tasks()

    name = input('Введите название: ').strip()
    if name not in tasks_dict:
        print(f"Задача '{name}' не найдена!")
        return

    current_status = tasks_dict[name]["isDone"]
    new_status = not current_status
    tasks_dict[name]["isDone"] = new_status

    status_text = "Выполнено" if new_status else "Не выполнено"
    print(f'Статус задачи "{name}" изменён на "{status_text}"')

    save_tasks(tasks_dict)
    print()
    input("Нажмите Enter для продолжения...")

def main():
    print('=== ToDo Лист (JSON) ===')
    print(*tasks, sep='\n')
    election = input('>> ').strip().lower()
    os.system('cls' if os.name == 'nt' else 'clear')
    return election

while True:
    election = main()
    if election in ['1', 'добавить задачу', 'добавить']:
        add()
    elif election in ['2', 'удалить задачу', 'удалить']:
        delete()
    elif election in ['3', 'просмотреть задачи', 'просмотреть']:
        view()
    elif election in ['4', 'отметить задачу как выполнено/не выполнено', 'отметить задачу как', 'отметить']:
        correct()
    elif election in ['5', 'выход']:
        break
    else:
        print('Неправильный выбор')
        input("Нажмите Enter для продолжения...")

input('\nНажмите [ENTER] для выхода\n')
