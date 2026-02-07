# Implementation Plan: Phase I Core Todo Application

**Branch**: `001-phase1-core-todo` | **Date**: 2025-12-31 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-phase1-core-todo/spec.md`

## Summary

Phase I implements a console-based todo application with five core operations: add, view, update, delete, and mark tasks complete/incomplete. All data is stored in-memory using Python's built-in data structures. The application runs as a single-user, menu-driven CLI program with no persistence between sessions. Technical approach uses a simple list-based storage with sequential ID generation and a command-loop pattern for the CLI.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: None (Python standard library only)
**Storage**: In-memory list of dictionaries (no persistence)
**Testing**: pytest with 80% coverage minimum
**Target Platform**: Console/Terminal (Windows, Linux, macOS)
**Project Type**: Single console application
**Performance Goals**: <1 second response for all operations, support 100+ tasks in memory
**Constraints**: No file I/O, no databases, no external services, single-user only
**Scale/Scope**: Single Python file initially, may refactor to modules if exceeds 300 lines

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Phase I Constraints (from Constitution)

✅ **PASS**: Python 3.13+ meets constitutional minimum of Python 3.11+
✅ **PASS**: In-memory storage only - no persistence mechanisms
✅ **PASS**: Standard library only - no third-party dependencies
✅ **PASS**: pytest for testing as required by constitution
✅ **PASS**: Type hints and docstrings planned for all public functions
✅ **PASS**: No global mutable state (except task storage encapsulated in class)
✅ **PASS**: No future-phase features or abstractions
✅ **PASS**: Simplicity principle - flat structure, no over-engineering

### Code Quality Gates

✅ **PASS**: Maximum cyclomatic complexity 10 per function (enforced via pytest-complexity)
✅ **PASS**: Test coverage minimum 80% (enforced via pytest-cov)
✅ **PASS**: Type hints for all function signatures
✅ **PASS**: Google-style docstrings for all public functions and classes

### Phase Governance Gates

✅ **PASS**: Scope limited to Phase I specification only
✅ **PASS**: No preparation for future phases
✅ **PASS**: No abstractions beyond current requirements
✅ **PASS**: All features explicitly defined in approved specification

**Gate Status**: ✅ ALL GATES PASSED - Proceed to Phase 0

## Project Structure

### Documentation (this feature)

```text
specs/001-phase1-core-todo/
├── spec.md              # Feature specification (approved)
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (technical decisions)
├── data-model.md        # Phase 1 output (Task entity design)
├── quickstart.md        # Phase 1 output (user guide)
├── checklists/
│   └── requirements.md  # Spec quality validation (completed)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created yet)
```

### Source Code (repository root)

```text
src/
├── main.py              # Entry point and CLI loop
├── task_manager.py      # Task storage and CRUD operations
├── cli.py               # Menu display and user input handling
└── validators.py        # Input validation logic

tests/
├── unit/
│   ├── test_task_manager.py
│   ├── test_validators.py
│   └── test_cli.py
└── integration/
    └── test_full_workflow.py

requirements.txt         # Empty (no dependencies) or pytest only
pyproject.toml          # Project metadata and pytest configuration
.gitignore              # Python standard ignores
```

**Structure Decision**: Single project structure selected. Console application doesn't require web/mobile organization. Separation into four modules (main, task_manager, cli, validators) provides clear responsibility boundaries while maintaining simplicity. If total code stays under 300 lines, may consolidate into 2-3 files during implementation.

## Complexity Tracking

No constitutional violations to justify. All complexity gates passed.

## Architecture Decisions

### AD-001: Data Storage Strategy

**Decision**: Use Python list of dictionaries for in-memory task storage

**Rationale**:
- Constitutional requirement: No persistence, in-memory only
- Simplest data structure that meets requirements
- Native Python types, no external dependencies
- Direct integer indexing for O(1) access by position
- Sequential ID generation trivial with `len(tasks) + 1`

**Alternatives Considered**:
1. **Dictionary with ID as key**: More complex, no benefit for sequential IDs
2. **Custom Task class**: Over-engineering for Phase I, conflicts with YAGNI principle
3. **NamedTuple**: Immutability conflicts with update/delete operations

**Implementation**:
```python
# Task stored as dict:
{
    "id": 1,
    "title": "Buy groceries",
    "description": "Get milk, eggs, bread",
    "status": "incomplete"
}

