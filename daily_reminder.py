import datetime

def daily_reminder():
    now = datetime.datetime.now()
    print(f"Good day! This is your reminder for {now.strftime('%A, %d %B %Y')}.")

if __name__ == "__main__":
    daily_reminder()
