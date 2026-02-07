# Quickstart Guide: Phase I Core Todo Application

**Feature**: Phase I Core Todo Application
**Branch**: `001-phase1-core-todo`
**Last Updated**: 2025-12-31

## What is This?

The Evolution of Todo application is a simple, console-based task management tool. You can add tasks, view your task list, update tasks, delete tasks, and mark them as complete or incomplete.

**Important**: All data is stored in memory only. When you exit the application, all your tasks are lost.

## Prerequisites

- Python 3.13 or higher installed on your system
- Terminal or command prompt access

## Installation

No installation required beyond Python itself. This is a simple script that runs directly.

## Quick Start

### Running the Application

1. Open your terminal or command prompt
2. Navigate to the project directory
3. Run the application:

```bash
python src/main.py
```

4. You'll see the main menu:

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

### Basic Workflow

**Step 1**: Add your first task
- Select option `1`
- Enter a title when prompted (e.g., "Buy groceries")
- Enter a description when prompted (e.g., "Get milk, eggs, and bread")
- You'll see: "Task created successfully with ID: 1"

**Step 2**: View your tasks
- Select option `2`
- You'll see your task displayed with its ID, title, description, and status

**Step 3**: Mark a task complete
- Select option `5`
- Enter the task ID (e.g., `1`)
- You'll see: "Task 1 marked as complete."

**Step 4**: Exit the application
- Select option `7`
- You'll see: "Thank you for using Todo Application. Goodbye!"

## Feature Guide

### 1. Add Task

**What it does**: Creates a new task with a title and description

**How to use**:
1. Select option `1` from the main menu
2. Enter a task title when prompted
3. Enter a task description when prompted
4. Task is created with a unique ID and status "incomplete"

**Example**:
```
Select an option (1-7): 1
Enter task title: Buy groceries
Enter task description: Get milk, eggs, bread, and vegetables
Task created successfully with ID: 1
```

**Tips**:
- Keep titles short and descriptive
- Use descriptions for details about what needs to be done
- Both title and description are required (cannot be empty)

---

### 2. View Task List

**What it does**: Displays all your tasks in creation order

**How to use**:
1. Select option `2` from the main menu
2. All tasks are displayed with their details

**Example (with tasks)**:
```
Select an option (1-7): 2

===== Task List (3 tasks) =====
[1] Title: Buy groceries
    Description: Get milk, eggs, bread
    Status: incomplete

[2] Title: Finish report
    Description: Complete Q4 financial analysis
    Status: complete

[3] Title: Call dentist
    Description: Schedule cleaning appointment
    Status: incomplete
===============================
```

**Example (empty list)**:
```
Select an option (1-7): 2
No tasks found. Your task list is empty.
```

**Tips**:
- Tasks are always shown in the order they were created
- Task IDs never change, even if you delete tasks
- Use this to find the ID of tasks you want to update, delete, or mark

---

### 3. Update Task

**What it does**: Change the title and/or description of an existing task

**How to use**:
1. Select option `3` from the main menu
2. Enter the task ID you want to update
3. Enter new title (or press Enter to keep current)
4. Enter new description (or press Enter to keep current)

**Example (update both)**:
```
Select an option (1-7): 3
Enter task ID to update: 1
Enter new title (or press Enter to keep current): Buy groceries and snacks
Enter new description (or press Enter to keep current): Get milk, eggs, bread, vegetables, and chips
Task 1 updated successfully.
```

**Example (update title only)**:
```
Select an option (1-7): 3
Enter task ID to update: 1
Enter new title (or press Enter to keep current): Weekly shopping
Enter new description (or press Enter to keep current): [press Enter]
Task 1 updated successfully.
```

**Tips**:
- Use View Task List (option 2) to find the task ID
- Press Enter without typing anything to keep the current value
- The task's completion status is not affected by updates

---

### 4. Delete Task

**What it does**: Permanently removes a task from your list

**How to use**:
1. Select option `4` from the main menu
2. Enter the task ID you want to delete
3. Task is immediately and permanently removed

**Example**:
```
Select an option (1-7): 4
Enter task ID to delete: 2
Task 2 deleted successfully.
```

**Warning**:
- There is no confirmation prompt
- Deleted tasks cannot be recovered
- The task ID is not reused for new tasks

---

### 5. Mark Task Complete

**What it does**: Changes a task's status to "complete"

**How to use**:
1. Select option `5` from the main menu
2. Enter the task ID you want to mark complete
3. Task status changes to "complete"

**Example**:
```
Select an option (1-7): 5
Enter task ID to mark complete: 1
Task 1 marked as complete.
```

**Tips**:
- You can mark an already-complete task as complete (no error)
- Use this when you've finished a task
- You can still update or delete completed tasks

---

### 6. Mark Task Incomplete

