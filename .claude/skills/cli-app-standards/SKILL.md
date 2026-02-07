---
name: cli-app-standards
description: Enforces consistent, user-friendly standards for command-line interface (CLI) application development. Apply when generating or modifying any CLI application code.
allowed-tools: Read, Write
---

# CLI Application Development Standards

## Purpose
This skill enforces consistent, user-friendly standards for command-line interface (CLI) application development. Apply these rules when generating or modifying any CLI application code.

## Command Structure Conventions

### Basic Command Anatomy
```
program [global-options] command [command-options] [arguments]
```

### Command Naming Rules
1. **Use verb-noun pattern for commands**
   - ✅ `task add`, `user delete`, `config set`
   - ❌ `addition`, `remove-user`, `configuration`

2. **Keep commands short and memorable**
   - Prefer single words: `add`, `list`, `show`, `delete`
   - Use common abbreviations when clear: `ls`, `rm`, `cp`
   - Maximum 2-3 words for compound commands

3. **Use consistent command vocabulary**
   - `add` / `create` - pick one and stick with it
   - `delete` / `remove` / `rm` - pick one and stick with it
   - `list` / `ls` / `show` - pick one and stick with it
   - `update` / `edit` / `modify` - pick one and stick with it

4. **Subcommands for grouped functionality**
   ```
   todo task add "Buy milk"
   todo task list
   todo config set theme dark
   ```

### Command Organization
- **Flat structure** for simple apps (< 10 commands)
- **Hierarchical structure** for complex apps (> 10 commands)
- Group related commands under common prefixes

## Argument and Flag Naming Rules

### Positional Arguments
1. **Order by importance and frequency**
   - Most important/required arguments first
   - Optional arguments last

2. **Use descriptive names in help text**
   ```
   add <task_description> [priority]
   ```

3. **Validate early and fail fast**
   - Check required arguments before processing
   - Validate format and constraints immediately

### Flag Naming Conventions

#### Short Flags (Single Character)
- Use single dash: `-v`, `-h`, `-f`
- Reserve common flags consistently:
  - `-h` : help
  - `-v` : version or verbose
  - `-V` : version (if `-v` is verbose)
  - `-f` : force or file
  - `-o` : output
  - `-i` : input
  - `-q` : quiet
  - `-d` : debug or directory
  - `-n` : number or dry-run
  - `-a` : all

#### Long Flags (Multi-Character)
- Use double dash: `--verbose`, `--help`, `--force`
- Use kebab-case: `--dry-run`, `--output-file`
- Be descriptive: `--recursive`, `--ignore-case`
- Provide both short and long forms for common options

#### Boolean Flags
```python
# Good: Clear boolean flag
--verbose / -v          # Enable verbose output
--force / -f            # Force operation without confirmation
--recursive / -r        # Operate recursively

# Bad: Ambiguous flags
--level verbose         # Use --verbose instead
--confirm no            # Use --force or --no-confirm instead
```

#### Value Flags
```python
# Good: Clear value flags
--output <file>         # Output file path
--format <type>         # Output format (json, text, csv)
--limit <number>        # Limit number of results
--priority <level>      # Priority level (low, medium, high)

# Bad: Unclear flags
--o <value>             # Too abbreviated
--thing <thing>         # Non-descriptive name
```

#### Flag Negation
```python
# Use --no- prefix for negative flags
--color / --no-color
--verify / --no-verify
--interactive / --no-interactive
```

## Error Handling Guidelines

### Error Handling Principles
1. **Fail fast with clear error messages**
2. **Provide actionable guidance**
3. **Use consistent error format**
4. **Exit with appropriate status codes**

### Error Message Format
```
ERROR: <what went wrong>
<why it happened (optional)>
<how to fix it>
```

#### Examples
```
ERROR: Task ID not found: 42
No task exists with ID 42.
Use 'todo list' to see all tasks.

ERROR: Invalid date format: 2024-13-45
Date must be in YYYY-MM-DD format.
Example: 2024-12-31

ERROR: Permission denied: config.json
The configuration file is not writable.
Try running with elevated permissions or check file ownership.
```

### Exit Codes
Use standard exit codes consistently:

```python
# Standard exit codes
EXIT_SUCCESS = 0           # Successful execution
EXIT_GENERAL_ERROR = 1     # General error
EXIT_MISUSE = 2           # Invalid command usage
EXIT_NOT_FOUND = 3        # Resource not found
EXIT_PERMISSION = 4       # Permission denied
EXIT_IO_ERROR = 5         # I/O error
EXIT_INVALID_DATA = 6     # Invalid data format
EXIT_INTERRUPTED = 130    # Interrupted by Ctrl+C
```

### Error Handling Best Practices

