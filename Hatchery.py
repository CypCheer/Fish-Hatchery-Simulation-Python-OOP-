"""
Filename: hatchery.py
Author: Chayaporn Makchuay
Date: 16 November 2024
Description:
    This module defines the Hatchery class, which manages the operations
    of the fish hatchery, including technicians, resources, and cash balance.
"""

from Technician import Technicians
from Warehouse import Warehouse
from Vendors import Vendor

class Hatchery:
    """
    This class represents a hatchery for managing resources, technicians, 
    warehouses, and fish sales.

    Attributes:
    - cash_balance (float): current cash balance of the hatchery.
    - technicians (list): list of technician objects.
    - warehouse_cost (float): fixed quarterly cost for warehouse maintenance.
    - sales (dict): tracks fish sales by type.
    - fish_data (object): an instance of the 'Fish' class include fish details.
    - warehouses (dict): dictionary of 'Warehouse' objects for managing resources.
    - vendors (dict): dictionary of 'Vendor' objects for buying resources.
    """

    def __init__(self, cash_balance, fish_data):
        """
        Beginning the Hatchery class with attributes.

        Args:
            cash_balance (float): cash balance for the hatchery.
            fish_data (object): instance of the 'Fish' class that contain 
                                fish details.
        """
        self.cash_balance = cash_balance
        self.technicians = []
        self.warehouse_cost = 1500
        self.sales = {}
        self.fish_data = fish_data

        self.warehouses = {
            'main': Warehouse(
                {'fertilizer': 20, 'feed': 400, 'salt': 200},
                {'fertilizer': 0.4, 'feed': 0.1, 'salt': 0.0},
                {'fertilizer': 0.1, 'feed': 1.0, 'salt': 1.0}  
            ),
            'auxiliary': Warehouse(
                {'fertilizer': 10, 'feed': 200, 'salt': 100},
                {'fertilizer': 0.4, 'feed': 0.1, 'salt': 0.0},
                {'fertilizer': 0.1, 'feed': 1.0, 'salt': 1.0} 
            )
        }

        self.vendors = {
            'Slippery Lakes': Vendor(
                'Slippery Lakes', {'fertilizer': 0.30, 'feed': 0.10, 'salt': 0.05}
            ),
            'Scaly Wholesaler': Vendor(
                'Scaly Wholesaler', {'fertilizer': 0.20, 'feed': 0.40, 'salt': 0.25}
            ),
        }

    def update_cash_balance(self):
        """
        Updates the cash balance by rounding it to two decimal places.
        """
        self.cash_balance = round(self.cash_balance, 2)

    def calculate_warehouse_cost(self):
        """
        Subtract the fixed warehouse cost from the cash balance and prints a summary.
        """
        self.cash_balance -= self.warehouse_cost 
        self.update_cash_balance() 
        print(f"Paid rent/utilities {self.warehouse_cost}")   
        print(f"Remainding cash balance: {self.cash_balance}") 

    def depreciation(self):
        """
        Reducing their resource quantity by Applying depreciation.
        """
        for name, warehouse in self.warehouses.items():
            warehouse.depreciate_resources() 
            print(f"{name.capitalize()} after depreciation: {warehouse.supplies}")
   
    def add_technician(self, name=None, weekly_rate=500, speciality=None):
        """
        Adds a technician to the hatchery and check whether that technician
        have speciality or not. This will add new technicians object.
        This will ensure that names are unique and valid technician details 
        are added.

        Args:
            name (str): name of the technician.
            weekly_rate (float): weekly pay rate (default is 500).
            speciality (str): fish type specialization (default is None).
        """
        while True:
            # Check the input to handle error
            if not name:
                name = input("Enter technician name to add: ").strip()

            if not name:
                print("No input provided. Please enter a name.")
                name = None
                continue

            if name in [tech.name for tech in self.technicians]:
                print(
                    f"Technician with the name '{name}' already exists." 
                    f"Please enter a unique name."
                )
                
                name = None
                continue
            
            # Check the ispeciality
            if speciality is None:
                speciality = (
                    input(f"Does {name} have a speciality? If yes," 
                          f"enter the fish type, or press Enter for none: ").strip().lower()
                    )

            if speciality == 'none' or speciality == '':
                speciality = None
            elif speciality not in self.fish_data.fish_data:
                print(
                    f"Invalid speciality '{speciality}'. "
                    f"Please enter a valid fish type."
                )
                speciality = None
                continue

            technician = Technicians(name, weekly_rate, speciality)
            self.technicians.append(technician)
            print(
                f"Hired technician: {technician.name}, Weekly rate: "
                f"{technician.weekly_rate}, Speciality: {technician.speciality or 'None'}"
            )
            break

    def remove_technician(self, name):
        """
        Removes a technician by name, which the name of the technician 
        to remove. 
        
        This will check whether the technician exists in 
        'self.techniciansor not. If the technician already exists in 
        'self.technicians', it will remove from 'self.technicians' 
        and then print the name that has just been removed.

        Args:
            name (str): the name of the technician to remove.
        """
        removed = False
        for technician in self.technicians:
            if technician.name == name:
                self.technicians.remove(technician)
                removed = True
                print(f"Removed technician: {technician.name}")
                break
            else:
                print(f"No removing technicians : {technician.name}")

    def calculation_total_payment(self):
        """
        Calculates total payments for all technicians and then deduct
        cash balance and finally print it to show for users.
        """
        total_payment = 0
        print("\n=== Technician Payment Summary ===")
        for technician in self.technicians:
            # Calculate payment for 12 weeks (1 quarter)
            payment = technician.weekly_rate * 12  
            total_payment += payment
            print(f"Paid {technician.name}, weekly rate = 500, amount: £{payment}")
        self.cash_balance -= total_payment  # Deduct total payments
        self.update_cash_balance()  # Update balance
        print(f"\nTotal technician payment: £{total_payment}")
        print(f"Remaining cash balance: £{self.cash_balance}")
    
    def sell_fish(self):
        """
        Let users to sell fish while considering three conditions.

        The three conditions include technician availability, 
        warehouse resource, and fish demand. The condition will have 
        an interaction with Warehouse resources for fertilizer, feed, 
        and salt and Fish demand and pricing from 'fish_data'. After updating
        cash balance warehouse supplies, and fish demand after each sale,
        it will print to show users the summary and remaining resources
        """
        print("\n=== The Number of Fish Available for Sale ===")
        for fish_name, fish_details in self.fish_data.fish_data.items():
            print(
                f"{fish_name}: {fish_details['demand']} units available" 
                f"for sale at £{fish_details['price']}"
            )
        
        # Calculate total day base on the number of technician
        remaining_days = len(self.technicians) * 45  
        print(
            f"\nTechnicians available: {len(self.technicians)}, " 
            f"Total working days: {remaining_days}"
        )

        # Keep all of resources in one variable
        available_resources = {
            'fertilizer': sum(warehouse.supplies['fertilizer'] for warehouse 
                              in self.warehouses.values()),
            'feed': sum(warehouse.supplies['feed'] for warehouse 
                        in self.warehouses.values()),
            'salt': sum(warehouse.supplies['salt'] for warehouse 
                        in self.warehouses.values()),
        }

        while True:
            fish_name = (
                input("\nEnter fish name to sell (type 'done' to finish): ").strip()
            )
            # Let users prompt the name of fish to sell and check error
            if fish_name.lower() == 'done':
                break

            if fish_name not in self.fish_data.fish_data:
                print("Invalid fish name. Please choose from the available types.")
                continue
            
            try:
                max_demand = self.fish_data.fish_data[fish_name]['demand']
                # The quantity of fish to sell have no more the maximum demand and
                quantity = (
                    int(input(
                        f"Enter quantity of {fish_name} " 
                        f"to sell (max {max_demand}): "))
                )
                
                # The quantity of fish to sell have no less than or equal 0
                if quantity <= 0:
                    print("Please enter a positive number.")
                    continue
                # The quantity of fish to sell have no more the maximum demand
                if quantity > max_demand:
                    print(
                        f"\nInsufficient stock for {fish_name}. " 
                        f"Available: {max_demand} units."
                    )
                    continue

                # Calculate maintenance time for each fish type and the quantity 
                calculation_of_maintenance_time = (
                self.fish_data.fish_data[fish_name]['maintenance_time']
                )
                effectiveness_of_maintenance_time = calculation_of_maintenance_time

                # Check whether technician have speciality or not
                specialists = (
                [tech for tech in self.technicians if tech.speciality == fish_name]
                )
                if specialists:
                    effectiveness_of_maintenance_time *= 2 / 3
                    print(
                        f"Specialist(s) available for {fish_name}, reducing maintenance time "
                        f"to {effectiveness_of_maintenance_time:.2f} days per unit."
                    )

                maintenance_time_required = effectiveness_of_maintenance_time * quantity

                # Check whether the technician time is enough or not
                if maintenance_time_required > remaining_days:
                    print(f"\nInsufficient technician to sell {quantity} units of {fish_name}.")
                    print(
                        f"Requirement: {maintenance_time_required:.2f} days, "
                        f"Available: {remaining_days:.2f} days"
                    )
                    continue

                # Calculate the quantity of resources
                requirement_of_fertilizer = (
                self.fish_data.fish_data[fish_name]['fertilizer'] * quantity / 1000
                )
                requirement_of_feed = (
                self.fish_data.fish_data[fish_name]['feed'] * quantity
                )
                requirement_of_salt = (
                self.fish_data.fish_data[fish_name]['salt'] * quantity
                )

                # Check the resources in the storage
                insufficient_resources = []
                if requirement_of_fertilizer > available_resources['fertilizer']:
                    insufficient_resources.append(
                        f"Fertilizer: Need {requirement_of_fertilizer:.2f} "
                        f"L, available {available_resources['fertilizer']:.2f} L"
                    )
                if requirement_of_feed > available_resources['feed']:
                    insufficient_resources.append(
                        f"Feed: Need {requirement_of_feed:.2f} kg, "
                        f"available {available_resources['feed']:.2f} kg"
                    )
                if requirement_of_salt > available_resources['salt']:
                    insufficient_resources.append(
                        f"Salt: Need {requirement_of_salt:.2f} kg, "
                        f"available {available_resources['salt']:.2f} kg"
                    )

                if insufficient_resources:
                    print("\nInsufficient resources to sell this quantity. ")
                    for resource in insufficient_resources:
                        print(f" - {resource}")
                    continue

                # Reduce time and resources
                remaining_days -= maintenance_time_required
                for warehouse_name, warehouse_data in self.warehouses.items():
                    used_fertilizer = min(requirement_of_fertilizer, 
                                          warehouse_data.supplies['fertilizer'])
                    warehouse_data.supplies['fertilizer'] -= used_fertilizer
                    requirement_of_fertilizer -= used_fertilizer

                    used_feed = min(requirement_of_feed, warehouse_data.supplies['feed'])
                    warehouse_data.supplies['feed'] -= used_feed
                    requirement_of_feed -= used_feed

                    used_salt = min(requirement_of_salt, warehouse_data.supplies['salt'])
                    warehouse_data.supplies['salt'] -= used_salt
                    requirement_of_salt -= used_salt

                # Updating information to inform users
                self.sales[fish_name] = self.sales.get(fish_name, 0) + quantity
                self.cash_balance += quantity * self.fish_data.fish_data[fish_name]['price']
                self.update_cash_balance()
                self.fish_data.fish_data[fish_name]['demand'] -= quantity

                print(
                    f"Sold {quantity} units of {fish_name} for"
                    f"£{quantity * self.fish_data.fish_data[fish_name]['price']}."
                )
                print(
                    f"Remaining technician time: {remaining_days / 5:.2f} "
                    f"weeks ({remaining_days:.2f} days)"
                )
                print(f"Remaining resources in warehouse:")
                print(f" - Fertilizer: {available_resources['fertilizer']:.2f} L")
                print(f" - Feed: {available_resources['feed']:.2f} kg")
                print(f" - Salt: {available_resources['salt']:.2f} kg")

            except ValueError:
                print("Invalid input. Please enter a valid number.")

        print("\n=== Sales Summary ===")
        # Inform users about the sale summary
        for fish, quantity_sold in self.sales.items():
            print(f"{fish}: {quantity_sold} units sold")
        print(f"Updated cash balance: £{self.cash_balance:.2f}")
    
    def calculate_storage_cost(self):
        """
        Calculate and deduct total warehouse cost for main 
        and auxiliary warehouses.
        
        The calculation depends on resource levels in both main 
        and auxiliary warehouses and storage cost rates for each 
        resource. After that deduct total storage cost from cash_balance. 
        """
        total_storage_cost = 0
        print("\n=== Warehouse Cost ===")
        
        # Calculate Cash balance by minus fixed rent (1500)
        self.cash_balance -= self.warehouse_cost
        print(f"Paid fixed warehouse rent: £{self.warehouse_cost:.2f}")


        for resource in ['fertilizer', 'feed', 'salt']:
            remaining_main = self.warehouses['main'].supplies[resource]
            remaining_auxiliary = self.warehouses['auxiliary'].supplies[resource]
            
            # Calculate main warehouse rent  
            main_cost = (
                remaining_main 
                * self.warehouses['main'].storage_cost_rate[resource]
            )
            total_storage_cost += main_cost
            print(
                f"Main - {resource.capitalize()}: £{main_cost:.2f} "
                f"(Remaining: {remaining_main} units)"
            )
            # Calculate auxiliary warehouse rent 
            auxiliary_cost = (
                remaining_auxiliary 
                * self.warehouses['auxiliary'].storage_cost_rate[resource]
            )
            total_storage_cost += auxiliary_cost
            print(
                f"Auxiliary - {resource.capitalize()}: £{auxiliary_cost:.2f}" 
                f"(Remaining: {remaining_auxiliary} units)"
            )

        # Calculate cash balance by minus warehouse rent
        self.cash_balance -= total_storage_cost
        print(f"Total storage cost: £{total_storage_cost:.2f}")
        print(f"Remaining cash balance after storage costs: £{self.cash_balance:.2f}")