# Storage:
tasks: list[dict[str, str | int]] = []
```

### AD-002: Task ID Generation Strategy

**Decision**: Sequential integer IDs starting from 1, never reused

**Rationale**:
- Specification requires unique sequential IDs
- Simple counter approach: `next_id = len(tasks) + 1`
- For Phase I in-memory scope, deleted task IDs don't need reuse
- Maintains chronological ordering

**Alternatives Considered**:
1. **Reuse deleted IDs**: Adds complexity tracking available IDs, not required by spec
2. **UUID**: Overkill for single-user in-memory application
3. **Index-based**: Breaks when tasks deleted, violates spec requirement for stable IDs

**Implementation**:
```python
def generate_next_id(tasks: list[dict]) -> int:
    """Generate next sequential task ID."""
    return max([task["id"] for task in tasks], default=0) + 1
```

**Note**: Using `max()` instead of `len()` ensures correct ID generation even after deletions.

### AD-003: CLI Control Flow Pattern

**Decision**: Infinite menu loop with command dispatch

**Rationale**:
- Specification requires return to main menu after each operation
- Clear separation between menu display and command execution
- Easy to test each operation independently
- Standard pattern for console applications

**Implementation Pattern**:
```python
while True:
    display_menu()
    choice = get_user_input()

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    # ... other options
    elif choice == "7":
        exit_application()
        break
    else:
        display_error("Invalid option")
```

**Alternatives Considered**:
1. **Command-line arguments**: Conflicts with spec requirement for menu-driven interface
2. **Recursive function calls**: Risks stack overflow, harder to test
3. **State machine**: Over-engineering for simple linear menu flow

### AD-004: Module Responsibility Separation

**Decision**: Four-module design with clear boundaries

**Modules**:
1. **main.py**: Application entry point, main loop orchestration
2. **task_manager.py**: Task storage and CRUD operations (add, get, update, delete, mark)
3. **cli.py**: User interface (menu display, input prompts, output formatting)
4. **validators.py**: Input validation logic (ID validation, empty check, numeric check)

**Rationale**:
- Testability: Each module can be tested independently
- Single Responsibility Principle: Clear, focused purposes
- CLI logic separated from business logic (task operations)
- Validators reusable across different operations
- Enables 80%+ test coverage requirement

**Alternatives Considered**:
1. **Single file**: May exceed 300 lines, hard to test, poor organization
2. **More granular modules**: Over-engineering, violates YAGNI
3. **Class-based architecture**: Unnecessary for stateless operations, adds complexity

### AD-005: Error Handling Strategy

**Decision**: Exception-based error handling with graceful recovery

**Approach**:
- Validators raise `ValueError` for invalid input (non-numeric ID, empty strings)
- Task operations raise `KeyError` for non-existent task IDs
- Main loop catches exceptions, displays user-friendly messages, continues to menu
- No application crashes on invalid input

**Rationale**:
- Specification requires graceful error handling for all edge cases
- Python idiomatic approach
- Clear error messages as specified in spec
- Application always returns to main menu after error

**Implementation Pattern**:
```python
try:
    task_id = validate_numeric_input(user_input)
    task = get_task_by_id(task_id)
    # ... operation
except ValueError as e:
    print(f"Error: {e}")
except KeyError:
    print(f"Error: Task ID {task_id} not found.")
