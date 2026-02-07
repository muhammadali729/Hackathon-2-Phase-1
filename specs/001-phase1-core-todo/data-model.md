# Data Model: Phase I Core Todo Application

**Feature**: Phase I Core Todo Application
**Branch**: `001-phase1-core-todo`
**Date**: 2025-12-31

## Overview

This document defines the data model for Phase I of the Evolution of Todo application. The model is intentionally simple, focusing on in-memory storage using Python's native data structures with no persistence layer.

## Entities

### Task

A Task represents a single todo item with a unique identifier, descriptive content, and completion status.

**Storage Format**: Python dictionary

**Schema**:
```python
{
    "id": int,          # Unique sequential identifier
    "title": str,       # Short summary of the task
    "description": str, # Detailed description of what needs to be done
    "status": str       # Current completion state: "complete" or "incomplete"
}
```

**Field Specifications**:

| Field       | Type | Required | Constraints                                          | Default     |
|-------------|------|----------|------------------------------------------------------|-------------|
| id          | int  | Yes      | Positive integer, unique, sequential, auto-generated | Auto        |
| title       | str  | Yes      | Non-empty, non-whitespace-only, any reasonable length| None        |
| description | str  | Yes      | Non-empty, non-whitespace-only, any reasonable length| None        |
| status      | str  | Yes      | Exactly "complete" or "incomplete"                   | "incomplete"|

**Example Task**:
```python
{
    "id": 1,
    "title": "Buy groceries",
    "description": "Get milk, eggs, bread, and vegetables",
    "status": "incomplete"
}
```

## Field Details

### ID Field

**Purpose**: Unique identifier for each task

**Generation Strategy**:
- Auto-generated sequentially starting from 1
- Never reused, even after task deletion
- Algorithm: `max(existing_task_ids, default=0) + 1`

**Validation**:
- Must be positive integer
- Must exist in task list for update/delete/mark operations
- Non-numeric input triggers ValueError
- Non-existent ID triggers KeyError

**Rationale**: Sequential IDs provide chronological ordering and are human-friendly for console input. Using `max()` instead of `len()` ensures correct ID generation after deletions.

### Title Field

**Purpose**: Short summary of the task for quick identification

**Characteristics**:
- Free-form text
- Any length supported by terminal display
- No maximum length enforced (trust user to keep reasonable)
- Leading/trailing whitespace trimmed automatically

**Validation**:
- Cannot be empty string
- Cannot be whitespace-only (spaces, tabs, newlines)
- Validation: `title.strip() != ""`

**Error Handling**:
- Empty/whitespace-only input raises ValueError: "Task title cannot be empty."

**Examples**:
- Valid: "Buy groceries", "Finish Q4 report", "Call dentist for appointment"
- Invalid: "", "   ", "\t\n"

### Description Field

**Purpose**: Detailed explanation of what needs to be done

**Characteristics**:
- Free-form text
- Any length supported by terminal display
- No maximum length enforced
- Can include multiple sentences or lists
- Leading/trailing whitespace trimmed automatically

**Validation**:
- Cannot be empty string
- Cannot be whitespace-only (spaces, tabs, newlines)
- Validation: `description.strip() != ""`

**Error Handling**:
- Empty/whitespace-only input raises ValueError: "Task description cannot be empty."

**Examples**:
- Valid: "Get milk, eggs, bread", "Complete financial analysis for Q4 2025", "Schedule and confirm appointment"
- Invalid: "", "   ", "\t\n"

### Status Field

**Purpose**: Track task completion state

**Valid Values**:
- `"complete"`: Task has been finished
- `"incomplete"`: Task is pending (default for new tasks)

**Type**: String literal (not boolean for future extensibility)

**State Transitions**:
```
New Task → "incomplete"
"incomplete" ↔ "complete"
```

**Validation**:
- Must be exactly "complete" or "incomplete"
- Case-sensitive
- No other values permitted

**Rationale**: String literal chosen over boolean to allow future status extensions (e.g., "in-progress", "blocked") without breaking Phase I data structure.

## Data Storage

### Storage Mechanism

**Implementation**: Python list containing task dictionaries

```python
tasks: list[dict[str, str | int]] = []
```

**Example**:
```python
[
    {"id": 1, "title": "Buy groceries", "description": "Get milk, eggs, bread", "status": "incomplete"},
    {"id": 2, "title": "Finish report", "description": "Complete Q4 analysis", "status": "complete"},
    {"id": 3, "title": "Call dentist", "description": "Schedule appointment", "status": "incomplete"}
]
```

**Characteristics**:
- In-memory only - no file or database persistence
- Data lost when application exits
- Ordered by ID (insertion order maintained)
- O(n) lookup by ID (acceptable for Phase I scale)

### Ordering

**Default Order**: Tasks displayed in creation order (ID ascending)

