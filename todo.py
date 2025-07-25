# Date: 25th July 2025

def main():
    tasks = []

    while True:
        print("\n======= To-Do List =======")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")

        choice = input("Enter Your Choice: ")

        if choice == '1':
            print()
            n_tasks = int(input("How many tasks do you want to add?: "))

            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"tasks": task, "done": False})
                print("Task Added!")

        elif choice == '2':
            print("\nTasks: ")
            for index, task in enumerate(tasks):
                status = "Done" if task ["done"] else "Not Done"
                print(f"{index + 1}. {task['tasks']} - {status}")

        elif choice == '3':
            task_index = int(input("Enter the task Number to mark as Done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task Marked as Done!")
            else:
                print("Invalid Task Number.")

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid Choice. Please try again")

if __name__ == "__main__":
    main()