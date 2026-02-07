---
name: testing-guidelines
description: Enforces structured, reliable testing practices. Apply when writing, updating, or reviewing tests to ensure correctness, coverage, and maintainability.
allowed-tools: Read, Write
---

# Automated Testing Guidelines

## Purpose
This skill enforces rigorous automated testing practices to ensure implementation correctness, reliability, and maintainability. Apply these guidelines when writing, reviewing, or executing tests for any implementation.

## Core Testing Principles

### 1. Test Everything That Can Break
- Every feature must have corresponding tests
- Every bug fix must include a regression test
- No code is complete until it has tests

### 2. Tests Must Be Reliable
- Tests must pass consistently (no flaky tests)
- Tests must be deterministic (same input = same result)
- Tests must be independent (no shared state)

### 3. Tests Must Be Maintainable
- Test code quality equals production code quality
- Clear test names that describe what is tested
- Minimal duplication through proper test utilities

### 4. No Test Skipping Without Justification
- **NEVER skip tests without documented reason**
- Every `@skip`, `@unittest.skip`, or `pytest.skip` requires a comment explaining why
- Skipped tests must have a tracking issue or timeline for fixing

## Unit vs Integration Test Rules

### Unit Tests

**Definition**: Tests that verify a single unit of code (function, method, class) in isolation.

**Characteristics**:
- Fast execution (milliseconds)
- No external dependencies (databases, files, networks)
- Use mocks/stubs for dependencies
- Focus on a single behavior or method

**When to Write Unit Tests**:
- Testing business logic and algorithms
- Testing data transformations
- Testing validation functions
- Testing utility functions
- Testing error handling paths

**Unit Test Structure**:
```python
def test_function_name_condition_expected_result():
    # Arrange: Set up test data and dependencies
    input_data = create_test_input()
    mock_dependency = Mock()

    # Act: Execute the function under test
    result = function_under_test(input_data, mock_dependency)

    # Assert: Verify the expected outcome
    assert result == expected_value
    mock_dependency.method.assert_called_once_with(expected_arg)
```

**Unit Test Examples**:
```python
# Good: Tests single function with clear intent
def test_add_task_with_valid_description_returns_task_id():
    todo_list = TodoList()
    task_id = todo_list.add("Buy milk")
    assert isinstance(task_id, int)
    assert task_id > 0

def test_add_task_with_empty_description_raises_value_error():
    todo_list = TodoList()
    with pytest.raises(ValueError, match="empty"):
        todo_list.add("")

def test_complete_task_marks_task_as_done():
    todo_list = TodoList()
    task_id = todo_list.add("Test task")
    todo_list.complete(task_id)
    assert todo_list.is_completed(task_id) is True
```

### Integration Tests

**Definition**: Tests that verify multiple components work together correctly.

**Characteristics**:
- Slower execution (seconds)
- May use real dependencies (databases, files)
- Test component interactions
- Focus on workflows and data flow

**When to Write Integration Tests**:
- Testing database operations
- Testing file I/O operations
- Testing API endpoints
- Testing command-line interface
- Testing multi-component workflows

**Integration Test Structure**:
```python
def test_workflow_name_complete_scenario():
    # Setup: Prepare real or test environment
    setup_test_database()

    # Execute: Run the complete workflow
    result = execute_workflow(test_data)

    # Verify: Check end-to-end results
    assert result.status == "success"
    assert database_contains(expected_data)

    # Cleanup: Restore environment
    cleanup_test_database()
```

**Integration Test Examples**:
```python
# Good: Tests complete workflow
def test_cli_add_and_list_workflow():
    # Setup
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = os.path.join(tmpdir, "test.db")

        # Add task via CLI
        result = subprocess.run(
            ["todo", "add", "Test task", "--db", db_path],
            capture_output=True, text=True
        )
        assert result.returncode == 0

        # List tasks via CLI
        result = subprocess.run(
            ["todo", "list", "--db", db_path],
            capture_output=True, text=True
        )
        assert result.returncode == 0
        assert "Test task" in result.stdout
```