**What it does**: Changes a task's status to "incomplete"

**How to use**:
1. Select option `6` from the main menu
2. Enter the task ID you want to mark incomplete
3. Task status changes to "incomplete"

**Example**:
```
Select an option (1-7): 6
Enter task ID to mark incomplete: 1
Task 1 marked as incomplete.
```

**Tips**:
- Use this if you accidentally marked a task complete
- Or if a previously completed task needs to be done again

---

### 7. Exit

**What it does**: Closes the application

**How to use**:
1. Select option `7` from the main menu
2. Application exits with a goodbye message

**Example**:
```
Select an option (1-7): 7
Thank you for using Todo Application. Goodbye!
```

**Remember**: All your tasks will be lost when you exit!

---

## Error Messages

The application provides helpful error messages when something goes wrong:

| Error Message | What It Means | How to Fix |
|---------------|---------------|------------|
| "Error: Invalid option. Please select a number between 1 and 7." | You entered something other than 1-7 in the main menu | Enter a number from 1 to 7 |
| "Error: Task ID X not found." | You tried to operate on a task that doesn't exist | Use View Task List to see available IDs |
| "Error: Task ID must be a number." | You entered non-numeric input when asked for a task ID | Enter a numeric task ID (e.g., 1, 2, 3) |
| "Error: Task title cannot be empty." | You tried to create/update a task with an empty title | Provide a non-empty title |
| "Error: Task description cannot be empty." | You tried to create/update a task with an empty description | Provide a non-empty description |

## Common Workflows

### Daily Task Management

```
Morning:
1. Run application
2. Add tasks for the day (option 1)
3. View all tasks (option 2)

Throughout the day:
4. Mark tasks complete as you finish them (option 5)
5. View tasks to see what's left (option 2)

End of day:
6. Review completed vs incomplete tasks (option 2)
7. Exit application (option 7)

Next day:
8. Start fresh - all previous tasks are gone
```

### Weekly Planning

```
1. Run application
2. Add all tasks for the week (option 1)
3. Work through tasks, marking complete (option 5)
4. Update task details as plans change (option 3)
5. Delete tasks that are no longer relevant (option 4)
6. Keep application running all week
7. Exit at end of week
```

## Tips and Best Practices

**For Titles**:
- Keep them under 50 characters for easy scanning
- Use action verbs: "Buy", "Call", "Finish", "Review"
- Be specific: "Buy groceries" not just "Shopping"

**For Descriptions**:
- Add details that will help you remember what to do
- Include quantities, names, or other specifics
- Keep it concise but complete

**For Managing Tasks**:
- View your list regularly to stay on track
- Mark tasks complete as soon as you finish them
- Delete tasks you won't do rather than leaving them incomplete
- Update tasks if plans change instead of creating duplicates

**For Long Sessions**:
- Remember: if you close the terminal or application crashes, all data is lost
- For important tasks, keep a backup elsewhere
- This tool is best for temporary, session-based task tracking

## Limitations (Phase I)

**What This Application Does NOT Do**:
- ❌ Save tasks to a file or database
- ❌ Remember tasks after you exit
- ❌ Sort or filter tasks
- ❌ Search tasks
- ❌ Categorize or tag tasks
- ❌ Set due dates or priorities
- ❌ Support multiple users
- ❌ Provide undo/redo functionality
- ❌ Import or export task lists

These features may come in future phases!

## Troubleshooting

**Problem**: Application doesn't start
- **Solution**: Check that Python 3.13+ is installed (`python --version`)
- **Solution**: Make sure you're in the correct directory
- **Solution**: Verify the file path is correct: `src/main.py`

**Problem**: Can't find task ID
- **Solution**: Use option 2 (View Task List) to see all task IDs
- **Solution**: Task IDs are the numbers in brackets like [1], [2], [3]

**Problem**: All my tasks disappeared
- **Solution**: This is expected behavior when the application exits
- **Solution**: Phase I does not save data - use it for temporary task tracking only

**Problem**: Error messages appear on every action
- **Solution**: Make sure you're entering valid input (numbers for IDs, non-empty text for titles/descriptions)
- **Solution**: Read the error message carefully - it explains what went wrong

## Getting Help

For issues, questions, or feedback:
1. Review this quickstart guide
2. Check the error message (they're designed to be helpful)
3. Refer to the feature specification for detailed requirements
4. Contact the development team or file an issue in the project repository

## Keyboard Shortcuts

None available in Phase I - all interaction is menu-driven.

## Next Steps

Once you're comfortable with the basic features:
- Try managing a full day of tasks
- Experiment with updating and deleting tasks
- See how the status changes affect your workflow

Remember: This is Phase I - a minimal viable product focused on core functionality. Future phases will add persistence, advanced features, and more!

---

**Happy task tracking!** 🎯
