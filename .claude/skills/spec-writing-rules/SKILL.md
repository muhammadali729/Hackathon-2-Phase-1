---
name: spec-writing-rules
description: Enforces clear, unambiguous, testable specification writing rules. Apply when creating or updating technical specifications before any code is written.
allowed-tools: Read, Write
---

# Specification Writing Rules

## Purpose
This skill enforces a strict spec-before-code discipline for software projects, particularly CLI applications and backend systems. No code shall be written until a complete, approved specification exists.

## Core Principles

### 1. Specification-First Mandate
- **NEVER write implementation code before the specification is complete and approved**
- All features, commands, and behaviors must be documented before implementation
- The specification is the contract between intent and implementation

### 2. Specification Structure
Every specification must contain these four mandatory sections:

#### A. Overview
- **Purpose**: What problem does this solve? Why does it exist?
- **Scope**: What is included and explicitly excluded?
- **Target Users**: Who will use this? What are their needs?
- **High-Level Architecture**: Brief description of major components

#### B. Requirements
- **Functional Requirements**: Specific behaviors, features, and capabilities
  - Use clear, testable language (e.g., "The system shall...", "The application must...")
  - Include all commands, options, flags, and arguments for CLI tools
  - Specify input formats, output formats, and data structures
- **Non-Functional Requirements**: Performance, scalability, security, usability
- **User Stories** (optional but recommended): As a [user], I want [goal] so that [benefit]

#### C. Constraints
- **Technical Constraints**: Language version, dependencies, platform requirements
- **Design Constraints**: Architectural patterns, coding standards, libraries to use/avoid
- **External Constraints**: File system access, network requirements, environment variables
- **Performance Constraints**: Response time limits, memory limits, throughput requirements

#### D. Acceptance Criteria
- **Testable Conditions**: Clear pass/fail criteria for each requirement
- **Example Scenarios**: Concrete examples of inputs and expected outputs
- **Edge Cases**: How the system handles errors, invalid inputs, and boundary conditions
- **Success Metrics**: How will we know the implementation is correct and complete?

## Specification Writing Process

### Phase 1: Discovery
1. Ask clarifying questions about user needs and context
2. Understand existing systems, constraints, and integration points
3. Identify ambiguities and resolve them before writing the spec

### Phase 2: Drafting
1. Write the Overview section first to establish context
2. Document all Requirements systematically
3. List all Constraints that affect implementation
4. Define precise Acceptance Criteria for verification

### Phase 3: Review and Refinement
1. Present the specification to the user for review
2. Address feedback and questions
3. Iterate until all ambiguities are resolved
4. Get explicit user approval before proceeding to implementation

### Phase 4: Approval and Handoff
1. Mark the specification as "APPROVED" with date and version
2. Specification becomes the authoritative source of truth
3. Only after approval may implementation begin

## CLI Application Specification Guidelines

For command-line tools, the specification must include:

### Command Structure
```
command [subcommand] [options] [arguments]
```

### Required Details
- **All commands and subcommands**: Complete list with descriptions
- **All flags and options**: Short form (-f), long form (--flag), descriptions, default values
- **Arguments**: Required vs optional, data types, validation rules
- **Output format**: stdout, stderr, exit codes, file outputs
- **Error handling**: All error conditions and their messages
- **Configuration**: Config files, environment variables, precedence rules

### Example Format
```
Command: todo add <task_description>
Description: Adds a new task to the todo list
Arguments:
  - task_description (string, required): The task to add, max 500 characters
Options:
  - --priority, -p (string, optional): Set priority [low|medium|high], default: medium
  - --due, -d (date, optional): Due date in YYYY-MM-DD format
Output:
  - Success: "Task added: {task_description} (ID: {id})"
  - Error: "Invalid priority value" (exit code 1)
Exit Codes:
  - 0: Success
  - 1: Invalid input
  - 2: System error
```

## Backend System Specification Guidelines

For backend systems, the specification must include:

### API Endpoints
- HTTP method, path, description
- Request format (headers, body schema, query parameters)
- Response format (status codes, body schema)
- Authentication and authorization requirements
- Rate limiting and caching behavior

### Data Models
- All entities and their attributes
- Data types, constraints, validations
- Relationships between entities
- Indexes and query patterns

### Business Logic
- Algorithms and workflows
- State transitions
- Validation rules
- Error handling and recovery

### Integration Points
- External services and APIs
- Message queues and event systems
- Database interactions
- File system operations

## Quality Checklist

Before marking a specification as complete, verify:

- [ ] All sections (Overview, Requirements, Constraints, Acceptance Criteria) are present
- [ ] Every requirement is clear, unambiguous, and testable
- [ ] All edge cases and error conditions are documented
- [ ] Examples are provided for complex behaviors
- [ ] Technical constraints are explicitly listed
- [ ] Acceptance criteria are measurable and verifiable
- [ ] User has reviewed and approved the specification
- [ ] No implementation details or code exist yet

## Anti-Patterns to Avoid

### ❌ Don't:
- Write code before the spec is approved
- Leave requirements vague or open to interpretation
- Skip edge cases or error handling in the spec
- Mix specification with implementation details
- Assume implicit requirements without documenting them
- Create partial specs and "figure out the rest later"

### ✅ Do:
- Get explicit approval before coding
- Use precise, testable language
- Document all behaviors, including edge cases
- Separate "what" (spec) from "how" (implementation)
- Make all assumptions explicit
- Complete the entire specification before implementation

## Usage

Invoke this skill when:
1. Starting a new project or feature
2. User requests a specification or requirements document
3. Before writing any implementation code
4. When requirements are unclear and need formalization

## Output

The skill produces a complete specification document that:
- Serves as the authoritative source of truth
- Enables implementation without further clarification
- Provides clear acceptance criteria for validation
- Documents all decisions and constraints
- Can be used to generate test cases

## Success Criteria

A specification is complete when:
1. A developer could implement it without asking questions
2. A tester could create test cases directly from it
3. The user has explicitly approved it
4. All four mandatory sections are thoroughly documented
5. No ambiguities or "TBD" items remain
