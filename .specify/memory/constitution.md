<!--
SYNC IMPACT REPORT:
Version change: [Initial] → 1.0.0
Modified principles: N/A (Initial creation)
Added sections:
  - Core Principles (I-VI)
  - Technology Constraints
  - Phase Governance
  - Development Workflow
  - Governance
Templates requiring updates:
  ✅ plan-template.md - Constitution Check section references this file
  ✅ spec-template.md - Aligns with requirement discipline
  ✅ tasks-template.md - Aligns with phase/story structure
Follow-up TODOs: None
-->

# Evolution of Todo Constitution

## Core Principles

### I. Spec-Driven Development (NON-NEGOTIABLE)

No agent, tool, or human may write or modify code without following this mandatory sequence:

1. **Constitution** → Defines project-wide governance and principles (this document)
2. **Approved Specification** → Captures user requirements and acceptance criteria
3. **Approved Plan** → Documents architectural decisions and technical approach
4. **Approved Tasks** → Breaks down implementation into testable units

**Enforcement Rules**:
- If ambiguity exists at ANY level, refinement MUST happen at the specification level, NEVER in code
- No feature invention, assumption, or interpretation is permitted
- Agents may only implement what is explicitly defined and approved
- All deviations require spec amendment followed by re-approval

**Rationale**: Prevents scope creep, ensures traceability, maintains alignment between intent and implementation, and creates a single source of truth for all decisions.

### II. Agent Behavior Rules (NON-NEGOTIABLE)

Agents operate under strict constraints to ensure predictable, auditable outcomes:

- **No Manual Coding**: Humans do not write code under any circumstance; all implementation is agent-driven from approved artifacts
- **No Feature Invention**: Agents MUST NOT add features, capabilities, or "helpful improvements" beyond what is explicitly specified
- **No Assumptions**: When requirements are unclear or missing, agents MUST halt and request clarification rather than assume intent
- **No Deviation**: Agents MUST follow approved specifications, plans, and tasks exactly as written
- **Refactoring Constraints**: Refactoring is allowed ONLY when:
  - Required to satisfy an approved specification
  - Documented in the plan with explicit justification
  - Does not introduce new features or change behavior

**Rationale**: Maintains control, predictability, and auditability of the development process. Ensures AI agents remain tools that execute human decisions rather than autonomous decision-makers.

### III. Phase Governance (NON-NEGOTIABLE)

The Evolution of Todo project progresses through five strictly isolated phases:

**Phase Isolation Rules**:
- Each phase is a self-contained boundary with defined scope
- Phase I MUST NEVER contain features, architecture, or code from Phase II, III, IV, or V
- Future-phase ideas, suggestions, or "forward-compatible" designs MUST be ignored completely
- No "preparation" for future phases is permitted (no hooks, no abstractions, no placeholders)

**Phase Progression**:
- A phase is complete when ALL its specifications are implemented and tested
- Phase N+1 cannot begin until Phase N is complete and approved
- Moving to a new phase requires:
  1. New or updated specifications
  2. New architectural planning
  3. Approval of the new spec and plan
  4. Generation of new tasks

**Architecture Evolution**:
- Architecture may evolve between phases ONLY through updated specifications and plans
- Changes require the full spec-driven cycle: Constitution → Spec → Plan → Tasks
- Backward compatibility is NOT required between phases unless explicitly specified

**Rationale**: Prevents premature optimization, maintains focus on current deliverables, enables clean pivots between phases, and ensures each phase delivers complete, working functionality.

### IV. Technology Constraints

**Language**: Python 3.11+

**Storage**: In-memory only (no persistence layer permitted in Phase I)

**Testing Framework**: pytest

**Code Quality**:
- Type hints MUST be used for all function signatures
- Docstrings MUST follow Google style for all public functions and classes
- Maximum cyclomatic complexity: 10 per function
- Test coverage minimum: 80% for core logic

**Dependencies**:
- Standard library preferred
- Third-party dependencies require explicit justification in the plan
- No database libraries, ORMs, or persistence frameworks in Phase I

**Prohibited**:
- Global mutable state (except where explicitly required by specification)
- Hardcoded configuration (use environment variables or configuration objects)
- Silent error swallowing (all errors must be logged or propagated)
- Magic numbers (use named constants)

**Rationale**: Ensures code quality, maintainability, testability, and alignment with Python best practices. Restricts complexity to what is necessary for current phase requirements.

### V. Test-First Development (NON-NEGOTIABLE)

Testing follows a strict Test-Driven Development (TDD) cycle:

**Red-Green-Refactor Cycle**:
1. **Red**: Write tests that capture acceptance criteria → Tests MUST fail initially
2. **Green**: Implement minimum code to make tests pass → No additional features
3. **Refactor**: Improve code quality without changing behavior → Tests remain green

**Test Requirements**:
- Tests MUST be written BEFORE implementation code
- Tests MUST fail initially (proving they test the right thing)
- User MUST approve tests before implementation begins
- All acceptance criteria from specifications MUST have corresponding tests
- Tests MUST be deterministic, isolated, and fast

**Test Categories**:
- **Unit Tests**: Test individual functions and classes in isolation
- **Integration Tests**: Test component interactions and system behavior
- **Contract Tests**: Validate API contracts and interfaces (when applicable)

**Enforcement**:
- Commits containing implementation code without corresponding tests are invalid
- Implementation may not begin until test approval is received
- Test failures block progression to next task

**Rationale**: Ensures code correctness, provides living documentation, enables confident refactoring, and validates that specifications are testable and complete.

