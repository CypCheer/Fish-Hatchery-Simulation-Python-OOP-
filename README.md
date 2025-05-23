# Fish Hatchery Simulation Project

## Overview

The Fish Hatchery Simulation Project is a Python-based program designed to simulate the operations of a fish farming. 
It allows users to choose sell several type of fishes, manage technicians, monitor resources, and handle to maintain 
profitability and avoid going bankrupt. The simulation provides users to manage multiple aspects of hatchery management, 
including: 

- Adding and Removing technicians. 
- Managing fish sales based on demand, resource availability, and technician time. 
- Refilling resources by purchasing supplies from vendors. 
- Handling resource depreciation and warehouse costs. This project shows the principles of Object-Oriented
  Programming (OOP) and provides an interactive user experience while maintaining structured and reusable code.


## Code Design

The structure of the code is organized into several files, each file represents a specific component of the hatchery 
simulation. The design make sure the scalability, maintenance, and clarity and reusability.


## Key Components

### 1. Object-Oriented Design

The project bases on object-oriented programming (OOP) principles to structure the simulation. 
There are five major classes used, including:
 
1.1 Fish
	
- This class represents the types of fish in the hatchery, including their information that 
  relate to each fish type such as maintenance requirements, feed, fertilizer, salt, demand, and price.

1.2 Technicians

- This class manages technician attributes such as name, weekly rate, and specialization 
of each technician in specific fish types.
	
1.3 Warehouse
	
- This class handles storage for resources including, fertilizer, feed, and salt. It manages 
resource depreciation, refilling, and storage costs.
	
1.4 Vendor
- This class shows vendors that user will choose that which vendors they will choose to buy supplies.

1.5 Hatchery
- This class is the central system for the simulation. It work with fish sales, resource management, 
technician payments, and working with other classes.


### 2. Error Handling

2.1 Input Validation
	
- The program includes robust input validation to ensure that only valid data is accepted from the user. 
For example:
- To ensure that numeric inputs are within acceptable ranges.
- To check for the same technician names or invalid fish types before performing operations.
	
2.2 Useful Feedback
	
- When an error occurs the program will provide messages to inform the user understand and correct the issue.

### 3. Modular Structure
	
Each component is stored in its file. The outline of the project's structure including:
	
- Fish.py contains the Fish class to manage fish types and their properties.
- Technician.py defines the Technicians class to handle technician information and actions.
- Warehouse.py includes the Warehouse class to manage resource storage and costs.
- Vendor.py implements the Vendor class for buying resources.
- Hatchery.py contains the Hatchery class, which integrates all components and simulates the operations.
- main.py is the entry point for the simulation, gather other modules to work together and interact with users. 
For example, It extract fish data from Fish.py, handles technician addition or removal by using Technician.py, 
manages resources via Warehouse.py, and helps resource purchases via Vendor.py.


## Design Decisions

- Separate each part into individual files to ensure the better readability and simplifies debugging. For instance, 
if a bug occurs in the Warehouse module, it can be checked only in module, do not check in other modules. Additionally,
utilizing classes to gather data and the related work in the same area. This makes the code easy to understand and 
convenient to add the new functions.

## Description of Files

### 1. main.py
	
Purpose:
- main.py is the central control the simulation. It works between all other modules such as Fish, Technicians, 
Warehouse, Vendor, Hatchery, and ensures that the hatchery management simulation execute smoothly.

Responsibilities:

- Prompts the user to input the number of quarters to simulate, while it ensures that input is valid to handle errors, 
such as invalid or negative inputs.
- Manages technician adding, removing, and technician’s speciality and making sure that the number of technician is between 1 to 5
- Facilitates fish sales and resource purchases, while consider technician avaiability and the quantity of resources 
and also adjusts the hatchery's cash balance based on sales revenue
- Applying depreciation rate of resource and warehouse cost calculations. Using input from the user to select a vendor and 
calculates costs based on the chosen vendor's pricing.
- Computes and deducts warehouse storage costs based on the quantity of resources stored in both the main and auxiliary warehouses.
- Manages the payment of technician salaries for each quarter and ensures that the cash balance is sufficient.
- The simulation will stop if the hatchery goes bankrupt.

	
The advantages:

- Separating logic into a main script simplifies interaction and testing.
- It keeps the simulation flow separate from the core logic of individual components
- Additional features (e.g., new types of fish, resources, or vendors) can be added to their modules without modifying main.py.
- Providing clear feedback to the user at every step of the simulation (e.g., resource levels, sales summaries, cash balance).

	
### 2. Fish.py
	
