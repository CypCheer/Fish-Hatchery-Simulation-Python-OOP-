"""
Filename: vendor.py
Author: Chayaporn Makchuay
Date: 16 November 2024
Description:
    This module defines the Vendor class, which represents vendors that sell
    resources to the fish hatchery wth different prices.
"""

class Vendor:
    """
    Shows a vendor that supplies resources.

    Attributes:
        name (str): The name of the vendor.
        prices (dict): A dictionary of resource prices offered by the vendor.
    """

    def __init__(self, name, prices):
        """
        Constructor for the `Vendor` class. Beginning with vendor details.

        Parameters:
            - name: The name of the vendor.
            - prices: Prices for each resource offered by the vendor
        """
        self.name = name  
        self.prices = prices 

    def calculate_cost(self, resource, quantity):
        """
        Calculates the cost of buying resources.
        
        Parameters:
            - resource: The name of the resource to purchase
            - quantity: The amount of the resource to purchase.
        """
        #Return the total cost of buying the resource.
        return self.prices[resource] * quantity