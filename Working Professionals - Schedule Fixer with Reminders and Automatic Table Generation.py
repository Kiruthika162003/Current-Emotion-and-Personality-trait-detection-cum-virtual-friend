from datetime import datetime, timedelta

# Function to display the main menu
def display_menu():
    print("Welcome to Schedule Fixer!")
    print("Please select an option:")
    print("1. Add Task to Schedule")
    print("2. View Today's Schedule")
    print("3. Exit")

# Function to add a task to the schedule
def add_task_to_schedule(schedule):
    task_name = input("Enter the task name: ")
    task_time = input("Enter the task time (HH:MM AM/PM format): ")

    # Convert task_time to a datetime object
    try:
        task_time = datetime.strptime(task_time, "%I:%M %p")
    except ValueError:
        print("Invalid time format. Please use HH:MM AM/PM format.")
        return

    schedule.append((task_name, task_time))
    print("Task added to the schedule!")

# Function to view today's schedule
def view_todays_schedule(schedule):
    print("Today's Schedule:")
    if len(schedule) == 0:
        print("No tasks for today.")
    else:
        for task_name, task_time in schedule:
            print(f"{task_time.strftime('%I:%M %p')}: {task_name}")

# Function to send a reminder for a task
def send_reminder(task_name, task_time):
    reminder_time = task_time - timedelta(minutes=30)
    print(f"Reminder: You have a task '{task_name}' at {task_time.strftime('%I:%M %p')}. "
          f"Remember to prepare for it.")

# Function to generate and share the daily task table as a text message
def share_daily_task_table(schedule):
    print("Daily Task Table:")
    if len(schedule) == 0:
        print("No tasks for today.")
    else:
        for task_name, task_time in schedule:
            print(f"{task_time.strftime('%I:%M %p')}: {task_name}")

def main():
    schedule = []

    while True:
        # Display the main menu
        display_menu()

        # Simulate user selection (replace this with actual user input)
        selected_option = int(input("Enter the number of the option you want to choose (3 to exit): "))

        if selected_option == 1:
            add_task_to_schedule(schedule)
        elif selected_option == 2:
            view_todays_schedule(schedule)
        elif selected_option == 3:
            print("Exiting Schedule Fixer.")
            break
        else:
            print("Invalid option. Please select a valid option.")

    # Simulate sending reminders (replace this with actual reminder functionality)
    for task_name, task_time in schedule:
        send_reminder(task_name, task_time)

    # Simulate sharing the daily task table (replace this with actual text messaging functionality)
    share_daily_task_table(schedule)

if __name__ == "__main__":
    main()
