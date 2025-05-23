"""
Filename: main.py
Author: Chayaporn Makchuay
Date: 16 November 2024
Description:
    This script is the entry point for the fish hatchery simulation.
    It begins the hatchery, handles user inputs, and manages the simulation
    with a number of quarters.
"""

from Fish import Fish
from Technician import Technicians
from Warehouse import Warehouse
from Vendors import Vendor
from Hatchery import Hatchery

def main():

    """
    This is the main function that is the entry point for 
    the fish hatchery simulation program. 
    
    This funtion allows users to simulate the operation of 
    the hatchery and also shows the important information 
    for users to manage smoothly, including prompt the user to input 
    the number of quarters to simulate, allow users to manage technicians, 
    and buy supplies from vendors. The simulation will end when the number 
    of quarters equal to the number that they filled or they face with bankruptcy.

    """
    # Beginning fish data from the 'Fish' class
    fish_data = Fish()

    # Create a hatchery with a 10000 cash balance
    hatchery = Hatchery(cash_balance=10000, fish_data=fish_data)

    # Prompt the user to enter the number of quarters to run the simulation.
    while True:
        try:
            # Check input for handle earror from users' input
            number_of_quarters_input = input(
                "Please enter number of quarters: "
            ).strip()
            if not number_of_quarters_input:
                print("No input provided. Please enter a valid number of quarters.")
                continue
            number_of_quarters = int(number_of_quarters_input)
            if number_of_quarters <= 0:
                print("Invalid input. Please enter a positive number for the quarters.")
                continue
            break  # If input is valid, exit the loop
        except ValueError:
            print("Invalid input. Please enter a valid integer for the number of quarters.")
    
    # Simulate each quarter
    for quarter in range(1, number_of_quarters + 1):
        print(f"\n====== SIMULATING quarter {quarter} ======")

        # Reset sales for the new quarter
        hatchery.sales = {}

        # Reset fish demand
        fish_data.reset_fish_demand()

        # Prompt the users to add/remove technicians at beginning of the quarter.
        while True:
            try:
                # Check input for handle earror from users' input
                print(f"Current number of technicians: {len(hatchery.technicians)}")
                technician_input = input(
                    "Enter number of technicians to add (+) or remove (-), "
                    "or 0 for no change: "
                ).strip()
                if not technician_input:
                    print("No input provided. Please enter a valid number.")
                    continue
                number_of_technicians = int(technician_input)

                # Ensure that the number of technicians remains between 1 and 5
                if len(hatchery.technicians) + number_of_technicians < 1:
                    print("Cannot have less than 1 technician. Please fill new input.")
                    continue
                if len(hatchery.technicians) + number_of_technicians > 5:
                    print("Cannot have more than 5 technicians. Please fill new input.")
                    continue
                break  # If input is valid, it will exit the loop
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        # Add technician name and chack the speciality of the technicians
        if number_of_technicians > 0:
            for i in range(number_of_technicians):
                while True:
                    # Check input for handle error from users' input 
                    name = input("Enter technician name to add: ").strip()
                    if not name:
                        print("No input provided. Please enter a name.")
                        continue
                    if name in [tech.name for tech in hatchery.technicians]:
                        print(
                            f"Technician with the name '{name}' already exists. "
                            "Please enter a unique name."
                        )
                        continue
                    speciality = input(
                        f"Does {name} have a speciality? If yes, enter the fish type, "
                        "or press Enter for none: "
                    ).strip()
                    hatchery.add_technician(
                        name, speciality=speciality if speciality else None
                    )
                    break

        # Remove technicians
        elif number_of_technicians < 0:
            for i in range(abs(number_of_technicians)):
                while True:
                    # Check input for handle error from users' input
                    name = input("Enter technician name to remove: ").strip()
                    if not name:
                        print("No input provided. Please enter a name.")
                        continue
                    if name not in [tech.name for tech in hatchery.technicians]:
                        print(
                            f"No technician found with the name '{name}'. "
                            "Please enter a valid name."
                        )
                        continue
                    hatchery.remove_technician(name)
                    break

        # if user don't want to change
        else:
            print("No change")

        # Sell fish for this quarter
        hatchery.sell_fish()

        # Deduct warehouse storage costs
        hatchery.calculate_storage_cost()
        if hatchery.cash_balance < 0:
            print("Went Bankrupt! Simulation terminated.")
            break

        # Apply depreciation to warehouse resources
        hatchery.depreciation()

        # Calculate total payment and check whether it go bankrupt or not
        hatchery.calculation_total_payment()
        if hatchery.cash_balance < 0:
            print("Went Bankrupt! Simulation terminated.")
            break

        # let users choose vendors to refill supplies
        vendor_choice = input(
            "Choose a vendor: 1. Slippery Lakes, 2. Scaly Wholesaler: "
        ).strip()
        vendor_name = (
            'Slippery Lakes' if vendor_choice == '1' else 'Scaly Wholesaler'
        )
        vendor = hatchery.vendors[vendor_name]

        # Refill supplies 
        for resource in ['fertilizer', 'feed', 'salt']:
            # Calculate total capacity and the quantity 
            total_capacity = sum(
                warehouse.capacity[resource] for warehouse in hatchery.warehouses.values()
            )
            current_quantity = sum(
                warehouse.supplies[resource] for warehouse in hatchery.warehouses.values()
            )
            amount_needed = max(0, total_capacity - current_quantity)

            if amount_needed > 0:  # Buy only if the resource is needed
                # Calculate cost of purchase
                cost = vendor.calculate_cost(resource, amount_needed)  
                # Check if the cash balance is sufficient
                if hatchery.cash_balance >= cost:  
                    hatchery.cash_balance -= cost  # Deduct the cost
                    remaining_amount_needed = amount_needed

                    # Refill resources in warehouses
                    for warehouse in hatchery.warehouses.values():
                        remaining_amount_needed = warehouse.refill_resources(
                            resource, remaining_amount_needed
                        )
                        if remaining_amount_needed == 0:  
                            break

                    # Shows the quantity purchased and cost
                    print(
                        f"Purchased {amount_needed - remaining_amount_needed} units of "
                        f"{resource} from {vendor_name} for £{cost:.2f}"
                    )
                else:
                    # Show if user face with insufficient cash 
                    print(
                        f"Not enough cash to purchase {resource}. "
                        f"Needed: £{cost:.2f}, Available: £{hatchery.cash_balance:.2f}"
                    )

        # Summarise at the end of the quarter
        print(f"\n--- End of Quarter {quarter} ---")
        print(f"Cash balance after Quarter {quarter}: £{hatchery.cash_balance:.2f}")
        print(f"----------------------------------\n")
        
        # Check for bankruptcy
        if hatchery.cash_balance < 0:
            print("Went Bankrupt! No funds remaining.")
            break

if __name__ == "__main__":
    main()
