# Daily Reminder Program

# Ask the user for details
task = input("What task do you need to do? ")
time_bound = input("Is this task time-bound? (yes/no): ").lower()
priority = input("What is the priority level? (high/medium/low): ").lower()

# Match-case structure for task response
match task.lower():
    case "study":
        print("📘 Remember to find a quiet place to study.")
    case "exercise":
        print("🏃‍♀️ Time to move! Don’t forget to warm up.")
    case "meeting":
        print("📅 Make sure your calendar is updated.")
    case _:
        print("📝 Got it! Let’s stay on track.")

# Modify reminder if the task is time-bound
if time_bound == "yes":
    print("⏰ This task is time-sensitive! Plan your time wisely.")

# Provide a customized reminder
print(f"Reminder: You need to '{task}' with {priority.upper()} priority.")
if priority == "high" and time_bound == "yes":
    print("⚠️ Act immediately. This is both important and urgent!")

