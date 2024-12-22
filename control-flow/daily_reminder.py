# daily_reminder.py

# Prompt for a Single Task:
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Validate priority input
if priority not in ("high", "medium", "low"):
    print("Invalid priority input. Please enter 'high', 'medium', or 'low'.")
    exit()

# Validate time_bound input
if time_bound not in ("yes", "no"):
    print("Invalid input for time sensitivity. Please enter 'yes' or 'no'.")
    exit()

# Match case for priority
match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"

# Modify message based on time sensitivity
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."

# Print the reminder
print(f"\nReminder: {message}")
