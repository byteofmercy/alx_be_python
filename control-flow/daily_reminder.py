# daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority.lower():
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        message = f"Reminder: '{task}' has an unknown priority."

if time_bound.lower() == "yes" and priority.lower() in ("high", "medium"):
    message += " that requires immediate attention today!"
elif time_bound.lower() == "yes" and priority.lower() == "low":
    message = f"Note: '{task}' is a low priority task that requires immediate attention today!"
    
print(message)
