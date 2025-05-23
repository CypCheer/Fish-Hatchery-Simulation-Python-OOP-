"""
Filename: warehouse.py
Author: Chayaporn Makchuay
Date: 16 November 2024
Description:
    This module defines the Warehouse class, which is in charge of managing
    resource storage, including capacity, depreciation, and refilling.
"""

import math

"""
This module is imported to perform mathematical operations, 
It is important for precise calculations to handle 
resource management.
"""


class Warehouse:
    """
    This class is made for representing a warehouse, that is used to
    store resources .

    Purpose:
    - To manage resource storage like capacity, depreciation rates, 
      and storage costs.
    - To handle resource calculations such as depreciation and refilling.

    Attributes:
    - supplies (dict): the current amount of each resource in the warehouse.
    - capacity (dict): the maximum storage capacity for each resource type.
    - depreciation_rate (dict): the rate of depreciation for each resource.
    - storage_cost_rate (dict): the storage cost per unit for each resource.
    """

    def __init__(self, capacity, depreciation_rate, storage_cost_rate):
        """
        Beginning a warehouse instance with storage information.

        Args:
            capacity (dict): the maximum storage for each resource.
            depreciation_rate (dict): the depreciation rate for each resource.
            storage_cost_rate (dict): the cost per unit of resource stored.

        Attributes:
            supplies (dict): to tracks the current quantity of each resource.'
        """
        self.supplies = {resource: capacity[resource] for resource in capacity}
        self.capacity = capacity
        self.depreciation_rate = depreciation_rate
        self.storage_cost_rate = storage_cost_rate

    def depreciate_resources(self):
        """
        Reduces resources based on depreciation rate. 
        Ensures that values do not drop below zero.

        How it works:
        - Iterates through each resource in the warehouse.
        - Calculates the depreciated quantity by multiplying the current 
          resource amount by its depreciation rate.
        - Updates the remaining resource quantity, ensuring it does not 
          go below zero.
        """
        for resource, rate in self.depreciation_rate.items():
            depreciated_quantity = math.ceil(self.supplies[resource] * rate)
            self.supplies[resource] = max(0, self.supplies[resource] - depreciated_quantity)

    def refill_resources(self, resource, amount):
        """
        Refills resources back to the storage to meet their maximum capacity.
        Args:
            resource (str): the name of the resource to refill.
            amount (int): the amount of resource to add.

        Returns:
            int: The leftover amount that could not be stored due to capacity limits.
        """
        available_capacity = self.capacity[resource] - self.supplies[resource]
        to_fill = min(amount, available_capacity)
        self.supplies[resource] += to_fill 
        return amount - to_fill 