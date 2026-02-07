# Internal Function Contracts: Phase I Core Todo Application

**Feature**: Phase I Core Todo Application
**Branch**: `001-phase1-core-todo`
**Date**: 2025-12-31

## Overview

This document defines the contracts for all internal functions in the Phase I Todo application. Since this is a console application with no external API, these contracts serve as the interface specification between modules and guide test development.

## Module: task_manager.py

### TaskManager Class

Encapsulates all task storage and CRUD operations.

#### `__init__(self) -> None`

Initialize a new TaskManager instance with empty task storage.

**Parameters**: None

**Returns**: None

**Side Effects**:
- Creates empty task list in memory

**Example**:
```python
manager = TaskManager()
```

---

#### `add_task(self, title: str, description: str) -> dict`

Create a new task with automatically generated sequential ID and incomplete status.

**Parameters**:
- `title` (str): Task title, required, non-empty
- `description` (str): Task description, required, non-empty

**Returns**:
- `dict`: Created task dictionary containing:
  - `id` (int): Auto-generated sequential ID
  - `title` (str): Trimmed title
  - `description` (str): Trimmed description
  - `status` (str): Always "incomplete" for new tasks

**Raises**:
- `ValueError`: If title is empty or whitespace-only after stripping
- `ValueError`: If description is empty or whitespace-only after stripping

**Preconditions**:
- title and description are strings

**Postconditions**:
- New task added to internal task list
- Task ID is one greater than maximum existing ID (or 1 if list empty)
- Task status is "incomplete"
- Title and description are trimmed of leading/trailing whitespace

**Example**:
```python
manager = TaskManager()
task = manager.add_task("Buy groceries", "Get milk, eggs, bread")
# Returns: {"id": 1, "title": "Buy groceries", "description": "Get milk, eggs, bread", "status": "incomplete"}
```

---

#### `get_all_tasks(self) -> list[dict]`

Retrieve all tasks in creation order (ID ascending).

**Parameters**: None

**Returns**:
- `list[dict]`: List of task dictionaries, ordered by ID ascending
  - Empty list if no tasks exist

**Raises**: None

**Preconditions**: None

**Postconditions**:
- No changes to internal state
- Returns copy or direct reference to task list (implementation detail)

**Example**:
```python
tasks = manager.get_all_tasks()
# Returns: [{"id": 1, ...}, {"id": 2, ...}, ...]
# Or: [] if empty
```

---

#### `get_task_by_id(self, task_id: int) -> dict`

Retrieve a specific task by its unique ID.

**Parameters**:
- `task_id` (int): The ID of the task to retrieve

**Returns**:
- `dict`: Task dictionary with matching ID

**Raises**:
- `KeyError`: If task with specified ID does not exist

**Preconditions**:
- task_id is an integer

**Postconditions**:
- No changes to internal state

**Example**:
```python
task = manager.get_task_by_id(1)
# Returns: {"id": 1, "title": "Buy groceries", ...}

task = manager.get_task_by_id(999)
# Raises: KeyError
```

---

#### `update_task(self, task_id: int, title: str | None = None, description: str | None = None) -> dict`

Update a task's title and/or description while preserving ID and status.

**Parameters**:
- `task_id` (int): ID of task to update
- `title` (str | None): New title, or None to keep current title
- `description` (str | None): New description, or None to keep current description

**Returns**:
- `dict`: Updated task dictionary with all fields

**Raises**:
- `KeyError`: If task with specified ID does not exist
- `ValueError`: If provided title is empty or whitespace-only after stripping
- `ValueError`: If provided description is empty or whitespace-only after stripping

**Preconditions**:
- task_id is an integer
- At least one of title or description must be provided (not both None)

**Postconditions**:
- Task title updated if title parameter provided
- Task description updated if description parameter provided
- Task ID and status remain unchanged
- Provided fields are trimmed of leading/trailing whitespace

**Example**:
```python
# Update title only
task = manager.update_task(1, title="Buy groceries and snacks", description=None)

# Update description only
task = manager.update_task(1, title=None, description="Get milk, eggs, bread, and chips")

# Update both
task = manager.update_task(1, title="Shopping", description="Weekly grocery run")
```