### Test Coverage Guidelines

**Minimum Coverage Requirements**:
- Critical business logic: 100% coverage
- Public APIs and interfaces: 100% coverage
- Utility functions: 90%+ coverage
- Overall codebase: 80%+ coverage

**Coverage is Necessary But Not Sufficient**:
- 100% coverage doesn't mean all behaviors are tested
- Must test edge cases and error conditions
- Must test boundary conditions
- Must test integration points

## Edge Case Testing

### What Are Edge Cases?
Edge cases are scenarios at the boundaries of normal operation:
- Boundary values (min, max, zero, empty)
- Invalid inputs
- Error conditions
- Unusual but valid inputs
- Race conditions and timing issues

### Mandatory Edge Cases to Test

#### 1. Boundary Values
```python
# Test minimum, maximum, and zero values
def test_add_task_with_maximum_length_description():
    max_length = 500
    description = "x" * max_length
    task_id = todo_list.add(description)
    assert task_id is not None

def test_add_task_exceeding_maximum_length_raises_error():
    description = "x" * 501
    with pytest.raises(ValueError, match="too long"):
        todo_list.add(description)

def test_list_tasks_with_zero_tasks_returns_empty_list():
    tasks = todo_list.list_all()
    assert tasks == []
    assert len(tasks) == 0
```

#### 2. Empty and Null Values
```python
# Test empty strings, None, empty collections
def test_add_task_with_empty_string_raises_error():
    with pytest.raises(ValueError):
        todo_list.add("")

def test_add_task_with_whitespace_only_raises_error():
    with pytest.raises(ValueError):
        todo_list.add("   ")

def test_add_task_with_none_raises_error():
    with pytest.raises(TypeError):
        todo_list.add(None)
```

#### 3. Invalid Types
```python
# Test wrong data types
def test_complete_task_with_string_id_raises_error():
    with pytest.raises(TypeError):
        todo_list.complete("not_an_int")

def test_complete_task_with_float_id_raises_error():
    with pytest.raises(TypeError):
        todo_list.complete(1.5)
```

#### 4. Non-Existent Resources
```python
# Test operations on missing resources
def test_complete_nonexistent_task_raises_error():
    with pytest.raises(KeyError, match="not found"):
        todo_list.complete(99999)

def test_delete_already_deleted_task_raises_error():
    task_id = todo_list.add("Task")
    todo_list.delete(task_id)
    with pytest.raises(KeyError):
        todo_list.delete(task_id)
```

#### 5. Special Characters and Encoding
```python
# Test Unicode, special characters, escape sequences
def test_add_task_with_unicode_characters():
    task_id = todo_list.add("买东西 🛒")
    task = todo_list.get(task_id)
    assert task.description == "买东西 🛒"

def test_add_task_with_newlines_and_tabs():
    description = "Line 1\nLine 2\tTabbed"
    task_id = todo_list.add(description)
    task = todo_list.get(task_id)
    assert task.description == description
```

#### 6. Large Inputs
```python
# Test with large data sets
def test_list_tasks_with_1000_tasks():
    for i in range(1000):
        todo_list.add(f"Task {i}")
    tasks = todo_list.list_all()
    assert len(tasks) == 1000
```

#### 7. Concurrent Access (if applicable)
```python
# Test thread safety and race conditions
def test_concurrent_add_tasks_maintains_consistency():
    import threading
    results = []

    def add_tasks():
        for i in range(100):
            task_id = todo_list.add(f"Task {i}")
            results.append(task_id)

    threads = [threading.Thread(target=add_tasks) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    # All task IDs should be unique
    assert len(set(results)) == len(results)
```

### Edge Case Testing Checklist

For every function/method, consider testing:
- [ ] Empty input (empty string, empty list, zero, None)
- [ ] Minimum valid value
- [ ] Maximum valid value
- [ ] Just below minimum (should fail)
- [ ] Just above maximum (should fail)
- [ ] Wrong data type
- [ ] Negative numbers (when not allowed)
- [ ] Non-existent resources (invalid IDs, missing files)
- [ ] Special characters and Unicode
- [ ] Very large inputs
- [ ] Duplicate operations
- [ ] Order-dependent operations

