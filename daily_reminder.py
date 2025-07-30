# daily_reminder.py

print("Welcome to the Daily Reminder Converter!")

# 🟡 1. Prompt user inputs
task = input("Enter the task you want to be reminded of: ")
time_bound = input("Is this task time-bound? (yes/no): ").lower()
priority = input("Enter the priority level (high/medium/low): ").lower()

# 🟢 2. Match-case for priority
match priority:
    case "high":
        urgency_note = "This is a high-priority task. Attend to it immediately!"
    case "medium":
        urgency_note = "This task is of medium importance. Schedule it soon."
    case "low":
        urgency_note = "This is a low-priority task. No rush, but don’t forget."
    case _:
        urgency_note = "Unknown priority. Treat accordingly."

# 🔵 3. Modify reminder based on time-bound
if time_bound == "yes":
    reminder = f"Reminder: {task} is time-bound and should be completed ASAP."
else:
    reminder = f"Reminder: {task} can be done at your convenience."

# 🟣 4. Final custom reminder
print("\n--- DAILY REMINDER ---")
print(reminder)
print(urgency_note)
