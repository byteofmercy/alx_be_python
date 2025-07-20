from datetime import date

# Print today's date
print(f"\n📅 Today is {date.today().strftime('%A, %d %B %Y')}")

# Prompt for inputs
task = input("📝 Enter your task: ")
time_bound = input("⏰ Is this task time-bound? (yes/no): ").lower()
priority = input("🚦 Enter the priority (High/Medium/Low): ").capitalize()

# Time-sensitive reminder
if time_bound == "yes":
    print(f"\n🔔 Reminder: '{task}' — This task is time-sensitive! Please handle it ASAP.")
else:
    print(f"\n📝 Reminder: '{task}' — No immediate deadline, but stay on track.")

# Match-case for priority
match priority:
    case "High":
        print("⚠️ Priority: High — Give this task immediate attention.")
    case "Medium":
        print("🔶 Priority: Medium — Plan to work on this soon.")
    case "Low":
        print("✅ Priority: Low — Can be handled later.")
    case _:
        print("❓ Unknown priority level.")
