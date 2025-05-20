# file name
TASK_FILE = "task.txt"


# function to load task in task form file.
def load_task():
    try:
        with open(TASK_FILE, "r") as file:
            tasks = file.readline()
            return [
                task.strip() for task in tasks
            ]  # run loop on task.strip() funtion on each task in tasks.
    except FileNotFoundError:
        return []

#  save task in file. 
def save_task(tasks):
    with open(TASK_FILE, 'w') as file: 
        for task in tasks: 
            file.write(task + '\n')


# main loop 
def todo_app():
    tasks = load_task()

    while True: 
        print("\n📋 To-Do List Menu:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("\n Your tasks: ")
            
            if tasks:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
            else: 
                print("No task yet.")
        
        elif choice == '2':
            new_task = input("Enter new task: ")
            tasks.append(new_task)
            save_task(tasks)
            print("Task Added!")
        
        elif choice == '3':
            try: 
                task_number = int(input("Enter task number to delete: "))
                if 1 <= task_number <= len(tasks):
                    removed = tasks.pop(task_number - 1)
                    save_task(tasks)
                    print(f"removed {removed}")
                else: 
                    print("Invaild task number.")
            except ValueError:
                print("Please enter a number.")

        elif choice == '4':
            print("Exiting from Todo, Bye.")
            break
    
        else: 
            print("Please choose right number form 1 to 4")

todo_app()