### VI. Simplicity and Minimalism

**YAGNI (You Aren't Gonna Need It)**:
- Implement only what is required by current phase specifications
- No "future-proofing" or "flexible architectures" for hypothetical requirements
- No abstractions until they are needed by at least two concrete use cases

**Start Simple**:
- Choose the simplest solution that satisfies requirements
- Prefer flat structures over hierarchies
- Prefer explicit code over clever abstractions
- Prefer composition over inheritance

**Complexity Justification**:
- Any deviation from simple solutions MUST be justified in the plan
- Justifications must reference specific requirements that necessitate complexity
- Alternative simpler approaches must be documented and reasons for rejection stated

**Rationale**: Reduces cognitive load, improves maintainability, accelerates development, and prevents over-engineering. Complexity is a cost that must be paid for with clear benefits.

## Technology Constraints

**Primary Language**: Python 3.11 or higher

**Dependency Policy**:
- Python standard library is preferred for all functionality
- Third-party dependencies require:
  - Explicit justification in the implementation plan
  - Security and maintenance considerations documented
  - Version pinning in requirements.txt

**Phase I Specific Constraints**:
- No file I/O (except for logging)
- No database connections
- No network calls
- No persistence mechanisms
- All state in-memory only
- Console-based interface only

**Code Organization**:
- Follow standard Python project structure
- Modules should be cohesive and loosely coupled
- Public APIs clearly distinguished from internal implementation

## Phase Governance

**Phase Boundaries**:
- **Phase I**: In-memory console Todo application with core CRUD operations
- **Phase II**: TBD (specification required before work begins)
- **Phase III**: TBD (specification required before work begins)
- **Phase IV**: TBD (specification required before work begins)
- **Phase V**: TBD (specification required before work begins)

**Current Phase**: Phase I

**Phase Transition Requirements**:
1. All Phase N specifications implemented and tested
2. All Phase N tests passing
3. Phase N+1 specification created and approved
4. Phase N+1 architectural plan created and approved
5. Phase N+1 tasks generated and approved
6. Explicit approval to begin Phase N+1 work

**Phase Isolation Enforcement**:
- Code reviews MUST verify no future-phase features present
- Specifications MUST NOT reference future phases
- Plans MUST NOT include preparation for future phases
- Tasks MUST NOT create infrastructure for future phases

## Development Workflow

**Specification Phase**:
1. User provides feature description
2. Agent generates specification using spec template
3. Specification includes user stories, requirements, success criteria
4. User reviews and approves specification
5. Specification locked (changes require amendment cycle)

**Planning Phase**:
1. Agent researches codebase and dependencies
2. Agent generates implementation plan using plan template
3. Plan includes architecture decisions, file structure, complexity justification
4. Significant architectural decisions flagged for ADR creation
5. User reviews and approves plan
6. Plan locked (changes require amendment cycle)

**Task Generation Phase**:
1. Agent generates tasks from approved plan and spec
2. Tasks organized by user story for independent implementation
3. Tasks include test-first requirements
4. User reviews and approves tasks
5. Tasks locked (changes require amendment cycle)

**Implementation Phase**:
1. For each task:
   - Write tests first (Red)
   - Get test approval from user
   - Implement minimum code to pass tests (Green)
   - Refactor for quality (Refactor)
   - Commit with clear message
2. User stories implemented independently and incrementally
3. Each story tested and validated before moving to next

**Quality Gates**:
- All tests must pass before task completion
- Code coverage must meet 80% threshold
- No linting errors permitted
- Type hints required for all public functions
- Documentation required for all public APIs

**Prompt History Records (PHR)**:
- MUST be created after every significant user interaction
- Captures: prompt, response, stage, files modified, decisions made
- Routed to appropriate directory: constitution/, feature-name/, or general/
- No placeholders permitted; all fields must be complete

**Architecture Decision Records (ADR)**:
- Created when significant architectural decisions are made
- Requires user consent (never auto-created)
- Documents: context, decision, alternatives considered, consequences
- Referenced in implementation plan

## Governance

**Constitutional Authority**:
- This constitution is the supreme authority for the Evolution of Todo project
- All specifications, plans, tasks, and code MUST comply with this constitution
- Conflicts between this constitution and other artifacts are resolved in favor of the constitution
- No tool, agent, or process may override constitutional requirements

**Amendment Process**:
1. Proposed change documented with rationale
2. Impact analysis performed (affected specs, plans, code)
3. User approval required for all amendments
4. Version number incremented according to semantic versioning:
   - **MAJOR**: Backward incompatible changes (removals, redefinitions)
   - **MINOR**: New principles or sections added
   - **PATCH**: Clarifications, typo fixes, non-semantic refinements
5. Sync impact report generated
6. Dependent artifacts updated (templates, existing specs, plans)
7. Amendment date recorded

**Compliance Verification**:
- All pull requests MUST verify constitutional compliance
- Code reviews MUST check for spec-driven process adherence
- Complexity MUST be justified in implementation plans
- Phase boundaries MUST be enforced

**Violation Handling**:
- Constitutional violations block merge/deployment
- Violations require:
  - Root cause analysis
  - Corrective action (fix code or amend constitution)
  - Documentation of lesson learned
  - Process improvement if systemic

**Runtime Guidance**:
- Development workflow details in `CLAUDE.md`
- Command execution procedures in `.specify/templates/commands/`
- Template structures in `.specify/templates/`
- Project memory in `.specify/memory/`

**Version**: 1.0.0 | **Ratified**: 2025-12-31 | **Last Amended**: 2025-12-31
