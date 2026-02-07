"""Task Manager module for Evolution of Todo application.

This module provides the TaskManager class for managing tasks in memory.
"""

from typing import Literal
from validators import validate_non_empty_string


TaskDict = dict[str, str | int]
TaskStatus = Literal["complete", "incomplete"]


class TaskManager:
    """Manages tasks in memory with CRUD operations."""

    def __init__(self) -> None:
        """Initialize a new TaskManager instance with empty task storage."""
        self._tasks: list[TaskDict] = []

    def add_task(self, title: str, description: str) -> TaskDict:
        """Create a new task with automatically generated sequential ID and incomplete status.

        Args:
            title: Non-empty task title.
            description: Non-empty task description.

        Returns:
            Created task dictionary with id, title, description, status.

        Raises:
            ValueError: If title or description is empty/whitespace-only.

        Example:
            >>> manager = TaskManager()
            >>> task = manager.add_task("Buy groceries", "Get milk, eggs, bread")
            >>> task["id"]
            1
            >>> task["status"]
            'incomplete'
        """
        # Validate inputs
        trimmed_title = validate_non_empty_string(title, "title")
        trimmed_description = validate_non_empty_string(description, "description")

        # Generate next ID using max() strategy to handle deletions correctly
        next_id = max([task["id"] for task in self._tasks], default=0) + 1

        # Create task
        task: TaskDict = {
            "id": next_id,
            "title": trimmed_title,
            "description": trimmed_description,
            "status": "incomplete"
        }

        self._tasks.append(task)
        return task

    def get_all_tasks(self) -> list[TaskDict]:
        """Retrieve all tasks in creation order (ID ascending).

        Returns:
            List of task dictionaries, ordered by ID ascending.
            Empty list if no tasks exist.

        Example:
            >>> manager = TaskManager()
            >>> manager.add_task("Task 1", "Description 1")  # doctest: +SKIP
            >>> manager.add_task("Task 2", "Description 2")  # doctest: +SKIP
            >>> tasks = manager.get_all_tasks()
            >>> len(tasks)  # doctest: +SKIP
            2
        """
        return self._tasks

    def get_task_by_id(self, task_id: int) -> TaskDict:
        """Retrieve a specific task by its unique ID.

        Args:
            task_id: The ID of the task to retrieve.

        Returns:
            Task dictionary with matching ID.

        Raises:
            KeyError: If task with specified ID does not exist.

        Example:
            >>> manager = TaskManager()
            >>> task = manager.add_task("Buy groceries", "Get milk")
            >>> retrieved = manager.get_task_by_id(1)
            >>> retrieved["title"]
            'Buy groceries'
        """
        for task in self._tasks:
            if task["id"] == task_id:
                return task
        raise KeyError(f"Task ID {task_id} not found.")

    def mark_task_complete(self, task_id: int) -> TaskDict:
        """Change a task's status to 'complete'.

        Args:
            task_id: ID of task to mark complete.

        Returns:
            Updated task dictionary with status='complete'.

        Raises:
            KeyError: If task with specified ID does not exist.

        Example:
            >>> manager = TaskManager()
            >>> task = manager.add_task("Task 1", "Description 1")
            >>> updated = manager.mark_task_complete(1)
            >>> updated["status"]
            'complete'
        """
        task = self.get_task_by_id(task_id)
        task["status"] = "complete"
        return task

    def mark_task_incomplete(self, task_id: int) -> TaskDict:
        """Change a task's status to 'incomplete'.

        Args:
            task_id: ID of task to mark incomplete.

        Returns:
            Updated task dictionary with status='incomplete'.

        Raises:
            KeyError: If task with specified ID does not exist.

        Example:
            >>> manager = TaskManager()
            >>> task = manager.add_task("Task 1", "Description 1")
            >>> manager.mark_task_complete(1)  # doctest: +SKIP
            >>> updated = manager.mark_task_incomplete(1)
            >>> updated["status"]
            'incomplete'
        """
        task = self.get_task_by_id(task_id)
        task["status"] = "incomplete"
        return task

    def update_task(self, task_id: int, title: str | None = None, description: str | None = None) -> TaskDict:
        """Update a task's title and/or description while preserving ID and status.

        Args:
            task_id: ID of task to update.
            title: New title, or None to keep current title.
            description: New description, or None to keep current description.

        Returns:
            Updated task dictionary with all fields.

        Raises:
            KeyError: If task with specified ID does not exist.
            ValueError: If provided title or description is empty or whitespace-only.

        Example:
            >>> manager = TaskManager()
            >>> task = manager.add_task("Task 1", "Description 1")
            >>> updated = manager.update_task(1, title="New Title")
            >>> updated["title"]
            'New Title'
            >>> updated["description"]
            'Description 1'
        """
        task = self.get_task_by_id(task_id)

        if title is not None:
            trimmed_title = validate_non_empty_string(title, "title")
            task["title"] = trimmed_title

        if description is not None:
            trimmed_description = validate_non_empty_string(description, "description")
            task["description"] = trimmed_description

        return task

    def delete_task(self, task_id: int) -> None:
        """Permanently remove a task from the task list.

        Args:
            task_id: ID of task to delete.

        Raises:
            KeyError: If task with specified ID does not exist.

        Example:
            >>> manager = TaskManager()
            >>> task = manager.add_task("Task 1", "Description 1")
            >>> manager.delete_task(1)
            >>> len(manager.get_all_tasks())
            0
        """
        task = self.get_task_by_id(task_id)  # Verify task exists
        self._tasks.remove(task)