**Rationale**: Chronological ordering is intuitive and matches user mental model of when tasks were added.

**Implementation**: List naturally maintains insertion order; no sorting required.

## Validation Rules

### Add Task Validation

When creating a new task:
1. Title must be non-empty after stripping whitespace
2. Description must be non-empty after stripping whitespace
3. ID auto-generated (not user-provided)
4. Status automatically set to "incomplete"

### Update Task Validation

When updating an existing task:
1. Task ID must exist in task list
2. If new title provided, must be non-empty after stripping whitespace
3. If new description provided, must be non-empty after stripping whitespace
4. If title or description not provided (None), keep existing value
5. ID and status cannot be changed via update operation

### Delete Task Validation

When deleting a task:
1. Task ID must exist in task list
2. No confirmation required (per spec)
3. Task permanently removed from list

### Mark Task Validation

When marking task complete or incomplete:
1. Task ID must exist in task list
2. Status toggled to specified value
3. All other fields remain unchanged

## State Lifecycle

```
┌─────────────┐
│   New Task  │
│ (not created)│
└──────┬──────┘
       │ add_task(title, description)
       │
       ▼
┌──────────────┐
│   INCOMPLETE │ ◄─────┐
│  (default)   │       │ mark_task_incomplete()
└──────┬───────┘       │
       │               │
       │ mark_task_complete()
       │               │
       ▼               │
┌──────────────┐       │
│   COMPLETE   │───────┘
└──────┬───────┘
       │
       │ delete_task()
       ▼
┌──────────────┐
│   DELETED    │
│  (removed)   │
└──────────────┘
```

**Notes**:
- New tasks always start as "incomplete"
- Status can toggle between "complete" and "incomplete" any number of times
- Update operation does not change status
- Delete permanently removes task from system (no "archived" state in Phase I)

## Constraints and Assumptions

### Constraints

1. **No Persistence**: All data in memory, lost on exit (constitutional requirement)
2. **Single User**: No concurrent access handling needed
3. **No Relationships**: Tasks are independent, no subtasks or dependencies
4. **No Metadata**: No created_at, updated_at, or audit fields
5. **No Categories**: No tags, projects, or organizational features
6. **Sequential IDs**: Simple integer sequence, no UUIDs or complex schemes

### Assumptions

1. **Task Volume**: Expect < 1000 tasks per session (O(n) lookup acceptable)
2. **Field Length**: Terminal can display reasonable task titles/descriptions
3. **Single Session**: Users understand data is ephemeral
4. **English Language**: No internationalization in Phase I
5. **Manual Input**: All operations via interactive menu (no import/export)

## Type Definitions (Python)

```python
from typing import Literal, TypedDict

class TaskDict(TypedDict):
    """Type definition for a task dictionary."""
    id: int
    title: str
    description: str
    status: Literal["complete", "incomplete"]

# Type alias for task list
TaskList = list[TaskDict]
```

## Future Considerations (Out of Scope for Phase I)

The following are explicitly NOT included in this data model but may be considered in future phases:

- Timestamps (created_at, updated_at, completed_at)
- Task categories or tags
- Priority levels
- Due dates or reminders
- Task dependencies or subtasks
- User/owner fields (multi-user)
- Task history or audit log
- Archived/soft-delete status
- Custom fields or metadata
- Task ordering (manual reordering)

Any additions require specification update and constitute Phase II+ changes.

## Validation Summary Table

| Operation      | Field       | Validation Rule                              | Error Type  | Error Message                        |
|----------------|-------------|----------------------------------------------|-------------|--------------------------------------|
| Add Task       | title       | Non-empty, non-whitespace-only               | ValueError  | "Task title cannot be empty."        |
| Add Task       | description | Non-empty, non-whitespace-only               | ValueError  | "Task description cannot be empty."  |
| Update Task    | task_id     | Must exist in task list                      | KeyError    | "Task ID [X] not found."             |
| Update Task    | title       | If provided, non-empty, non-whitespace-only  | ValueError  | "Task title cannot be empty."        |
| Update Task    | description | If provided, non-empty, non-whitespace-only  | ValueError  | "Task description cannot be empty."  |
| Delete Task    | task_id     | Must exist in task list                      | KeyError    | "Task ID [X] not found."             |
| Mark Complete  | task_id     | Must exist in task list                      | KeyError    | "Task ID [X] not found."             |
| Mark Incomplete| task_id     | Must exist in task list                      | KeyError    | "Task ID [X] not found."             |
| All Operations | task_id     | Must be numeric                              | ValueError  | "Task ID must be a number."          |

## Conclusion

This data model provides a simple, clear foundation for Phase I implementation. It strictly adheres to constitutional constraints (in-memory only, no persistence) and specification requirements (sequential IDs, required fields, status tracking). The model is intentionally minimal, following YAGNI principles, and avoids any preparation for future phases.
