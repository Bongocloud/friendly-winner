"""
-----------------------------------------------------------------------
ASSIGNMENT 11A REVISED: THE BUG TRACKING LOG
-----------------------------------------------------------------------
[ ] 1. Program uses a while loop to keep asking for bugs.
[ ] 2. Uses the datetime module to get a timestamp format.
[ ] 3. Stores the timestamp, file name, description, and priority in a dictionary.
[ ] 4. Uses `with open("bug_log.txt", "a")` to append to the file safely.
[ ] 5. The bug_log.txt file is formatted neatly with newlines.
-----------------------------------------------------------------------
"""
#Import datetime for timestamp
import datetime

# Get information about the bug
def bug_data():
    file_name = input(f"Enter file name: ")

    error_description = input(f"What is the error description: ")

#Trap user till they give an answer
    priority_level = ""
    while priority_level == "":
        priority_level = (input(f"What is the priority level (High, Medium, Low): ")).strip().capitalize()

    return file_name, priority_level, error_description

def file_write(error_info):
     with open("bug_log.txt", "a") as file:
        file.write(f"---Bug Log---\n")
        file.write(f"{error_info['Time']}\n")
        file.write(f"File: {error_info['File Name']}\n")
        file.write(f"Status: {error_info['Error Description']}\n")
        file.write(f"Priority: {error_info['Priority Level']}\n")
     
def main():
    
    # While loop = log (keeps loop going)
    continue_program = input(f"Enter 'log' to record a bug, or 'quit' to stop: ").strip().lower()
    
    while continue_program == "log":

        timestamp = datetime.datetime.now()

        # Unpacking previous bug_data values in main under new names
        name, priority, desc = bug_data()
        #Using new names for dictionary
        error_info = {
        "Time" : timestamp,
        "File Name" : name,
        "Error Description" : desc,
        "Priority Level" : priority
        }

        file_write(error_info=error_info)

        continue_program = input(f"\nEnter 'log' to record a bug, or 'quit' to stop: ").strip().lower()
    
    print("Bug log updated!")

main()