---

#### `delete_task(self, task_id: int) -> None`

Permanently remove a task from the task list.

**Parameters**:
- `task_id` (int): ID of task to delete

**Returns**: None

**Raises**:
- `KeyError`: If task with specified ID does not exist

**Preconditions**:
- task_id is an integer

**Postconditions**:
- Task with specified ID removed from internal task list
- Task cannot be retrieved or operated on after deletion
- ID is not reused for future tasks

**Example**:
```python
manager.delete_task(1)
# Task with ID 1 is removed permanently

manager.delete_task(999)
# Raises: KeyError
```

---

#### `mark_task_complete(self, task_id: int) -> dict`

Change a task's status to "complete".

**Parameters**:
- `task_id` (int): ID of task to mark complete

**Returns**:
- `dict`: Updated task dictionary with status="complete"

**Raises**:
- `KeyError`: If task with specified ID does not exist

**Preconditions**:
- task_id is an integer

**Postconditions**:
- Task status changed to "complete"
- All other fields (ID, title, description) unchanged
- Can be called on already-complete tasks (idempotent)

**Example**:
```python
task = manager.mark_task_complete(1)
# Returns: {"id": 1, ..., "status": "complete"}
```

---

#### `mark_task_incomplete(self, task_id: int) -> dict`

Change a task's status to "incomplete".

**Parameters**:
- `task_id` (int): ID of task to mark incomplete

**Returns**:
- `dict`: Updated task dictionary with status="incomplete"

**Raises**:
- `KeyError`: If task with specified ID does not exist

**Preconditions**:
- task_id is an integer

**Postconditions**:
- Task status changed to "incomplete"
- All other fields (ID, title, description) unchanged
- Can be called on already-incomplete tasks (idempotent)

**Example**:
```python
task = manager.mark_task_incomplete(1)
# Returns: {"id": 1, ..., "status": "incomplete"}
```

---

## Module: validators.py

### Input Validation Functions

#### `validate_non_empty_string(value: str, field_name: str) -> str`

Validate that a string is non-empty and contains non-whitespace characters.

**Parameters**:
- `value` (str): String to validate
- `field_name` (str): Name of field for error messages (e.g., "title", "description")

**Returns**:
- `str`: Trimmed string value

**Raises**:
- `ValueError`: If value is empty or whitespace-only, message includes field_name

**Preconditions**:
- value is a string

**Postconditions**:
- Returned value has leading/trailing whitespace removed
- Returned value contains at least one non-whitespace character

**Example**:
```python
title = validate_non_empty_string("  Buy groceries  ", "title")
# Returns: "Buy groceries"

validate_non_empty_string("   ", "description")
# Raises: ValueError("Task description cannot be empty.")
```

---

#### `validate_numeric_input(value: str) -> int`

Validate and convert user input to an integer task ID.

**Parameters**:
- `value` (str): User input string to validate

**Returns**:
- `int`: Parsed integer value

**Raises**:
- `ValueError`: If value cannot be converted to integer

**Preconditions**:
- value is a string

**Postconditions**:
- Returned value is a valid integer

**Example**:
```python
task_id = validate_numeric_input("5")
# Returns: 5

validate_numeric_input("abc")
# Raises: ValueError("Task ID must be a number.")
```

---

## Module: cli.py

### User Interface Functions

#### `display_menu() -> None`

Display the main menu to the user.

**Parameters**: None

**Returns**: None

**Side Effects**:
- Prints menu to stdout exactly as specified in spec

**Preconditions**: None

**Postconditions**:
- Menu displayed on console

**Output Format**:
```
===== Todo Application =====
1. Add Task
2. View Task List
3. Update Task
4. Delete Task
5. Mark Task Complete
6. Mark Task Incomplete
7. Exit

Select an option (1-7):
```

---

#### `display_tasks(tasks: list[dict]) -> None`

Display all tasks in formatted list.

**Parameters**:
- `tasks` (list[dict]): List of task dictionaries to display