#### 1. Validate Input Early
```python
# Good: Validate before processing
def add_task(description):
    if not description or not description.strip():
        print("ERROR: Task description cannot be empty", file=sys.stderr)
        sys.exit(2)

    if len(description) > 500:
        print("ERROR: Task description too long (max 500 characters)", file=sys.stderr)
        sys.exit(2)

    # Process task...
```

#### 2. Handle System Errors Gracefully
```python
# Good: Catch and explain system errors
try:
    with open(file_path, 'r') as f:
        data = f.read()
except FileNotFoundError:
    print(f"ERROR: File not found: {file_path}", file=sys.stderr)
    print("Use 'init' command to create the file.", file=sys.stderr)
    sys.exit(3)
except PermissionError:
    print(f"ERROR: Permission denied: {file_path}", file=sys.stderr)
    sys.exit(4)
except Exception as e:
    print(f"ERROR: Failed to read file: {e}", file=sys.stderr)
    sys.exit(5)
```

#### 3. Provide Context in Error Messages
```python
# Bad: Vague error
print("ERROR: Invalid input")

# Good: Specific error with context
print(f"ERROR: Invalid priority '{priority}'")
print("Valid priorities: low, medium, high")
```

#### 4. Use stderr for Errors
```python
# Always write errors to stderr, not stdout
print("ERROR: Something went wrong", file=sys.stderr)
```

## Output Formatting Rules

### Output Principles
1. **Machine-readable by default, human-friendly when needed**
2. **Consistent format across commands**
3. **Respect terminal width and capabilities**
4. **Support multiple output formats**

### Standard Output Formats

#### Plain Text (Default)
- Human-readable
- Clean and simple
- Aligned columns for tabular data
- Clear visual hierarchy

```
Tasks (3):
  1. [HIGH] Complete project report     Due: 2024-12-31
  2. [MED]  Review pull requests       Due: 2024-12-25
  3. [LOW]  Update documentation
```

#### JSON Format (`--format json`)
- Machine-readable
- Complete data structure
- Valid JSON output only (no extra text)

```json
{
  "tasks": [
    {
      "id": 1,
      "description": "Complete project report",
      "priority": "high",
      "due_date": "2024-12-31",
      "completed": false
    }
  ]
}
```

#### CSV Format (`--format csv`)
- Spreadsheet-compatible
- Header row with column names
- Proper escaping of quotes and commas

```csv
id,description,priority,due_date,completed
1,"Complete project report",high,2024-12-31,false
2,"Review pull requests",medium,2024-12-25,false
```

### Output Formatting Guidelines

#### 1. Tabular Data
```python
# Good: Aligned columns
ID    Description              Priority  Status
1     Fix login bug           HIGH      Open
2     Update documentation    LOW       Done
123   Refactor database       MEDIUM    Open

# Bad: Misaligned, hard to read
ID Description Priority Status
1 Fix login bug HIGH Open
2 Update documentation LOW Done
```

#### 2. Lists
```python
# Good: Clear list format with consistent indentation
Tasks:
  • Complete project report
  • Review pull requests
  • Update documentation

# Alternative: Numbered lists for ordered items
Top priorities:
  1. Fix critical security bug
  2. Deploy to production
  3. Update API documentation
```

#### 3. Success Messages
```python
# Good: Clear, concise confirmation
✓ Task added successfully (ID: 42)
✓ Configuration updated
✓ 3 tasks marked as complete

# Bad: Verbose, unclear
The task has been added to your list of tasks and assigned ID 42.
```

#### 4. Verbose Output
```python
# Use --verbose flag for detailed output
# Normal output:
✓ Backup completed

# Verbose output (--verbose):
Creating backup...
✓ Database exported (2.3 MB)
✓ Files archived (15.7 MB)
✓ Backup saved to: /backups/2024-12-31.tar.gz
✓ Backup completed in 4.2 seconds
```

#### 5. Progress Indicators
```python
# For long-running operations
Processing files... [████████████████████] 100% (50/50)

# For indeterminate operations
Connecting to server...

# Avoid progress indicators for:
# - Operations < 2 seconds
# - When output is piped
# - In non-interactive mode
```

### Color and Styling

#### When to Use Color
- Errors: Red
- Warnings: Yellow
- Success: Green
- Info: Blue or Cyan
- Highlights: Bold

#### Color Guidelines
```python
# Good: Use color libraries that respect NO_COLOR
# Detect terminal capabilities
# Provide --no-color flag
# Don't use color when piped

# Check if output is to a terminal
if sys.stdout.isatty() and not args.no_color:
    use_colors = True
```

#### Standard Color Scheme
- ✅ Success: Green
- ❌ Error: Red
- ⚠️  Warning: Yellow
- ℹ️  Info: Blue/Cyan
- 🔍 Debug: Gray/Dim