## Test Organization and Structure

### File Organization
```
project/
├── src/
│   └── todo_app.py
└── tests/
    ├── unit/
    │   ├── test_task_model.py
    │   ├── test_task_manager.py
    │   └── test_validators.py
    ├── integration/
    │   ├── test_database_operations.py
    │   ├── test_cli_commands.py
    │   └── test_file_storage.py
    └── fixtures/
        └── test_data.py
```

### Test Naming Conventions

**Pattern**: `test_<unit>_<condition>_<expected_result>`

```python
# Good: Clear, descriptive names
def test_add_task_with_valid_description_returns_task_id()
def test_add_task_with_empty_description_raises_value_error()
def test_complete_task_with_invalid_id_raises_key_error()
def test_list_tasks_with_completed_filter_returns_only_completed()

# Bad: Vague or unclear names
def test_add()
def test_error_case()
def test_1()
```

### Test Documentation

Every test should be self-documenting through:
1. **Clear test name** describing what is tested
2. **Comments** for complex setup or assertions
3. **Assertion messages** for clarity on failure

```python
def test_add_task_with_duplicate_description_creates_separate_tasks():
    """
    Adding tasks with identical descriptions should create separate
    task instances with unique IDs, as tasks are distinguished by ID
    not description.
    """
    # Arrange
    description = "Duplicate task"

    # Act
    task_id_1 = todo_list.add(description)
    task_id_2 = todo_list.add(description)

    # Assert
    assert task_id_1 != task_id_2, "Task IDs must be unique"
    assert todo_list.get(task_id_1).description == description
    assert todo_list.get(task_id_2).description == description
```

## Test Fixtures and Test Data

### Use Fixtures for Setup and Teardown
```python
import pytest

@pytest.fixture
def empty_todo_list():
    """Provides a fresh TodoList instance for each test"""
    return TodoList()

@pytest.fixture
def todo_list_with_tasks():
    """Provides a TodoList with pre-populated test tasks"""
    todo = TodoList()
    todo.add("Task 1")
    todo.add("Task 2")
    todo.add("Task 3")
    return todo

@pytest.fixture
def temp_database():
    """Provides a temporary database that's cleaned up after test"""
    with tempfile.NamedTemporaryFile(suffix='.db', delete=False) as f:
        db_path = f.name

    # Setup
    initialize_database(db_path)

    yield db_path

    # Teardown
    os.unlink(db_path)

# Usage
def test_add_task(empty_todo_list):
    task_id = empty_todo_list.add("New task")
    assert task_id > 0

def test_list_tasks(todo_list_with_tasks):
    tasks = todo_list_with_tasks.list_all()
    assert len(tasks) == 3
```

### Test Data Best Practices
```python
# Good: Realistic, meaningful test data
def test_task_priority_sorting():
    tasks = [
        Task("Fix critical bug", priority="high"),
        Task("Update docs", priority="low"),
        Task("Review PR", priority="medium"),
    ]
    sorted_tasks = sort_by_priority(tasks)
    assert sorted_tasks[0].priority == "high"

# Bad: Meaningless test data
def test_task_priority_sorting():
    tasks = [
        Task("foo", priority="a"),
        Task("bar", priority="b"),
        Task("baz", priority="c"),
    ]
    # Unclear what priorities mean
```

## Assertion Best Practices

### Be Specific in Assertions
```python
# Good: Specific assertions
assert result.status == "success"
assert result.task_id == 42
assert len(result.errors) == 0

# Bad: Generic assertions
assert result  # What property are we checking?
assert result == True  # Use 'is True' for booleans
```

### Provide Assertion Messages
```python
# Good: Clear failure messages
assert task_id > 0, f"Expected positive task ID, got {task_id}"
assert description in task.description, \
    f"Expected '{description}' in task, got '{task.description}'"

# Bad: No message
assert task_id > 0
```