**Returns**: None

**Side Effects**:
- Prints formatted task list to stdout
- If tasks empty, prints "No tasks found. Your task list is empty."

**Preconditions**:
- tasks is a list (may be empty)
- Each task dict contains id, title, description, status

**Postconditions**:
- Task list displayed on console in spec format

**Output Format (non-empty)**:
```
===== Task List (3 tasks) =====
[1] Title: Buy groceries
    Description: Get milk, eggs, bread
    Status: incomplete

[2] Title: Finish report
    Description: Complete Q4 analysis
    Status: complete
===============================
```

**Output Format (empty)**:
```
No tasks found. Your task list is empty.
```

---

#### `prompt_for_input(prompt_text: str) -> str`

Display prompt and capture user input.

**Parameters**:
- `prompt_text` (str): Text to display as prompt

**Returns**:
- `str`: User input string (may be empty)

**Side Effects**:
- Prints prompt to stdout
- Reads input from stdin

**Preconditions**:
- prompt_text is a string

**Postconditions**:
- User input captured and returned

**Example**:
```python
title = prompt_for_input("Enter task title: ")
# User sees: "Enter task title: "
# Returns: whatever user types
```

---

#### `display_success(message: str) -> None`

Display success message to user.

**Parameters**:
- `message` (str): Success message text

**Returns**: None

**Side Effects**:
- Prints message to stdout

**Preconditions**:
- message is a string

**Postconditions**:
- Message displayed on console

**Example**:
```python
display_success("Task created successfully with ID: 1")
# Prints: "Task created successfully with ID: 1"
```

---

#### `display_error(message: str) -> None`

Display error message to user.

**Parameters**:
- `message` (str): Error message text (should include "Error:" prefix)

**Returns**: None

**Side Effects**:
- Prints message to stdout (or stderr - implementation detail)

**Preconditions**:
- message is a string

**Postconditions**:
- Error message displayed on console

**Example**:
```python
display_error("Error: Task ID 999 not found.")
# Prints: "Error: Task ID 999 not found."
```

---

## Module: main.py

### Application Entry Point

#### `main() -> None`

Main application loop and entry point.

**Parameters**: None

**Returns**: None

**Side Effects**:
- Runs infinite menu loop until user exits
- Displays menu, captures input, dispatches to operations
- Handles all exceptions and displays user-friendly errors
- Exits with status code 0 on normal exit

**Preconditions**: None

**Postconditions**:
- Application terminates when user selects exit option
- All errors caught and displayed gracefully

**Flow**:
1. Create TaskManager instance
2. Loop:
   a. Display menu
   b. Get user choice
   c. Dispatch to operation based on choice
   d. Catch and display errors
   e. Return to step 2a
3. Exit on choice 7

---

## Error Handling Contract

All functions follow these error handling principles:

1. **ValueError**: Used for invalid input values (empty strings, non-numeric, whitespace-only)
2. **KeyError**: Used for non-existent task IDs
3. **Clear Messages**: All errors include user-friendly explanation
4. **No Crashes**: Main loop catches all exceptions and returns to menu
5. **Specification Compliance**: Error messages match spec exactly

## Thread Safety

**Not Required**: Phase I is single-user, single-threaded console application. No concurrent access handling needed.

## Performance Expectations

- Add task: O(n) for ID generation (acceptable for Phase I scale)
- Get all tasks: O(1) list return
- Get task by ID: O(n) linear search (acceptable for < 1000 tasks)
- Update task: O(n) to find, O(1) to update
- Delete task: O(n) to find and remove
- Mark complete/incomplete: O(n) to find, O(1) to update

All operations complete in < 1 second for expected task volumes.

## Testing Contract

Each function contract above defines:
- **Happy path**: Normal operation with valid inputs
- **Error cases**: Expected exceptions with specific inputs
- **Edge cases**: Boundary conditions (empty lists, first/last items, etc.)
- **Idempotency**: Where applicable (mark operations)

Tests should verify:
1. Return values match contract
2. Exceptions raised as specified
3. Postconditions satisfied
4. No unintended side effects
