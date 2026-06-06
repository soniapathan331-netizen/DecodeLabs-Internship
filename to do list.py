# ============================================
# PROJECT 1: TO-DO LIST
# DecodeLabs Industrial Training - Batch 2026
# ============================================

my_tasks = []  # This is our "database" (empty list)

def add_task():
    task = input("Enter your task: ")
    my_tasks.append(task)
    print(f"✅ Task '{task}' added successfully!\n")

def view_tasks():
    if len(my_tasks) == 0:
        print("📭 No tasks yet! Add some tasks first.\n")
    else:
        print("\n📋 YOUR TO-DO LIST:")
        print("-" * 30)
        for index, task in enumerate(my_tasks, start=1):
            print(f"{index}. {task}")
        print("-" * 30)
        print()

def main():
    print("🚀 Welcome to DecodeLabs To-Do List!")
    print("=====================================\n")
    
    while True:
        print("Choose an option:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")
        
        choice = input("\nEnter choice (1/2/3): ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()