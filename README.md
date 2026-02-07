# Evolution of Todo - Phase I

[![Python Version](https://img.shields.io/badge/python-3.13%2B-blue)](https://www.python.org/downloads/) [![License](https://img.shields.io/badge/license-MIT-green)](LICENSE) [![Development Status](https://img.shields.io/badge/status-Phase%20I%20Complete-success)](https://github.com)

A professional, console-based task management application for managing your daily tasks. Phase I provides core functionality with in-memory storage, perfect for quick task tracking during your work sessions.

---

## Table of Contents

- [Overview](#overview)
- [What is Phase I?](#what-is-phase-i)
- [Features](#features)
- [System Requirements](#system-requirements)
- [Installation & Setup](#installation--setup)
- [How to Run](#how-to-run)
- [Usage Guide](#usage-guide)
- [Important Notes](#important-notes)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Overview

**Evolution of Todo** is a simple, console-based task management application that helps you organize and track your daily tasks. This is Phase I - a foundational version that stores tasks in memory, making it perfect for short-term task tracking during active work sessions.

### What You Can Do

- Add new tasks with titles and descriptions
- View all your tasks in an organized list
- Update task details when plans change
- Mark tasks as complete or incomplete
- Delete tasks you no longer need
- All operations through an easy-to-use numbered menu

---

## What is Phase I?

Phase I is the **in-memory console-based version** of Evolution of Todo. This means:

**In-Memory Storage**
- All your tasks are stored in the computer's RAM (memory)
- Fast and instant response for all operations
- No files or databases needed
- Perfect for temporary task tracking

**Console-Based Interface**
- Runs in your terminal or command prompt
- Simple numbered menu (1-7) for all operations
- Clear prompts guide you through each action
- No graphical interface - just text-based interaction

**Key Characteristic**
- **Data is temporary**: When you close the application, all tasks are lost
- This is intentional for Phase I - designed for session-based task tracking
- Think of it as a "scratchpad" for your daily tasks

---

## Features

### Core Operations

| Feature | What It Does |
|---------|--------------|
| **Add Task** | Create new tasks with a title and description |
| **View Tasks** | See all your tasks in a formatted list |
| **Update Task** | Change the title or description of existing tasks |
| **Delete Task** | Remove tasks you no longer need |
| **Mark Complete** | Mark tasks as done |
| **Mark Incomplete** | Unmark tasks (reopen them) |
| **Exit** | Close the application |

---

## Installation & Setup

### Step 1: Get the Application

Clone the repository to your local machine:
```bash
git clone <repository-url>
cd Todo-In-Memory-Python-Console-App
```

### Step 2: Verify Files

Make sure you have these files in your project folder:
- `src/main.py` - The main application file
- `src/task_manager.py` - Task management logic
- `src/cli.py` - Display functions
- `src/validators.py` - Input validation

### Step 3: Test Python Installation

Open your terminal/command prompt in the project folder and run:

```bash
python --version
```

Confirm it shows Python 3.13 or higher.

---

## How to Run

### Starting the Application

1. **Open Terminal/Command Prompt**
   - **Windows**: Press `Win + R`, type `cmd`, press Enter
   - **macOS**: Press `Cmd + Space`, type `terminal`, press Enter
   - **Linux**: Press `Ctrl + Alt + T`

2. **Navigate to Project Folder**
   ```bash
   cd path/to/Todo-In-Memory-Python-Console-App
   ```
   Replace `path/to/` with your actual folder location.

3. **Run the Application**
   ```bash
   python src/main.py
   ```

4. **You Should See the Main Menu**
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

### Stopping the Application

To exit, select option `7` from the main menu, or press `Ctrl + C` to force quit.

**Remember**: All tasks will be lost when you exit!

---

## Usage Guide

### Main Menu

When you run the application, you'll see a numbered menu with 7 options. Simply type the number and press Enter.

### 1. Add Task

**What it does**: Creates a new task

**How to use**:
1. Type `1` and press Enter
2. Enter a title when prompted (e.g., "Buy groceries")
3. Enter a description when prompted (e.g., "Milk, eggs, bread")
4. Task is created with a unique ID

**Example**:
```
Select an option (1-7): 1
Enter task title: Buy groceries
Enter task description: Get milk, eggs, bread, and vegetables
Task created successfully with ID: 1
```

**Rules**:
- Title cannot be empty
- Description cannot be empty
- Both are required

---

### 2. View Task List

**What it does**: Shows all your tasks

**How to use**:
1. Type `2` and press Enter
2. All tasks are displayed with their details

**Example with tasks**:
```
Select an option (1-7): 2

===== Task List (2 tasks) =====
[1] Title: Buy groceries
    Description: Get milk, eggs, bread, and vegetables
    Status: incomplete

[2] Title: Finish report
    Description: Complete Q4 financial analysis
    Status: complete
===============================
```

**Example with no tasks**:
```
Select an option (1-7): 2
No tasks found. Your task list is empty.
```

---

### 3. Update Task

**What it does**: Changes a task's title or description

**How to use**:
1. Type `3` and press Enter
2. Enter the task ID (the number in brackets)
3. Enter new title (or press Enter to keep current)
4. Enter new description (or press Enter to keep current)

**Example**:
```
Select an option (1-7): 3
Enter task ID to update: 1
Enter new title (or press Enter to keep current): Buy groceries and snacks
Enter new description (or press Enter to keep current):
Task 1 updated successfully.
```

**Tip**: Press Enter without typing anything to skip updating that field.

---

### 4. Delete Task

**What it does**: Permanently removes a task

**How to use**:
1. Type `4` and press Enter
2. Enter the task ID you want to delete
3. Task is immediately removed

**Example**:
```
Select an option (1-7): 4
Enter task ID to delete: 2
Task 2 deleted successfully.
```

**Warning**: There's no undo! Once deleted, the task is gone.

---

### 5. Mark Task Complete

**What it does**: Marks a task as done

**How to use**:
1. Type `5` and press Enter
2. Enter the task ID
3. Status changes to "complete"

**Example**:
```
Select an option (1-7): 5
Enter task ID to mark complete: 1
Task 1 marked as complete.
```

---

### 6. Mark Task Incomplete

**What it does**: Marks a task as not done (reopens it)

**How to use**:
1. Type `6` and press Enter
2. Enter the task ID
3. Status changes to "incomplete"

**Example**:
```
Select an option (1-7): 6
Enter task ID to mark incomplete: 1
Task 1 marked as incomplete.
```

**Use cases**:
- Accidentally marked wrong task as complete
- Task needs to be done again
- Reopening a task for additional work

---

### 7. Exit

**What it does**: Closes the application

**How to use**:
1. Type `7` and press Enter
2. Application displays goodbye message and closes

**Example**:
```
Select an option (1-7): 7
Thank you for using Todo Application. Goodbye!
```

**Remember**: All your tasks will be lost when you exit!

---

## Phase I Scope

This is what Phase I includes:

✅ **Included**:
- All 7 menu operations (Add, View, Update, Delete, Mark Complete/Incomplete, Exit)
- In-memory task storage
- Input validation
- Error handling
- Task ID management
- Status tracking (complete/incomplete)

❌ **Not Included** (may come in future phases):
- Data persistence (saving to files/database)
- Search or filter functionality
- Task categories or tags
- Due dates or priorities
- Undo/redo operations
- Multi-user support
- Import/export functionality
- Recurring tasks
- Task dependencies

Phase I focuses on core functionality only.

---

## Quick Reference

### Command Cheat Sheet

```
Starting the app:
  python src/main.py

Main Menu Options:
  1 - Add Task
  2 - View Task List
  3 - Update Task
  4 - Delete Task
  5 - Mark Task Complete
  6 - Mark Task Incomplete
  7 - Exit

Emergency Exit:
  Ctrl + C (force quit)
```

### File Locations

```
Project Root/
├── src/
│   ├── main.py          ← Run this file
│   ├── task_manager.py
│   ├── cli.py
│   └── validators.py
└── README.md            ← This file
```

### Tips

- View tasks first (option 2) before updating/deleting
- Task IDs are shown in brackets: [1], [2], [3]
- Press Enter to skip fields when updating
- Keep app running to preserve your tasks
- Exit with option 7 for clean shutdown

---

## Project Status

**Current Version**: Phase I (v0.1.0)
**Status**: Complete and Ready to Use
**Last Updated**: December 31, 2025

---

**Simple. Fast. Temporary. Perfect for quick task tracking.**

*Evolution of Todo - Phase I: Your in-memory task companion*
"# Hackathon-2-Phase-1" 
"# Hackathon-2-Phase-1" 