### Test One Thing Per Test
```python
# Good: Focused test
def test_complete_task_marks_as_completed():
    task_id = todo_list.add("Task")
    todo_list.complete(task_id)
    assert todo_list.is_completed(task_id)

# Bad: Multiple unrelated assertions
def test_todo_operations():
    task_id = todo_list.add("Task")
    assert task_id > 0
    todo_list.complete(task_id)
    assert todo_list.is_completed(task_id)
    todo_list.delete(task_id)
    with pytest.raises(KeyError):
        todo_list.get(task_id)
    # This should be 3 separate tests
```

### Use Appropriate Assertion Methods
```python
# Good: Specific assertion methods
assert actual == expected
assert item in collection
assert value is None
assert isinstance(obj, ExpectedClass)
with pytest.raises(ValueError, match="specific message"):
    function_that_should_raise()

# Bad: Generic or unclear assertions
assert actual
assert not not value  # Just use 'assert value'
```

## Clear Pass/Fail Reporting

### Test Output Format

**Successful Test Run**:
```
tests/unit/test_task_manager.py::test_add_task_with_valid_description PASSED
tests/unit/test_task_manager.py::test_add_task_with_empty_description_raises_error PASSED
tests/unit/test_task_manager.py::test_complete_task_marks_as_done PASSED

==================== 3 passed in 0.12s ====================
```

**Failed Test Run**:
```
tests/unit/test_task_manager.py::test_add_task_with_valid_description FAILED

________________________________ FAILURES ________________________________
____ test_add_task_with_valid_description ____

    def test_add_task_with_valid_description():
        todo_list = TodoList()
>       task_id = todo_list.add("Buy milk")
E       TypeError: add() missing 1 required positional argument: 'priority'

tests/unit/test_task_manager.py:42: TypeError

==================== 1 failed, 2 passed in 0.15s ====================
```

### Test Report Requirements

Every test run must report:
1. **Total tests executed**
2. **Pass/fail counts**
3. **Execution time**
4. **Failure details** (traceback, assertion values)
5. **Coverage percentage** (when coverage tool is used)

### Continuous Integration Reporting
```python
# Generate multiple report formats
pytest tests/ \
    --verbose \
    --tb=short \
    --cov=src \
    --cov-report=term-missing \
    --cov-report=html \
    --junit-xml=test-results.xml
```

## Test Skipping Rules

### NEVER Skip Tests Without Documentation

**Acceptable Reasons to Skip**:
1. Known platform-specific issue with tracking ticket
2. External dependency unavailable (with plan to fix)
3. Test for upcoming feature (clearly marked)
4. Performance test only run manually (documented)

**Unacceptable Reasons**:
1. Test is failing (fix the test or the code!)
2. Test is flaky (fix the flakiness!)
3. Test is slow (optimize it or move to integration suite)
4. "Will fix later" (no tracking issue)

### Proper Test Skipping Format
```python
# Good: Documented skip with reason and tracking
@pytest.mark.skip(reason="Windows file locking issue - See issue #123")
def test_concurrent_file_access():
    pass

@pytest.mark.skipif(sys.platform == "win32",
                    reason="POSIX-specific signal handling")
def test_signal_handling():
    pass

# Good: Conditional skip with clear reason
@pytest.mark.skipif(not has_database_connection(),
                    reason="Database not available in CI environment")
def test_database_query_performance():
    pass

# Bad: Skip without explanation
@pytest.mark.skip
def test_something():
    pass

# Bad: Skip due to test failure
@pytest.mark.skip(reason="TODO: fix this test")
def test_broken_feature():
    pass
```

### Expected Failures
```python
# Use xfail for known issues that need fixing
@pytest.mark.xfail(reason="Known bug #456 - invalid date handling")
def test_add_task_with_invalid_date():
    todo_list.add("Task", due_date="invalid")
    # This test should pass once bug #456 is fixed
```

## Test Execution Guidelines

### Running Tests

**Run All Tests**:
```bash
pytest tests/
```

