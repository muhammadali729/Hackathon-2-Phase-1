"""CLI helper functions for Evolution of Todo application.

This module provides user interface functions for displaying menus,
prompts, and formatted output.
"""


def display_menu() -> None:
    """Display the main menu to the user.

    Side Effects:
        Prints menu to stdout exactly as specified in spec.

    Example:
        >>> display_menu()
        ===== Todo Application =====
        1. Add Task
        2. View Task List
        3. Update Task
        4. Delete Task
        5. Mark Task Complete
        6. Mark Task Incomplete
        7. Exit
        <BLANKLINE>
        Select an option (1-7):
    """
    print("===== Todo Application =====")
    print("1. Add Task")
    print("2. View Task List")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task Complete")
    print("6. Mark Task Incomplete")
    print("7. Exit")
    print()
    print("Select an option (1-7): ", end="")


def display_success(message: str) -> None:
    """Display success message to user.

    Args:
        message: Success message text.

    Side Effects:
        Prints message to stdout.

    Example:
        >>> display_success("Task created successfully with ID: 1")
        Task created successfully with ID: 1
    """
    print(message)


def display_error(message: str) -> None:
    """Display error message to user.

    Args:
        message: Error message text (should include "Error:" prefix).

    Side Effects:
        Prints message to stdout.

    Example:
        >>> display_error("Error: Task ID 999 not found.")
        Error: Task ID 999 not found.
    """
    print(message)


def prompt_for_input(prompt_text: str) -> str:
    """Display prompt and capture user input.

    Args:
        prompt_text: Text to display as prompt.

    Returns:
        User input string (may be empty).

    Side Effects:
        Prints prompt to stdout and reads input from stdin.

    Example:
        >>> prompt_for_input("Enter task title: ")  # doctest: +SKIP
        Enter task title: Buy groceries
        'Buy groceries'
    """
    return input(prompt_text)


def display_tasks(tasks: list[dict]) -> None:
    """Display all tasks in formatted list.

    Args:
        tasks: List of task dictionaries to display.

    Side Effects:
        Prints formatted task list to stdout.
        If tasks empty, prints "No tasks found. Your task list is empty."

    Example:
        >>> tasks = [
        ...     {"id": 1, "title": "Buy groceries", "description": "Get milk, eggs, bread", "status": "incomplete"},
        ...     {"id": 2, "title": "Finish report", "description": "Complete Q4 analysis", "status": "complete"}
        ... ]
        >>> display_tasks(tasks)
        ===== Task List (2 tasks) =====
        [1] Title: Buy groceries
            Description: Get milk, eggs, bread
            Status: incomplete
        <BLANKLINE>
        [2] Title: Finish report
            Description: Complete Q4 analysis
            Status: complete
        ===============================
        >>> display_tasks([])
        No tasks found. Your task list is empty.
    """
    if not tasks:
        print("No tasks found. Your task list is empty.")
        return

    # Display header with count
    print(f"===== Task List ({len(tasks)} tasks) =====")

    # Display each task
    for task in tasks:
        print(f"[{task['id']}] Title: {task['title']}")
        print(f"    Description: {task['description']}")
        print(f"    Status: {task['status']}")
        print()  # Blank line between tasks

    # Display footer
    print("=" * 31)
