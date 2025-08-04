"""""
Simple To‑Do List App (console)

Stores tasks in a Python list; supports adding, removing, and viewing.
"""

def add_task(tasks: list[str], task: str) -> None:
    """
    Add `task` onto the end of the tasks list.
    """
    tasks.append(task)
    print(f"Added: {task!r}")

def remove_task(tasks: list[str], index: int) -> None:
    """
    Removes the task at given zero-based `index`, if valid.
    """
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Removed: {removed!r}")
    else:
        print("Invalid index — nothing removed.")

def view_tasks(tasks: list[str]) -> None:
    """
    Displays all tasks with 1‑based numbering.
    """
    if not tasks:
        print("(🗂️) No tasks in your to‑do list.")
    else:
        print("📋 Your To‑Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"  {i}. {task}")

def main():
    tasks: list[str] = []
    while True:
        print("\n--- MENU ---")
        print("1) Add Task")
        print("2) Remove Task")
        print("3) View Tasks")
        print("4) Quit")
        choice = input("Enter choice #: ").strip()

        if choice == '1':
            task = input("What task would you like to add? ").strip()
            if task:
                add_task(tasks, task)
            else:
                print("No task entered; nothing added.")
        elif choice == '2':
            view_tasks(tasks)
            try:
                idx = int(input("Enter task number to remove: "))
                remove_task(tasks, idx - 1)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '3':
            view_tasks(tasks)
        elif choice == '4':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid option — please select 1, 2, 3, or 4.")

if __name__ == '__main__':
    main()
