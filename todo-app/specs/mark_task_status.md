## Mark Task Complete/Incomplete Specification

### Feature
Users should be able to change the status of a task (mark as complete or incomplete) identified by its ID.

### Input
- User selects 'mark' option from the main menu.
- Prompts for 'Task ID to mark:' (integer, mandatory).
- Prompts for 'Mark as complete? (yes/no):' (string, mandatory, case-insensitive).

### Process
1. Find the task corresponding to the provided ID.
2. Update the task's status based on user input ('Complete' or 'Pending').

### Output
- Confirmation message: 'Task [ID] marked as [status] successfully.'
- If task ID is not found, an error message: 'Task with ID [ID] not found.'
- If invalid input for complete/incomplete, an error message: 'Invalid input. Please enter 'yes' or 'no'.'
