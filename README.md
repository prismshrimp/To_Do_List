Overview

This Python-based To-Do List application, implemented in to_do_list.py, allows users to manage tasks through an interactive, console-based interface. Users can add, view, mark as completed, and delete tasks, with robust input validation to ensure a seamless experience. The application uses Python lists, loops, conditionals, and functions to provide a modular and efficient task management system.

Features

Task Management: Stores tasks in a list of dictionaries, each containing a task description and status (Pending or Completed).

Add Task: Enables users to add new tasks with a description. Empty inputs are rejected.

View Tasks: Displays all tasks with their indices and status, handling empty lists gracefully.

Mark Task as Completed: Updates a task’s status to Completed based on its index.

Delete Task: Removes a task from the list using index-based selection.

Menu-Driven Interface: Offers a clear console menu with options 1-5 for user navigation.

Input Validation: Ensures valid numeric inputs for task indices and prevents empty task descriptions.

Continuous Operation: Runs in a loop until the user chooses to exit.

File Structure
to_do_list.py: The main Python script containing the To-Do List application.

README.md: This file, providing an overview and instructions for the project.



How to Run

Prerequisites: Ensure Python 3.x is installed on your system.

Download the Code: Clone or download the project folder containing to_do_list.py.



Run the Application:

Open a terminal or command prompt.

Navigate to the project folder.

Execute: python to_do_list.py.


Interact with the Menu:





Select options 1-5:


1: Add a task by entering a description.

2: View all tasks with indices and status.

3: Mark a task as completed by entering its index.

4: Delete a task by entering its index.

5: Exit the application.



Input Validation: The program prompts for valid inputs (e.g., numeric indices within range) and rejects invalid or empty entries.

Code Structure

The to_do_list.py script is organized into modular functions for clarity and maintainability:





display_menu(): Displays the interactive menu.



add_task(tasks, task_description): Adds a new task to the list.



view_tasks(tasks): Shows all tasks with indices and status.



mark_task_completed(tasks, task_index): Updates a task’s status to Completed.



delete_task(tasks, task_index): Removes a task from the list.



validate_task_index(input_str, tasks): Validates user input for task indices.



main(): Runs the main loop, handling user input and invoking appropriate functions.

Each function includes docstrings explaining its purpose, and inline comments clarify key logic. Descriptive variable names (e.g., tasks, task_description) enhance readability.

Usage Example

=== To-Do List Menu ===
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Delete Task
5. Exit
Enter your choice (1-5): 1
Enter task description: Buy groceries
Task 'Buy groceries' added successfully.

=== To-Do List Menu ===
Enter your choice (1-5): 2
=== Task List ===
1. Buy groceries - Pending

=== To-Do List Menu ===
Enter your choice (1-5): 3
=== Task List ===
1. Buy groceries - Pending
Enter task number to mark as completed: 1
Task 'Buy groceries' marked as Completed.
