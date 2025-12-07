## Delete Task Specification

### Feature
Users should be able to delete an existing task identified by its ID.

### Input
- User selects 'delete' option from the main menu.
- Prompts for 'Task ID to delete:' (integer, mandatory).

### Process
1. Find and remove the task corresponding to the provided ID from the in-memory task list.

### Output
- Confirmation message: 'Task [ID] deleted successfully.'
- If task ID is not found, an error message: 'Task with ID [ID] not found.'