```

**Alternatives Considered**:
1. **Return codes**: Less Pythonic, harder to trace error source
2. **Silent failures**: Violates specification requirement for clear feedback
3. **Custom exception classes**: Over-engineering for Phase I scope

### AD-006: Testing Strategy

**Decision**: Pytest with unit and integration test separation

**Test Structure**:
- **Unit tests**: Test individual functions in isolation (task_manager, validators, cli helpers)
- **Integration tests**: Test complete user workflows (add → view → update → delete)
- **Coverage target**: 80% minimum as per constitution
- **Mocking**: Use unittest.mock for input/output in CLI tests

**Rationale**:
- Constitutional requirement: pytest framework
- Separation enables focused, fast unit tests and comprehensive workflow validation
- Integration tests validate acceptance criteria from specification
- Mocking prevents actual console I/O during tests

**Test Files**:
- `test_task_manager.py`: CRUD operations, ID generation, validation
- `test_validators.py`: Input validation edge cases
- `test_cli.py`: Menu display, output formatting
- `test_full_workflow.py`: End-to-end user stories from specification

## Phase 0: Research

### Research Summary

**No research required** for Phase I. All technical decisions are straightforward:

1. **Python 3.13**: Standard library features sufficient, no version-specific concerns
2. **Data structures**: Built-in list and dict well-documented and appropriate
3. **Testing**: pytest is standard and well-known
4. **CLI patterns**: Simple input/output using built-in `input()` and `print()`

All technology choices are stable, well-documented, and have no ambiguity.

**Research Artifact**: No separate research.md needed - decisions documented above in Architecture Decisions section.

## Phase 1: Design

### Data Model

See `data-model.md` for complete entity design.

**Task Entity**:
```python
{
    "id": int,          # Sequential, unique, auto-generated
    "title": str,       # Required, non-empty, any length
    "description": str, # Required, non-empty, any length
    "status": str       # Literal["complete", "incomplete"]
}
```

**Validation Rules**:
- ID: Positive integer, must exist in task list for operations
- Title: Non-empty, non-whitespace-only string
- Description: Non-empty, non-whitespace-only string
- Status: Exactly "complete" or "incomplete"

**State Transitions**:
- New task: status = "incomplete"
- Mark complete: "incomplete" → "complete"
- Mark incomplete: "complete" → "incomplete"
- Update: status unchanged
- Delete: task removed entirely

### Contracts

**Note**: Console application has no external API, so traditional API contracts (OpenAPI, GraphQL) don't apply.

**Internal Function Contracts** documented in `contracts/internal_functions.md`:

```python
# TaskManager class contracts

def add_task(title: str, description: str) -> dict:
    """
    Create a new task with sequential ID and incomplete status.

    Args:
        title: Non-empty task title
        description: Non-empty task description

    Returns:
        Created task dictionary with id, title, description, status

    Raises:
        ValueError: If title or description is empty/whitespace-only
    """

def get_all_tasks() -> list[dict]:
    """
    Retrieve all tasks in creation order.

    Returns:
        List of task dictionaries, ordered by ID ascending
    """

def get_task_by_id(task_id: int) -> dict:
    """
    Retrieve a specific task by ID.

    Args:
        task_id: Task ID to retrieve

    Returns:
        Task dictionary

    Raises:
        KeyError: If task ID not found
    """

def update_task(task_id: int, title: str | None, description: str | None) -> dict:
    """
    Update task title and/or description.

    Args:
        task_id: Task ID to update
        title: New title or None to keep current
        description: New description or None to keep current

    Returns:
        Updated task dictionary

    Raises:
        KeyError: If task ID not found
        ValueError: If provided title/description is empty/whitespace-only
    """

def delete_task(task_id: int) -> None:
    """
    Permanently remove a task.

    Args:
        task_id: Task ID to delete

    Raises:
        KeyError: If task ID not found
    """

def mark_task_complete(task_id: int) -> dict:
    """
    Change task status to 'complete'.

    Args:
        task_id: Task ID to mark complete

    Returns:
        Updated task dictionary

    Raises:
        KeyError: If task ID not found
    """

def mark_task_incomplete(task_id: int) -> dict:
    """
    Change task status to 'incomplete'.

    Args:
        task_id: Task ID to mark incomplete

    Returns:
        Updated task dictionary

    Raises:
        KeyError: If task ID not found
    """
```

### Quickstart Guide

See `quickstart.md` for end-user documentation.

**Quick Summary**:
1. Run: `python src/main.py`
2. Select menu option (1-7)
3. Follow prompts for each operation
4. Data persists only while program running
5. Exit with option 7

## Implementation Notes

### Type Hints Strategy

All functions will use type hints as required by constitution:

```python
from typing import Literal

