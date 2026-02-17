
# --- PERSISTENCE LAYER ---

# Write code here to find the exact folder where this script file is saved
# Use the special variable that holds the full path to this script file
# Convert that path to absolute form so it always starts from the root
# Extract only the directory part from the full path
# This ensures the program always looks in the same folder as the script
# It works no matter from which folder the user runs the script from terminal
# Never hardcode full paths like C drive paths - this way it works on any computer

# Write code here to create the full path by safely joining the script folder with "tasks.json"
# Use the proper path joining method that works correctly on Windows, Mac and Linux

# Define a function called load_tasks
# Inside this function:
# Check if the data file exists on disk
# If the file does not exist, return an empty list
# Use try block to safely attempt reading the file
# Open the file for reading using context manager that auto-closes the file
# Read the content and convert from JSON text format to Python data structure
# If the JSON is corrupted or badly formatted, catch the error and return empty list

#.----[json.load - JSON text to Python list/dict]
#.----[json.dump - Python list/dict to JSON text]

# Define a function called save_tasks that takes the tasks list as input
# Open the file for writing using context manager
# Convert the Python tasks data back to JSON text format and write to file
# Use proper indentation to make the saved file nicely formatted and readable
# JSON is perfect for storing structured data like this without needing database

# --- LOGIC LAYER (The "Brain") ---

# Define function to calculate next available ID
# If the tasks list is empty, return 1 as starting ID
# Otherwise find the highest ID in all tasks and add 1 to it

# Define function to add new task - takes tasks list and task name
# Create new task dictionary with next ID, the given name, and status pending
# Add this new task to the tasks list

# Define function to delete task by ID
# Loop through all tasks
# If any task has matching ID, remove it from the list and return success
# If no match found after checking all, return failure

# Define function to mark task as done by ID
# Loop through all tasks
# If matching ID found, change its status to done and return success
# If no match, return failure

# Define function to get only pending tasks
# Return new list containing only tasks where status is pending

# Define function to get only completed tasks
# Return new list containing only tasks where status is done

# --- UI LAYER (The "Face") ---

# Create multi-line string containing the full menu with all options and letters

# Define function to print tasks in nice table format
# If no tasks provided, print message "No tasks found"
# Print the header line showing columns for ID, Task Name, Status
# Print separator line using dashes
# Loop through each task and print it with properly aligned columns
# ID column left aligned width 3 characters
# Task name column left aligned width 24 characters
# Status column normal
# Print final separator line

# --- MAIN PROGRAM (The "Glue") ---

# Define main function
# Load tasks from file at start
# Print welcome message
# Start infinite loop
# Inside loop:
# Print the menu
# Get user choice, convert to lowercase and remove extra spaces
# If user chooses add task:
# Ask for task name
# Add the task
# Save to file
# Show success message
# If user chooses show all:
# Print all tasks
# If user chooses delete:
# Ask for ID number
# Try to convert to integer
# Delete the task if found
# Save to file if successful
# Show appropriate message
# Handle error if user did not enter number
# If user chooses mark done: similar steps as delete but mark as done
# If user chooses pending: print only pending tasks
# If user chooses completed: print only completed tasks
# If user chooses exit: print goodbye and stop the loop
# If invalid choice: show error message

# Standard entry point at bottom of file
# Check if this file is being run directly
# If yes, start the main function