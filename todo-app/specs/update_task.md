## Update Task Specification

### Feature
Users should be able to update the title and/or description of an existing task identified by its ID.

### Input
- User selects 'update' option from the main menu.
- Prompts for 'Task ID to update:' (integer, mandatory).
- Prompts for 'New Title (leave blank to keep current):' (string, optional).
- Prompts for 'New Description (leave blank to keep current):' (string, optional).

### Process
1. Find the task corresponding to the provided ID.
2. If a new title is provided, update the task's title.
3. If a new description is provided, update the task's description.

### Output
- Confirmation message: 'Task [ID] updated successfully.'
- If task ID is not found, an error message: 'Task with ID [ID] not found.'
- If neither title nor description is provided, a message: 'No changes specified for task [ID].'
