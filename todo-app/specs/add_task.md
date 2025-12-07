## Add Task Specification

### Feature
Users should be able to add a new todo task including a title and an optional description.

### Input
- User selects 'add' option from the main menu.
- Prompts for 'Task Title:' (string, mandatory).
- Prompts for 'Task Description:' (string, optional).

### Process
1. Generate a unique ID for the new task.
2. Create a new task object with the provided title, description, a 'pending' status, and the generated ID.
3. Add the new task to the in-memory task list.

### Output
- Confirmation message: 'Task "[title]" added with ID: [ID].'
- If title is empty, an error message: 'Task title cannot be empty.'
