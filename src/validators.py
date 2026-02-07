"""Input validation functions for Evolution of Todo application.

This module provides validation functions for user input.
"""


def validate_non_empty_string(value: str, field_name: str) -> str:
    """Validate that a string is non-empty and contains non-whitespace characters.

    Args:
        value: String to validate.
        field_name: Name of field for error messages (e.g., "title", "description").

    Returns:
        Trimmed string value.

    Raises:
        ValueError: If value is empty or whitespace-only, message includes field_name.

    Example:
        >>> validate_non_empty_string("  Buy groceries  ", "title")
        'Buy groceries'
        >>> validate_non_empty_string("   ", "description")
        Traceback (most recent call last):
            ...
        ValueError: Task description cannot be empty.
    """
    trimmed = value.strip()
    if not trimmed:
        raise ValueError(f"Task {field_name} cannot be empty.")
    return trimmed


def validate_numeric_input(value: str) -> int:
    """Validate and convert user input to an integer task ID.

    Args:
        value: User input string to validate.

    Returns:
        Parsed integer value.

    Raises:
        ValueError: If value cannot be converted to integer.

    Example:
        >>> validate_numeric_input("5")
        5
        >>> validate_numeric_input("abc")
        Traceback (most recent call last):
            ...
        ValueError: Task ID must be a number.
    """
    try:
        return int(value)
    except ValueError:
        raise ValueError("Task ID must be a number.")
