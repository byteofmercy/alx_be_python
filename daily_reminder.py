from datetime import datetime

# Step 1: Get today's date
today = datetime.now().strftime("%A, %d %B %Y")
print(f"📅 Today is {today}")

# Step 2: Ask for task
task = input("📝 Enter your task: ").strip()

# Step 3: Ask if time-bound
time_bound = input("⏰ Is this task time-bound? (yes/no): ").strip().lower()

# Step 4: Ask for priority
priority = input("🚦 Enter the priority (High/Medium/Low): ").strip().lower()

# Step 5: Build reminder
reminder = f"🔔 Reminder: '{task}'"

if time_bound == "yes":
    reminder += " — This task is time-sensitive! Please handle it ASAP."
else:
    reminder += " — This task can be scheduled flexibly."

print("\n" + reminder)

# Step 6: Priority feedback using match-case (Python 3.10+)
match priority:
    case "high":
        print("⚠️ Priority: High — Give this task immediate attention.")
    case "medium":
        print("✅ Priority: Medium — Plan this task soon.")
    case "low":
        print("🕓 Priority: Low — Can be done at your convenience.")
    case _:
        print("❓ Priority not recognized.")
