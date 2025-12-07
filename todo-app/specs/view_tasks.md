## View Tasks Specification

### Feature
Users should be able to view a list of all current todo tasks, including their ID, title, description, and status.

### Input
- User selects 'view' option from the main menu.

### Process
1. Retrieve all tasks from the in-memory task list.
2. Format each task's details for display.

### Output
- A formatted list of tasks, each showing: `ID | Title | Description | Status`.
- Status should clearly indicate 'Complete' or 'Pending'.
- If no tasks exist, a message: 'No tasks to display.'
