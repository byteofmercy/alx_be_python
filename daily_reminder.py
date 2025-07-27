# daily_reminder.py

# Prompt user for the task
task = input("Enter your task: ")

# Prompt user for the priority level
priority = input("Priority (high/medium/low): ")

# Prompt user if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ")

# Use match-case to respond based on priority
match priority.lower():
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unknown priority"

# Modify message if time-bound
if time_bound.lower() == "yes":
    message += " that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."

# Print the final reminder
print("Reminder:", message)

