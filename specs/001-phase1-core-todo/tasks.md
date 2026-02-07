# Tasks: Phase I Core Todo Application

**Input**: Design documents from `/specs/001-phase1-core-todo/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), data-model.md, contracts/

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project structure per plan.md

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create src/ directory for source code
- [ ] T002 Create tests/unit/ directory for unit tests
- [ ] T003 Create tests/integration/ directory for integration tests
- [ ] T004 [P] Create requirements.txt with pytest dependency
- [ ] T005 [P] Create pyproject.toml with project metadata and pytest configuration
- [ ] T006 [P] Create .gitignore with Python standard ignores

**References**:
- Spec: CO-001 (Python 3.13+), CO-002 (stdlib only)
- Plan: Project Structure section, AD-006 (Testing Strategy)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T007 [P] Create TaskManager class skeleton in src/task_manager.py with __init__ method
- [ ] T008 [P] Create input validator functions in src/validators.py (validate_non_empty_string, validate_numeric_input)
- [ ] T009 [P] Create CLI helper functions in src/cli.py (display_menu, display_success, display_error, prompt_for_input)
- [ ] T010 Create main application loop skeleton in src/main.py with menu dispatch structure

**References**:
- Spec: FR-001 (menu interface), FR-010 (error messages), FR-011 (return to menu)
- Plan: AD-004 (Module Responsibility Separation), AD-003 (CLI Control Flow Pattern)
- Data Model: Task entity structure
- Contracts: TaskManager class structure, validators module, CLI module

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Task (Priority: P1) 🎯 MVP

**Goal**: Users can create tasks with title and description

**Independent Test**: Launch application, select "Add Task", enter details, verify task appears in list

**References**:
- Spec: User Story 1 (lines 10-23), FR-002, FR-003, FR-004, FR-017
- Plan: AD-001 (Data Storage), AD-002 (ID Generation), AD-005 (Error Handling)
- Data Model: Task entity fields, validation rules
- Contracts: add_task() method specification

### Implementation for User Story 1

- [ ] T011 [US1] Implement TaskManager.add_task() method in src/task_manager.py with ID generation using max() strategy
- [ ] T012 [US1] Implement TaskManager.get_all_tasks() method in src/task_manager.py returning tasks ordered by ID
- [ ] T013 [US1] Implement add_task operation in src/main.py: prompt for title and description, call TaskManager.add_task(), display success message
- [ ] T014 [US1] Add input validation for add_task: validate title non-empty using validate_non_empty_string()
- [ ] T015 [US1] Add input validation for add_task: validate description non-empty using validate_non_empty_string()
- [ ] T016 [US1] Add error handling in add_task operation: catch ValueError for empty inputs, display error message, return to menu

**Acceptance Criteria**:
- Task created with unique sequential ID starting from 1
- Task status set to "incomplete" by default
- Empty or whitespace-only title/description rejected with error message
- Success message displays task ID
- Application returns to main menu after operation

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Task List (Priority: P1) 🎯 MVP

**Goal**: Users can view all their tasks in creation order

**Independent Test**: Add several tasks, select "View Tasks", verify all tasks displayed with correct details

**References**:
- Spec: User Story 2 (lines 26-39), FR-005, FR-018
- Plan: AD-001 (Data Storage), Implementation Notes (CLI Output Format)
- Contracts: get_all_tasks() method, display_tasks() function

### Implementation for User Story 2

- [ ] T017 [US2] Implement display_tasks() function in src/cli.py to format and display task list
- [ ] T018 [US2] Add empty list handling in display_tasks(): show "No tasks found. Your task list is empty."
- [ ] T019 [US2] Add non-empty list handling in display_tasks(): show header with count, format each task with ID, title, description, status
- [ ] T020 [US2] Implement view_tasks operation in src/main.py: call get_all_tasks(), call display_tasks()

**Acceptance Criteria**:
- Empty task list displays appropriate message
- Non-empty list shows task count in header
- Each task displays with [ID] prefix, title, description, and status
- Tasks displayed in creation order (ID ascending)
- Application returns to main menu after operation

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently (MVP complete!)

---

## Phase 5: User Story 3 - Mark Complete/Incomplete (Priority: P2)

**Goal**: Users can mark tasks as complete or incomplete

**Independent Test**: Create tasks, mark complete, verify status change in list, mark incomplete again

**References**:
- Spec: User Story 3 (lines 42-55), FR-006, FR-009
- Plan: AD-005 (Error Handling)
- Data Model: Status field, state transitions
- Contracts: mark_task_complete(), mark_task_incomplete(), get_task_by_id()

### Implementation for User Story 3

- [ ] T021 [P] [US3] Implement TaskManager.get_task_by_id() method in src/task_manager.py, raise KeyError if not found
- [ ] T022 [P] [US3] Implement TaskManager.mark_task_complete() method in src/task_manager.py, set status to "complete"
- [ ] T023 [P] [US3] Implement TaskManager.mark_task_incomplete() method in src/task_manager.py, set status to "incomplete"
- [ ] T024 [US3] Implement mark_complete operation in src/main.py: prompt for ID, validate numeric, call mark_task_complete(), display success
- [ ] T025 [US3] Implement mark_incomplete operation in src/main.py: prompt for ID, validate numeric, call mark_task_incomplete(), display success
- [ ] T026 [US3] Add error handling for mark operations: catch ValueError for non-numeric ID, KeyError for not found, display appropriate error messages

**Acceptance Criteria**:
- Task status changes from "incomplete" to "complete" when marked complete
- Task status changes from "complete" to "incomplete" when marked incomplete
- Non-numeric ID displays "Task ID must be a number" error
- Non-existent ID displays "Task ID [X] not found" error
- Status change immediately visible in next view operation
- Application returns to main menu after operation

**Checkpoint**: All user stories (US1, US2, US3) should now be independently functional

---

## Phase 6: User Story 4 - Update Task (Priority: P3)

**Goal**: Users can update task title and/or description

**Independent Test**: Create task, update title/description, verify changes in list

**References**:
- Spec: User Story 4 (lines 58-71), FR-007, FR-009, FR-017
- Plan: AD-005 (Error Handling)
- Data Model: Validation rules for title and description
- Contracts: update_task() method specification

### Implementation for User Story 4

- [ ] T027 [US4] Implement TaskManager.update_task() method in src/task_manager.py: accept task_id, optional title, optional description
- [ ] T028 [US4] Add update_task validation: if title provided, validate non-empty; if description provided, validate non-empty
- [ ] T029 [US4] Implement update_task operation in src/main.py: prompt for ID, prompt for new title (allow empty to skip), prompt for new description (allow empty to skip)
- [ ] T030 [US4] Add update_task logic: if user presses Enter without input, pass None for that field to keep current value
- [ ] T031 [US4] Add error handling for update_task: catch ValueError for empty inputs, KeyError for not found, display appropriate error messages

**Acceptance Criteria**:
- Title can be updated while preserving description and status
- Description can be updated while preserving title and status
- Both title and description can be updated simultaneously
- Pressing Enter without input keeps current value
- Empty or whitespace-only new values rejected with error
- Non-existent ID displays error
- ID and status never change via update
- Application returns to main menu after operation

**Checkpoint**: User Stories 1-4 should all be independently functional

---

## Phase 7: User Story 5 - Delete Task (Priority: P3)

**Goal**: Users can permanently delete tasks

**Independent Test**: Create tasks, delete specific task by ID, verify it no longer appears in list

**References**:
- Spec: User Story 5 (lines 74-87), FR-008, FR-009
- Plan: AD-005 (Error Handling), AD-002 (ID never reused after deletion)
- Contracts: delete_task() method specification

### Implementation for User Story 5

- [ ] T032 [US5] Implement TaskManager.delete_task() method in src/task_manager.py: remove task by ID, raise KeyError if not found
- [ ] T033 [US5] Implement delete_task operation in src/main.py: prompt for ID, validate numeric, call delete_task(), display success message
- [ ] T034 [US5] Add error handling for delete_task: catch ValueError for non-numeric ID, KeyError for not found, display appropriate error messages

**Acceptance Criteria**:
- Task permanently removed from list
- Deleted task does not appear in subsequent view operations
- Only specified task deleted, others remain unchanged
- Non-numeric ID displays error
- Non-existent ID displays error
- Task ID never reused for new tasks (verified by ID generation using max())
- Application returns to main menu after operation

**Checkpoint**: All five user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories and final application completeness

- [ ] T035 [P] Add Exit operation in src/main.py: display goodbye message, break from main loop
- [ ] T036 [P] Add invalid menu choice handling in src/main.py: display "Error: Invalid option. Please select a number between 1 and 7."
- [ ] T037 [P] Add type hints to all functions in src/task_manager.py
- [ ] T038 [P] Add type hints to all functions in src/validators.py
- [ ] T039 [P] Add type hints to all functions in src/cli.py
- [ ] T040 [P] Add type hints to main() function in src/main.py
- [ ] T041 [P] Add Google-style docstrings to all public functions in src/task_manager.py
- [ ] T042 [P] Add Google-style docstrings to all public functions in src/validators.py
- [ ] T043 [P] Add Google-style docstrings to all public functions in src/cli.py
- [ ] T044 Verify all error messages match specification exactly
- [ ] T045 Verify menu format matches specification exactly
- [ ] T046 Verify task list display format matches specification exactly
- [ ] T047 Manual test: Run full application workflow (add, view, update, delete, mark complete/incomplete, exit)
- [ ] T048 Verify constitutional compliance: no persistence, in-memory only, Python 3.13+, type hints present, docstrings present

**References**:
- Spec: FR-010 (error messages), FR-011 (return to menu), FR-012 (exit option)
- Plan: Type Hints Strategy, Docstring Format, CLI Output Format, Error Messages
- Constitution: Code Quality requirements (type hints, docstrings, complexity ≤10, coverage ≥80%)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-7)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (US1 → US2 → US3 → US4 → US5)
- **Polish (Phase 8)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - Integrates with US1 (uses get_all_tasks from US1)
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - Integrates with US1 (uses get_task_by_id)
- **User Story 4 (P3)**: Can start after Foundational (Phase 2) - Integrates with US1 (uses get_task_by_id)
- **User Story 5 (P3)**: Can start after Foundational (Phase 2) - Integrates with US1 (uses get_task_by_id)

**Note**: All user stories technically depend on US1 completing the TaskManager.add_task() and get_all_tasks() methods, but tasks are organized to implement shared methods in US1's phase.

### Within Each User Story

- Foundation methods before operations
- Validation before business logic
- Error handling after core implementation
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks (T001-T006) marked [P] can run in parallel
- All Foundational tasks (T007-T009) marked [P] can run in parallel (T010 depends on T009)
- Within US1: Tasks T011-T012 can run in parallel (both TaskManager methods)
- Within US3: Tasks T021-T023 can run in parallel (all TaskManager methods, different operations)
- Within US4: No parallel opportunities (sequential dependency)
- Within US5: No parallel opportunities (sequential dependency)
- Within Polish: Tasks T035-T043 marked [P] can run in parallel

---

## Parallel Example: User Story 1

```bash
# Launch TaskManager methods together:
Task: "Implement TaskManager.add_task() method in src/task_manager.py"
Task: "Implement TaskManager.get_all_tasks() method in src/task_manager.py"

