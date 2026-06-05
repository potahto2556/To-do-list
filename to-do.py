tasks = []
def add_task(task):
    tasks.append(task)
    print("Task added:", task)
def view_tasks():
    for i, task in enumerate(tasks, start=1):
        print(i, "-", task)
def delete_task(el):
    if el in tasks:
      tasks.remove(el)
      print("removed ->", el)
    else:
        print("Task not found:", el)
def save_tasks():
    file = open("tasks.txt", "w")
    for task in tasks:
        file.write(task + "\n")
    file.close()
    print("File saved!")
def load_tasks():
    try:
        file = open("tasks.txt", "r")
        file.close()
    except FileNotFoundError:
        print("No saved tasks found, starting fresh!")

load_tasks()

while True:
    print("\nWhat do you want to do?")
    print("1 - View tasks")
    print("2 - Add task")
    print("3 - Delete task")
    print("4 - Quit")

    choice = input("Enter choice: ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        task = input("Enter task: ")
        add_task(task)
        save_tasks()
    elif choice == "3":
        view_tasks()
        task = input("Which task to delete: ")
        delete_task(task)
        save_tasks()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again!")