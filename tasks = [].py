tasks = []

while True:
    print("\nTo-Do List Manager")
    print("1. Add Task")
    print("2. Mark Task as Done")
    print("3. Remove Task")
    print("4. View Tasks")
    print("5. View Task Details")
    print("6. Quit")

    choice = input("Choose an option: ")

    if choice == '1':
        task_name = input("Enter task name: ")
        tasks.append([task_name, False])
        print(f"Task '{task_name}' added!")

    elif choice == '2':
        task_number = int(input("Enter the task number to mark as done: ")) - 1
        if 0 <= task_number < len(tasks):
            tasks[task_number][1] = True
            print(f"Task '{tasks[task_number][0]}' marked as done!")
        else:
            print("Invalid task number!")

    elif choice == '3':
        task_number = int(input("Enter the task number to remove: ")) - 1
        if 0 <= task_number < len(tasks):
            removed_task = tasks.pop(task_number)
            print(f"Task '{removed_task[0]}' removed!")
        else:
            print("Invalid task number!")

    elif choice == '4':
        if tasks:
            for i, (name, done) in enumerate(tasks):
                print(f"{i + 1}. {name} - {'Done' if done else 'Not Done'}")
        else:
            print("No tasks to display.")

    elif choice == '5':
        if tasks:
            task_number = int(input("Enter the task number to edit: ")) - 1
            if 0 <= task_number < len(tasks):
                new_name = input("Enter the new task name (leave blank to keep current): ")
                if new_name:
                    tasks[task_number][0] = new_name
                new_status = input("Enter new status (done/not done, leave blank to keep current): ").strip().lower()
                if new_status == 'done':
                    tasks[task_number][1] = True
                elif new_status == 'not done':
                    tasks[task_number][1] = False
                print(f"Task {task_number + 1} updated!")
            else:
                print("Invalid task number!")
        else:
            print("No tasks to edit.")

    elif choice == '6':
        print("Exiting List")
        break

    else:
        print("Invalid choice")