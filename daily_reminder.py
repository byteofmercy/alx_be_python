import datetime

def daily_reminder():
    now = datetime.datetime.now()
    print(f"\n📅 Today is {now.strftime('%A, %d %B %Y')}")
    
    # Step 1: Get user input
    task = input("📝 Enter your task: ")
    time_bound = input("⏰ Is this task time-bound? (yes/no): ").strip().lower()
    priority = input("🚦 Enter the priority (High/Medium/Low): ").strip().lower()
    
    # Step 2: Build base message
    message = f"\n🔔 Reminder: '{task}'"

    # Step 3: Time-bound reaction
    if time_bound == "yes":
        message += " — This task is time-sensitive! Please handle it ASAP."

    # Step 4: Match-case for priority
    match priority:
        case "high":
            message += "\n⚠️ Priority: High — Give this task immediate attention."
        case "medium":
            message += "\n🔶 Priority: Medium — Try to get it done soon."
        case "low":
            message += "\n🟢 Priority: Low — You can do this at your convenience."
        case _:
            message += "\n❓ Unknown priority entered."

    print(message)

if __name__ == "__main__":
    daily_reminder()