Purpose:
- The Fish.py file determines the Fish class, which is responsible for managing all fish details within the hatchery system. 
It contains important information such as the resources, demand, and sale prices for different fish species.

Attributes:
		
- fish_data (Dictionary): Keeps information about various fish species and each fish type has specific details including:
	- Fertilizer is keeping the amount of fertilizer per unit.
	- Feed is keeping amount of feed per unit.
	- Salt is keeping amount of salt per unit.
	- Maintenance Time is keeping the number of days needed to maintain one unit of fish.
	- Demand is keeping the demand for each type of fish, which will reset every quarter.
	- Price is keeping the selling price per unit of fish
			
Methods:
		
- reset_fish_demand:
	- Resets the demand for all fish types to their default values at the beginning of each quarter.
	- Uses a pre-defined dictionary default_demand to restore values.
		
The advantages:
	
- The dictionary structure allows to add new fish types easily.
- Separating fish logic into its own class keeps the main code clean.


### 3. Technician.py
	
Purpose:
- The Technician.py file contains the definition for the Technicians class. This class is responsible for managing hatchery staff, 
including their details, such as name, salary, and specialization for specific type of fishes.
	
Attributes:

- name (String): It shows the name of the technician, which is used to identify each technician within the system.
- weekly_rate (Integer): The weekly salary for the technician is £500, but this can be changed when creating a technician object.
- speciality (String or None): This is for indicating the fish type that the technician specializes in. The speciaization helps in 
  enhancing quality of operations like reducing maintenance time for specific fish types. If the technician has no specialization, 
  the value is set to None.

Methods:

- __init__: The constructor method starts technician objects with the provided name, weekly salary, and specialization. It ensures that 
	  every technician is defined by their attributes. 

The advantages:
	
- Using a Class: Group all information about the technicians is grouped in one place. This makes it easier to add new features 
	   in the future, like tracking their work or performance.
- Keeping Things Separate: The file only deals with technician-related details. This makes the code clean and organized. 


### 4. Warehouse.py
	
Purpose:
- The Warehouse.py file contains the Warehouse class. This class is incharge of management of resources like fertilizer, feed, 
and salt. It keeps track of how much of each resource is stored, handles storage limits, and applies depreciation over time.

Attributes:

- supplies (Dictionary)
	- Tracks the current quantity of each resource in the warehouse. This value will be updated when resources are used, 
	  refilled, or depreciated.
- capacity (Dictionary)
	- The maximum amount of each resource that the warehouse can store to ensure that resources cannot exceed this limit when refilled.
- depreciation_rate (Dictionary)
	- The rate at which resources decrease over time. This makes sure that unused resources are not unlimited.
- storage_cost_rate (Dictionary)
	- The cost of storing resources, calculated per unit of resource. This cost is applied to simulate real-world expenses in the hatchery.


Methods:
	
- depreciate_resources()
	- Reduces the quantity of resources stored in the warehouse based on the depreciation rate to make sure that resource quantities 
	do not go below zero. The working processes including:
	1. Multiply the current quantity of each resource by its depreciation rate. 
	2. Subtract the calculated amount from the current quantity. For instance, if you have 50 units of fertilizer with a 10% 
	depreciation rate: Depreciation = 50 * 0.1 = 5 and New fertilizer quantity = 50 - 5 = 45.

- refill_resources(resource, amount)
	- Adds more of a resource to the warehouse to make sure that total quantity does not exceed the warehouse’s maximum capacity. 
	The working processes including: 1. Calculate the available space in the warehouse for that resource. 2. Add the resource 
	quantity up to the available space. 3. Return any leftover quantity that could not be stored. For instance, if the warehouse 
	has 60 units of feed and the maximum capacity is 100: Available space = 100 - 60 = 40. If you add 50 units, only 40 can be stored then 
	the remaining amount = 50 - 40 = 10.


The advantages:

- By placing all resource-related logic in the Warehouse class, the main program remains clean and easy to read. Additionally, any future updates 
(e.g., adding new resources or changing storage rules) can be done within this class without affecting other parts of the code.
- The depreciation logic ensures that resources do not last forever, adding realism to the simulation and refilling logic prevents 
overloading the warehouse, maintaining practical constraints.
- If the simulation requires more complex storage rules or additional resource types, this class can be expanded without affecting other 
components. For example, we can add tracking for multiple warehouses or implement dynamic storage costs based on demand.


### 5. Vendors.py
	
Purpose:
- The Vendors.py file contains the Vendor class. This class shows vendors who sell resources sych as fertilizer, feed, and salt 
to the hatchery. It manages the vendor's details and the price f the resources.

Attributes:

- name (String)
	- Stores the name of the vendor. This makes it easier to identify which vendor the user is buy supplies with during the simulation.
