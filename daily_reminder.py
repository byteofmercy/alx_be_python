# daily_reminder.py

# Step 1: Prompt the user for task details
task = input("Enter the task: ")
time_bound = input("Is the task time-bound? (yes/no): ").strip().lower()
priority = input("Enter the priority (low, medium, high): ").strip().lower()

# Step 2: Build the base reminder
reminder = f"Reminder: {task} - Priority: {priority.title()}"

# Step 3: Modify reminder if time-bound
if time_bound == "yes":
    reminder += " [Requires immediate attention due to time sensitivity]"

# Step 4: Match-case to customize response
match priority:
    case "low":
        reminder += "\nTip: You can schedule this for later in the day."
    case "medium":
        reminder += "\nTip: Try to complete this by the end of the day."
    case "high":
        reminder += "\nTip: Start working on this task immediately!"
    case _:
        reminder += "\nWarning: Unknown priority level."

# Step 5: Print the customized reminder
print("\n" + reminder)
