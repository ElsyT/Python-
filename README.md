Inventory, Finance Calculator, and Task Manager
Welcome to the Documentation for the Python Project Suite: Inventory, Finance Calculator, and Task Manager.

Table of Contents
Introduction
Inventory
File Structure
Class: Shoes
Functions
Finance Calculator
Functions
Task Manager
User Interaction
Functions
Integration
Menu
Admin Features
Reporting
1. Introduction<a name="introduction"></a>
This project comprises three modules: Inventory, Finance Calculator, and Task Manager, designed to enhance organization and productivity. Each module serves a specific purpose, offering comprehensive functionality.

2. Inventory<a name="inventory"></a>
File Structure<a name="file-structure"></a>
inventory.py: Core module for managing inventory data.
inventory.txt: Text file storing inventory data.
Class: Shoes<a name="class-shoes"></a>
Inside inventory.py, the class Shoes is defined with attributes:

country
code
product
cost
quantity
Functions<a name="functions"></a>
get_cost()
Returns the cost of the shoes.

get_quantity()
Returns the quantity of the shoes.

__str__()
Returns a string representation of the class.

3. Finance Calculator<a name="finance-calculator"></a>
Functions<a name="functions-finance"></a>
value_per_item(): Calculates the total value for each item in the inventory.
4. Task Manager<a name="task-manager"></a>
User Interaction<a name="user-interaction"></a>
add_user(): Registers a new user.
add_task(): Adds a new task for the selected user.
view_all_tasks(): Displays all tasks assigned to users.
view_mine(): Displays tasks assigned to the logged-in user.
complete_task(): Allows users to mark a task as complete.
Functions<a name="functions-tasks"></a>
reg_user(): Ensures unique usernames and adds new users.
add_task_to_user(): Assigns tasks to specific users.
display_tasks(): Displays tasks based on user or completion status.
edit_due_date(): Edits the due date for a specific task.
5. Integration<a name="integration"></a>
Menu<a name="menu"></a>
main_menu(): Main menu for selecting modules.
inventory_menu(): Sub-menu for inventory-related actions.
finance_menu(): Sub-menu for finance-related actions.
task_menu(): Sub-menu for task-related actions.
Admin Features<a name="admin-features"></a>
generate_reports(): Creates reports for inventory and task data.
Reporting<a name="reporting"></a>
inventory_report(): Generates a report on current inventory status.
task_report(): Generates a report on task completion and pending tasks.