TaskDict = dict[str, str | int]  # Type alias for task dictionary
TaskStatus = Literal["complete", "incomplete"]

def add_task(title: str, description: str) -> TaskDict:
    ...

def get_all_tasks() -> list[TaskDict]:
    ...
```

### Docstring Format

Google-style docstrings for all public functions:

```python
def update_task(task_id: int, title: str | None, description: str | None) -> dict:
    """Update an existing task's title and/or description.

    Args:
        task_id: The ID of the task to update.
        title: New title or None to keep current title.
        description: New description or None to keep current description.

    Returns:
        The updated task dictionary with all fields.

    Raises:
        KeyError: If the task ID does not exist.
        ValueError: If provided title or description is empty or whitespace-only.

    Example:
        >>> task = update_task(1, "New Title", None)
        >>> print(task["title"])
        New Title
    """
```

### Testing Approach

**Unit Test Example** (test_task_manager.py):
```python
def test_add_task_creates_task_with_sequential_id():
    manager = TaskManager()
    task1 = manager.add_task("Task 1", "Description 1")
    task2 = manager.add_task("Task 2", "Description 2")

    assert task1["id"] == 1
    assert task2["id"] == 2
    assert task1["status"] == "incomplete"

def test_add_task_raises_error_for_empty_title():
    manager = TaskManager()
    with pytest.raises(ValueError, match="title cannot be empty"):
        manager.add_task("", "Description")
```

**Integration Test Example** (test_full_workflow.py):
```python
def test_user_story_1_add_and_view_task(capsys):
    """Test US1: User can add a task and view it in the list."""
    # Simulate adding task
    manager = TaskManager()
    task = manager.add_task("Buy groceries", "Get milk, eggs, bread")

    # Simulate viewing tasks
    tasks = manager.get_all_tasks()

    assert len(tasks) == 1
    assert tasks[0]["id"] == 1
    assert tasks[0]["title"] == "Buy groceries"
    assert tasks[0]["status"] == "incomplete"
```

### CLI Output Format

Exact output formats as specified in spec:

**Main Menu**:
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

**Task List Display**:
```
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

### Error Messages

Exact error messages as specified in spec:
- Invalid menu: "Error: Invalid option. Please select a number between 1 and 7."
- Invalid ID (non-existent): "Error: Task ID [X] not found."
- Invalid ID (non-numeric): "Error: Task ID must be a number."
- Empty title: "Error: Task title cannot be empty."
- Empty description: "Error: Task description cannot be empty."

## Risk Analysis

### Risk 1: Task Deletion ID Gap Handling

**Risk**: After deleting task ID 2, new tasks must start from ID 4 (not reuse ID 2)

**Mitigation**: Use `max(task["id"])` instead of `len(tasks)` for ID generation (AD-002)

**Impact**: Low - addressed in architecture decision

### Risk 2: Whitespace-Only Input

**Risk**: Users could enter strings with only spaces/tabs, bypassing empty checks

**Mitigation**: Use `str.strip()` before validation, check if result is empty

**Impact**: Low - covered by validators module design

### Risk 3: Large Task Lists

**Risk**: Displaying 1000+ tasks could cause terminal scrolling issues

**Mitigation**: For Phase I, accept this limitation per spec. No pagination required.

**Impact**: Low - spec defines scale as appropriate for in-memory console app

## Deferred to Future Phases

The following are explicitly NOT included in Phase I implementation:

- Data persistence (files, databases)
- Task filtering or sorting
- Task search functionality
- Task categories or tags
- Due dates or priorities
- Configuration options
- Command-line argument parsing
- Undo/redo functionality
- Multi-user support
- Any networked features

These would require specification updates and constitute Phase II+ features.

## Definition of Done

Phase I implementation plan is complete when:

✅ All architecture decisions documented with rationale
✅ Data model designed and validated against spec
✅ Internal function contracts defined
✅ Project structure defined
✅ Constitution check passed
✅ Risk analysis completed
✅ Test strategy documented
✅ Ready for `/sp.tasks` command to generate task breakdown

**Next Step**: Run `/sp.tasks` to generate task list from this plan and approved specification.