**Run Specific Test Suite**:
```bash
pytest tests/unit/          # Unit tests only
pytest tests/integration/   # Integration tests only
```

**Run Specific Test File**:
```bash
pytest tests/unit/test_task_manager.py
```

**Run Specific Test**:
```bash
pytest tests/unit/test_task_manager.py::test_add_task_with_valid_description
```

**Run with Coverage**:
```bash
pytest tests/ --cov=src --cov-report=term-missing
```

**Run with Verbose Output**:
```bash
pytest tests/ -v
```

### Test Execution Order

1. **Unit tests first** (fast feedback)
2. **Integration tests second** (verify component interaction)
3. **End-to-end tests last** (full system validation)

### Pre-Commit Testing
```bash
# Before committing, always run:
pytest tests/ --cov=src --cov-report=term-missing

# All tests must pass
# Coverage must meet threshold (80%+)
```

## Mocking and Test Doubles

### When to Use Mocks
- External API calls
- Database connections (in unit tests)
- File system operations (in unit tests)
- Time-dependent operations
- Random number generation

### Mock Examples
```python
from unittest.mock import Mock, patch, MagicMock

# Mock external API
def test_fetch_tasks_from_api():
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {'tasks': []}
        mock_get.return_value.status_code = 200

        result = fetch_tasks_from_api()

        assert result == []
        mock_get.assert_called_once_with('https://api.example.com/tasks')

# Mock file operations
def test_save_tasks_to_file():
    with patch('builtins.open', create=True) as mock_open:
        mock_file = MagicMock()
        mock_open.return_value.__enter__.return_value = mock_file

        save_tasks([Task("Test")])

        mock_open.assert_called_once_with('tasks.json', 'w')
        mock_file.write.assert_called()

# Mock time
def test_task_is_overdue():
    with patch('datetime.datetime') as mock_datetime:
        mock_datetime.now.return_value = datetime(2024, 12, 31)

        task = Task("Task", due_date=datetime(2024, 12, 30))

        assert task.is_overdue() is True
```

## Quality Checklist

Before considering tests complete, verify:

- [ ] All public methods have unit tests
- [ ] All edge cases are tested
- [ ] All error conditions are tested
- [ ] Integration tests cover main workflows
- [ ] Tests are independent (can run in any order)
- [ ] Tests have clear, descriptive names
- [ ] Test coverage meets minimum threshold (80%+)
- [ ] No flaky tests (tests pass consistently)
- [ ] No skipped tests without documented reason
- [ ] Tests run fast (unit tests < 1s, integration tests < 10s)
- [ ] Mocks are used appropriately
- [ ] Test data is realistic and meaningful
- [ ] Assertions are specific with clear messages
- [ ] Test failures provide actionable information

## Common Anti-Patterns to Avoid

### ❌ Don't:
- Skip tests because they're failing
- Test implementation details instead of behavior
- Write tests that depend on execution order
- Use sleep() to handle timing issues
- Copy-paste test code without refactoring
- Write tests after discovering bugs in production
- Ignore test failures in CI
- Test too much in a single test
- Use production data in tests
- Commit code without running tests

### ✅ Do:
- Write tests while developing (TDD or alongside)
- Test behavior and contracts, not implementation
- Make tests independent and isolated
- Use proper synchronization and mocking for timing
- Extract common test utilities and fixtures
- Write regression tests immediately after bug fixes
- Keep CI green at all times
- Focus each test on one behavior
- Use dedicated test data
- Run full test suite before committing

## Usage

Apply this skill when:
1. Writing tests for new features
2. Adding regression tests for bug fixes
3. Reviewing test code quality
4. Validating implementation correctness
5. Setting up test infrastructure
6. Debugging test failures

## Success Criteria

Tests meet these standards when:
1. All tests pass consistently
2. Coverage meets or exceeds 80%
3. Edge cases are thoroughly tested
4. Test names clearly describe what is tested
5. Failures provide clear, actionable information
6. Tests run quickly and independently
7. No tests are skipped without valid reason
8. Test code is maintainable and well-organized
