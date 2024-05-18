import os

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        return f"[{'x' if self.completed else ' '}] {self.description}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print("Task added.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            print("Task deleted.")
        else:
            print("Invalid task index.")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks.")
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    task_manager = TaskManager()
    
    while True:
        clear_screen()
        print("Task Manager")
        print("------------")
        task_manager.list_tasks()
        print("\nOptions:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            task_manager.add_task(description)
        elif choice == '2':
            index = int(input("Enter task number to delete: ")) - 1
            task_manager.delete_task(index)
        elif choice == '3':
            index = int(input("Enter task number to mark as completed: ")) - 1
            task_manager.complete_task(index)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
