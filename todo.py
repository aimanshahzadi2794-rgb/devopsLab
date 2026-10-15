import json
import sys

FILE = "todos.json"


def load():
    try:
        with open(FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save(todos):
    with open(FILE, "w") as f:
        json.dump(todos, f, indent=2)


def add(text):
    todos = load()
    todos.append({"text": text, "done": False})
    save(todos)
    print("Added:", text)


def list_todos():
    todos = load()
    if not todos:
        print("Nothing to do!")
    for i, t in enumerate(todos, 1):
        mark = "x" if t["done"] else " "
        print(f"{i}. [{mark}] {t['text']}")


def done(number):
    todos = load()
    todos[number - 1]["done"] = True
    save(todos)
    print("Done:", todos[number - 1]["text"])


def clear():
    save([])
    print("Cleared all todos")

def delete(number):
    todos = load()
    removed = todos.pop(number - 1)
    save(todos)
    print("Deleted:", removed["text"])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python todo.py add <text> | list | done <number>")
    elif sys.argv[1] == "add":
        add(" ".join(sys.argv[2:]))
    elif sys.argv[1] == "list":
        list_todos()
    elif sys.argv[1] == "done":
        done(int(sys.argv[2]))
    elif sys.argv[1] == "delete":
        delete(int(sys.argv[2]))
