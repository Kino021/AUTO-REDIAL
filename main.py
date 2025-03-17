import time

# Function to simulate a task (e.g., print a message)
def perform_task():
    print("Task is running...")

# Simple scheduler function using time.sleep() for intervals
def schedule_task(interval_seconds):
    while True:
        print(f"Waiting for {interval_seconds} seconds before performing the task...")
        time.sleep(interval_seconds)  # Wait for the interval time
        perform_task()  # Perform the task after the wait time

# Main function to simulate user input trigger for task scheduling
def main():
    print("Simple Task Automation")
    try:
        # Ask user for the interval time in seconds
        interval = int(input("Enter the interval in seconds to repeat the task: "))
        print(f"Automation will start now, repeating every {interval} seconds.")
        
        # Start scheduling the task with the given interval
        schedule_task(interval)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Run the main function
if __name__ == "__main__":
    main()
