# daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority.lower():
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        reminder = f"Reminder: '{task}' has an unknown priority."

if time_bound.lower() == "yes":
    # Add time sensitivity only if task is not low priority
    if priority.lower() in ("high", "medium"):
        reminder += " that requires immediate attention today!"
    elif priority.lower() == "low":
        reminder = f"Note: '{task}' is a low priority task that requires immediate attention today!"

print(reminder)

