# CLAUDE.md - Claude Code Instructions (Simulated)

This project simulates the use of Claude Code and Spec-Kit Plus for spec-driven development. In a real scenario, these tools would assist in generating code and specifications. Here, we document the process as if these tools were actively used.

## Specification Generation

For each feature, a detailed specification (found in the `specs/` directory) was written first. These specs describe the desired behavior, input, and expected output for each operation.

Example specification for adding a task (`specs/add_task.md`):

```markdown
## Add Task Specification

### Feature
Users should be able to add a new todo task including a title and an optional description.

### Input
-   User selects 'add' option from the main menu.
-   Prompts for 'Task Title:' (string, mandatory).
-   Prompts for 'Task Description:' (string, optional).

### Process
1.  Generate a unique ID for the new task.
2.  Create a new task object with the provided title, description, a 'pending' status, and the generated ID.
3.  Add the new task to the in-memory task list.

### Output
-   Confirmation message: 'Task "[title]" added with ID: [ID].'
-   If title is empty, an error message: 'Task title cannot be empty.'
```

## Code Development with Claude Code (Simulated)

Following the specifications, Python code was developed in the `src/` directory. Each function directly addresses the requirements outlined in its corresponding spec. The goal was to write minimal boilerplate and focus on implementing the specified logic.

## Spec-Kit Plus Integration (Simulated)

In a real-world scenario, Spec-Kit Plus would likely be used to validate the implementation against the specifications, perhaps through automated tests generated from the specs themselves. For this project, manual verification against the written specs ensures adherence to the design.