# Then continue with main.py integration sequentially
```

---

## Parallel Example: User Story 3

```bash
# Launch all TaskManager methods for US3 together:
Task: "Implement TaskManager.get_task_by_id() method in src/task_manager.py"
Task: "Implement TaskManager.mark_task_complete() method in src/task_manager.py"
Task: "Implement TaskManager.mark_task_incomplete() method in src/task_manager.py"

# Then integrate into main.py sequentially
```

---

## Implementation Strategy

### MVP First (User Stories 1 & 2 Only)

1. Complete Phase 1: Setup (T001-T006)
2. Complete Phase 2: Foundational (T007-T010)
3. Complete Phase 3: User Story 1 - Add Task (T011-T016)
4. Complete Phase 4: User Story 2 - View Task List (T017-T020)
5. **STOP and VALIDATE**: Test US1 and US2 independently
6. Deploy/demo if ready (MVP complete!)

**MVP Scope**: Add and view tasks - minimal viable product

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 (Add) + User Story 2 (View) → Test independently → MVP! ✅
3. Add User Story 3 (Mark Complete/Incomplete) → Test independently → Enhanced functionality
4. Add User Story 4 (Update) → Test independently → Quality of life improvement
5. Add User Story 5 (Delete) → Test independently → Full CRUD complete
6. Complete Polish phase → Production-ready application
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1 + User Story 2 (MVP pair)
   - Developer B: User Story 3 (Mark operations)
   - Developer C: User Story 4 (Update)
   - Developer D: User Story 5 (Delete)
3. All converge on Polish phase
4. Stories complete and integrate independently

---

## Task Count Summary

- **Total Tasks**: 48
- **Setup (Phase 1)**: 6 tasks
- **Foundational (Phase 2)**: 4 tasks
- **User Story 1 (Phase 3)**: 6 tasks
- **User Story 2 (Phase 4)**: 4 tasks
- **User Story 3 (Phase 5)**: 6 tasks
- **User Story 4 (Phase 6)**: 5 tasks
- **User Story 5 (Phase 7)**: 3 tasks
- **Polish (Phase 8)**: 14 tasks

**Parallel Opportunities**: 18 tasks marked [P] can run in parallel within their phases

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence

---

## Validation Checklist

✅ All tasks follow format: `- [ ] [ID] [P?] [Story?] Description with file path`
✅ Tasks organized by user story (Phases 3-7)
✅ Each user story has: goal, independent test criteria, implementation tasks
✅ Setup and Foundational phases complete before user stories
✅ Dependencies documented (phase and within-story)
✅ Parallel opportunities identified and marked [P]
✅ File paths included in all implementation tasks
✅ References to spec sections, plan sections, data model, and contracts included
✅ MVP scope clearly identified (US1 + US2)
✅ Incremental delivery strategy documented
✅ Total task count provided (48 tasks)
✅ No new features beyond specification
✅ No future phase references
✅ Constitutional compliance task included (T048)
