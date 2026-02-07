"""Main entry point for Evolution of Todo application.

This module contains the main application loop and menu dispatch logic.
"""

from task_manager import TaskManager
from cli import display_menu, display_error, display_success, prompt_for_input, display_tasks
from validators import validate_numeric_input


def main() -> None:
    """Main application loop and entry point.

    Side Effects:
        Runs infinite menu loop until user exits.
        Displays menu, captures input, dispatches to operations.
        Handles all exceptions and displays user-friendly errors.
        Exits with status code 0 on normal exit.

    Flow:
        1. Create TaskManager instance
        2. Loop:
           a. Display menu
           b. Get user choice
           c. Dispatch to operation based on choice
           d. Catch and display errors
           e. Return to step 2a
        3. Exit on choice 7
    """
    manager = TaskManager()

    while True:
        display_menu()
        choice = input().strip()

        if choice == "1":
            # Add Task - Phase 3: User Story 1
            try:
                title = prompt_for_input("Enter task title: ")
                description = prompt_for_input("Enter task description: ")
                task = manager.add_task(title, description)
                display_success(f"Task created successfully with ID: {task['id']}")
            except ValueError as e:
                display_error(f"Error: {e}")
        elif choice == "2":
            # View Task List - Phase 4: User Story 2
            tasks = manager.get_all_tasks()
            display_tasks(tasks)
        elif choice == "3":
            # Update Task - Phase 6: User Story 4
            try:
                task_id_str = prompt_for_input("Enter task ID to update: ")
                task_id = validate_numeric_input(task_id_str)

                new_title = prompt_for_input("Enter new title (or press Enter to keep current): ")
                new_description = prompt_for_input("Enter new description (or press Enter to keep current): ")

                # Convert empty strings to None to keep current values
                title_to_update = new_title if new_title.strip() else None
                description_to_update = new_description if new_description.strip() else None

                manager.update_task(task_id, title=title_to_update, description=description_to_update)
                display_success(f"Task {task_id} updated successfully.")
            except ValueError as e:
                display_error(f"Error: {e}")
            except KeyError:
                display_error(f"Error: Task ID {task_id_str} not found.")
        elif choice == "4":
            # Delete Task - Phase 7: User Story 5
            try:
                task_id_str = prompt_for_input("Enter task ID to delete: ")
                task_id = validate_numeric_input(task_id_str)
                manager.delete_task(task_id)
                display_success(f"Task {task_id} deleted successfully.")
            except ValueError as e:
                display_error(f"Error: {e}")
            except KeyError:
                display_error(f"Error: Task ID {task_id_str} not found.")
        elif choice == "5":
            # Mark Task Complete - Phase 5: User Story 3
            try:
                task_id_str = prompt_for_input("Enter task ID to mark complete: ")
                task_id = validate_numeric_input(task_id_str)
                manager.mark_task_complete(task_id)
                display_success(f"Task {task_id} marked as complete.")
            except ValueError as e:
                display_error(f"Error: {e}")
            except KeyError:
                display_error(f"Error: Task ID {task_id_str} not found.")
        elif choice == "6":
            # Mark Task Incomplete - Phase 5: User Story 3
            try:
                task_id_str = prompt_for_input("Enter task ID to mark incomplete: ")
                task_id = validate_numeric_input(task_id_str)
                manager.mark_task_incomplete(task_id)
                display_success(f"Task {task_id} marked as incomplete.")
            except ValueError as e:
                display_error(f"Error: {e}")
            except KeyError:
                display_error(f"Error: Task ID {task_id_str} not found.")
        elif choice == "7":
            # Exit - will be implemented in Phase 8
            print("Thank you for using Todo Application. Goodbye!")
            break
        else:
            display_error("Error: Invalid option. Please select a number between 1 and 7.")


if __name__ == "__main__":
    main()
