# daily_reminder.py

# Step 1: Ask the user for task details
task = input("Enter your task: ")
time_bound = input("Is this task time-bound? (yes/no): ").lower()
priority = input("Set priority (High/Medium/Low): ").capitalize()

# Step 2: Use match-case to customize the priority response
match priority:
    case "High":
        priority_message = "This is a high-priority task."
    case "Medium":
        priority_message = "This is a medium-priority task."
    case "Low":
        priority_message = "This is a low-priority task."
    case _:
        priority_message = "Priority not recognized."

# Step 3: Use if to modify based on time-bound response
if time_bound == "yes":
    urgency = "Immediate action is required!"
else:
    urgency = "No immediate action needed."

# Step 4: Print the final customized reminder
print("\n--- Daily Reminder ---")
print(f"Task: {task}")
print(f"Priority: {priority}")
print(priority_message)
print(urgency)