- prices (Dictionary)
	- Stores the price for each resource that the vendor offers. However, prices vary between vendors, allow the user 
	to choose based on cost.


Methods:

- calculate_cost(resource, quantity)
	- Calculate the total cost for purchasing a specified amount of a resource. The method multiplies the price of the resource 
	by the quantity requested and returns the total cost. This medthod include teo paramethers, including resource (String) and 
	quantity (Integer), For example, if a vendor sells fertilizer for £0.30 per unit, buying 100 units would cost: cost = 0.30 * 100 = £30.00.

	
The advantages:
	
- The design of the Vendor class helps make the code simple, realistic, and easy to expand. 
	- All related vendor tasks like calculating costs, are in a separate class. This keeps the main simulation code clean and easy to manage. 
	The Hatchery class doesn’t need to handle cost calculations directly, making the system modular.
	- Each vendor has unique prices for resources like fertilizer, feed, and salt. This makes the simulation realistic because users can 
	compare vendors and pick the most affordable vendor.
	- Adding new resources or vendors is simple and requires minimal changes. You can also add new features, like discounts or delivery times, 
	without affecting other parts of the program.
	- By separating vendor details, users can compare prices easily and make better strategic choices during the simulation.


### 6. Hatchery.py
	
Purpose:
- The Hatchery class is the main class that manages all hatchery operations. It is in chrage of  co-working with cash, 
resources, technicians, and fish sales.

Attributes:

- cash_balance: Tracks how much money is available for operations.
- technicians: A list of Technician objects who manage fish and resources.
- warehouse_cost: The fixed cost of maintaining warehouses each quarter.
- sales: Keeps a record of fish sold during each quarter.
- fish_data: Contains fish details from the Fish class.
- warehouses: A dictionary holding multiple Warehouse objects that store resources like fertilizer, feed, and salt.
- vendors: A dictionary with Vendor objects that provide resources for purchase.

Methods:
	
- add_technician
	- Adds a new technician to the team, while making sure that no duplicate names and allows specifying a fish speciality.
- remove_technician
	- Removes a technician by their name and also checks if the technician exists before removing.
- sell_fish
	- Manages the sale of fish while ensuring there are enough resources and technician availability. 
	Finally, updates cash balance, resource levels, and sales data after each sale.
- calculate_storage_cost
	- Deducts warehouse storage costs from the cash balance and calculates costs based on the amount of resources stored.
- Depreciation
	- Applies depreciation to warehouse resources to simulate storage decay.
- calculation_total_payment
	- Calculates and deducts the total salaries paid to technicians, while checking that the hatchery 
	can afford to pay its technician.


The advantages:

- The Hatchery class handles all core operations such as adding technician, managing resources, and selling fish. 
It provides a single location for managing the simulation, making the code easier to follow.
- The Hatchery class interacts with other classes (Fish, Technician, Warehouse, and Vendor) to perform specific tasks. 
Each task is handled by its class, keeping the code organized and easy to test.
- Storage costs, and technician payments, the simulation looks realistic bacause of calculating depreciation. The class can easily adapt to new features, such as adding new fish species or expanding vendor options.
- The methods are designed to handle user input such as adding or removing technicians or selling fish, 
while validating errors. This makes the simulation runs smoothly and remains flexible for future updates.


## How to Run the Code

To run the Fish Hatchery Simulation Project, follow these steps:

### 1. Ensure Python is Installed:
- The code is written in Python 3, ensure you have Python 3 installed on your device.
- To verify, open a terminal or command prompt and type: python --version or python3 --version

### 2. Set Up the Project Directory:
- Create a folder named fish_hatchery_simulation (or any other name you prefer).
- Place all the .py files (main.py, Fish.py, Technicians.py, Warehouse.py, Vendor.py, Hatchery.py) and 
	the README.md file in the same folder.

### 3. Navigate to the Project Directory:
- Open a terminal or command prompt.
- Use the cd command to navigate to the project directory. For example: cd path/to/fish_hatchery_simulation

### 4. Run the Program:
- Execute the main.py file using Python. For example: python main.py or python3 main.py

### 5. Follow the Interactive Prompts:
- The program will prompt you to enter the number of quarters for the simulation.
- Next, you can manage technicians, sell fish, purchase resources, and monitor cash flow.
- Enter appropriate inputs as guided by the program.

### 6. Simulation Ends:
- The simulation ends when:
- The specified number of quarters is completed.
- The hatchery goes bankrupt (cash balance drops below £0).


## GitHub Repository

- [Link to Repository](https://github.com/sx24318-EMATM0048/sx24318_EMATM0048)
