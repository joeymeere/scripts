import os
import datetime

def setup_squad_folder():
    # Get the current date
    current_date = datetime.datetime.now()
    month_day = current_date.strftime("%m-%d")  # formats the date as "Month-Day"

    # Define the folder and file names
    folder_path = f"/Users/joeymeere/Documents/Squads/Week of {month_day}"
    file_notes = "Notes.md"
    file_tasks = "Tasks.md"

    # Create the directory
    os.makedirs(folder_path, exist_ok=True)

    # Create "Notes.md" file
    with open(os.path.join(folder_path, file_notes), 'w') as file:
        file.write("")

    # Contents for "Tasks.md"
    tasks_content = """# Tasks & Priorities
    *Lowest to Highest Priority*
    1. ---

     

    | ----          | Urgent  | Not Urgent |
    | ------------- | ------- | ---------- |
    | Important     | 1. [] - | 1. [] -    |
    | Not Important | 1. [] - | 1. [] -    |
    """

    # Create "Tasks.md" file and write the content
    with open(os.path.join(folder_path, file_tasks), 'w') as file:
        file.write(tasks_content)

    print("Setup completed. Files created in:", folder_path)

# Run the function
setup_squad_folder()
