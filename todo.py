tasks = []
def display_menu():
    print("\n To-Do List Menu:")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Exit")

def add_task():
    task = input("Enter a task: ")
    tasks.append({"task": task,"completed":False})
    print(f"'{task}' added to the list")

def view_task():
    if not tasks:
        print("Your To-do List is empty.")
    else:
        for index, task in enumerate(tasks, start=1):
           status = "Done" if task["completed"] else "Not done"
           print(f"{index} : {task} : {status}")
def mark_task_completed():
    task_number = int(input("Enter the task which is to be completed as marked"))    
    if 0<task_number<= len(tasks):
        tasks[task_number-1]["completed"] = True
        print(f" Task {task_number + 1} marked as complete")
    else:
        print("Invalid task number.")
def delete_task():
    task_number = int(input("Enter the task to be deleted"))
    if 0<task_number <=len(tasks):
        del tasks[task_number-1]
        print(f"Task {task_number} has been deleted")
    else:
        print("Invalid entry")
while True:
    display_menu()
    choice = input("Enter your choice (1-5)")
    
    if choice == "1":
        add_task()
    elif choice =="2":
        view_task()
    elif choice == "3":
        mark_task_completed()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting the program")       
        break 
    else :
        print("Invalid option have been entered")