### Help Text Formatting

#### Command Help Structure
```
USAGE:
  program [OPTIONS] COMMAND [ARGS]

DESCRIPTION:
  Brief description of what the program does.

OPTIONS:
  -h, --help           Show this help message
  -v, --version        Show version information
  -q, --quiet          Suppress non-error output
  --format <type>      Output format (text, json, csv)

COMMANDS:
  add                  Add a new task
  list                 List all tasks
  delete               Delete a task
  complete             Mark a task as complete

Run 'program COMMAND --help' for command-specific help.
```

#### Command-Specific Help
```
USAGE:
  todo add [OPTIONS] <description>

DESCRIPTION:
  Add a new task to the todo list.

ARGUMENTS:
  <description>        Task description (required)

OPTIONS:
  -p, --priority <level>    Task priority (low, medium, high)
                            Default: medium
  -d, --due <date>          Due date (YYYY-MM-DD format)
  -t, --tags <tags>         Comma-separated tags

EXAMPLES:
  todo add "Buy groceries"
  todo add "Fix bug" --priority high --due 2024-12-31
  todo add "Review code" --tags code,urgent
```

## Implementation Patterns

### Argument Parsing
```python
# Use argparse or click for robust argument parsing
import argparse

parser = argparse.ArgumentParser(
    description='Simple todo list manager',
    formatter_class=argparse.RawDescriptionHelpFormatter
)

# Global options
parser.add_argument('-v', '--verbose', action='store_true',
                   help='Enable verbose output')
parser.add_argument('--format', choices=['text', 'json', 'csv'],
                   default='text', help='Output format')

# Subcommands
subparsers = parser.add_subparsers(dest='command', required=True)

# Add command
add_parser = subparsers.add_parser('add', help='Add a new task')
add_parser.add_argument('description', help='Task description')
add_parser.add_argument('-p', '--priority', choices=['low', 'medium', 'high'],
                       default='medium', help='Task priority')
```

### Command Execution Pattern
```python
def main():
    args = parser.parse_args()

    try:
        # Route to command handler
        if args.command == 'add':
            handle_add(args)
        elif args.command == 'list':
            handle_list(args)
        # ... other commands

        sys.exit(0)

    except KeyboardInterrupt:
        print("\nOperation cancelled", file=sys.stderr)
        sys.exit(130)

    except Exception as e:
        print(f"ERROR: Unexpected error: {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)
```

### Output Handler Pattern
```python
def output_result(data, format='text'):
    """Output data in requested format"""
    if format == 'json':
        import json
        print(json.dumps(data, indent=2))

    elif format == 'csv':
        import csv
        import sys
        writer = csv.DictWriter(sys.stdout, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    else:  # text
        # Human-readable format
        for item in data:
            print(f"{item['id']:3d}. {item['description']}")
```

## Quality Checklist

Before finalizing a CLI application, verify:

- [ ] All commands follow verb-noun naming pattern
- [ ] Short and long flag forms provided for common options
- [ ] Help text is clear and includes examples
- [ ] Errors print to stderr with actionable messages
- [ ] Exit codes are meaningful and documented
- [ ] Output format is consistent across commands
- [ ] --format flag supports json output for automation
- [ ] --help and --version flags work correctly
- [ ] Input validation happens before processing
- [ ] Long operations show progress indicators
- [ ] Colors respect terminal capabilities and NO_COLOR
- [ ] Command handles Ctrl+C gracefully

## Common Anti-Patterns to Avoid

### ❌ Don't:
- Use inconsistent command names (`add` vs `create` vs `new`)
- Make required arguments optional without defaults
- Print errors to stdout instead of stderr
- Use cryptic error messages without guidance
- Ignore exit codes (always exit 0)
- Mix output formats in text mode
- Use color when output is piped
- Make users remember obscure flag names
- Fail without explaining why
- Print help text when operation succeeds

### ✅ Do:
- Use consistent vocabulary throughout
- Validate input early and clearly
- Print errors to stderr with exit codes
- Provide helpful error messages with solutions
- Support both interactive and scripted usage
- Respect terminal capabilities
- Use standard flag conventions
- Provide examples in help text
- Handle interrupts gracefully
- Keep output clean and parseable

## Usage

Apply this skill when:
1. Generating new CLI applications
2. Modifying existing CLI code
3. Reviewing CLI application design
4. Creating command handlers
5. Implementing error handling
6. Formatting output

## Success Criteria

A CLI application meets these standards when:
1. Users can understand commands without consulting docs
2. Error messages guide users to solutions
3. Output is consistent and machine-parseable
4. Help text is clear and includes examples
5. Exit codes are meaningful
6. Flags follow common conventions
7. The tool works well in scripts and interactively
