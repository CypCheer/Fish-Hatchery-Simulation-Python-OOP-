"""
Filename: fish.py
Author: Chayaporn Makchuay
Date: 16 November 2024
Description:
    This module defines the Fish class, which fish details about different
    fish species, including their resource requirements, demand, and pricing.
"""

class Fish:
    """
    Beginning the Fish class with various type of fishes.

    Purpose:
    This class have various fish species and stores details about their
    maintenance requirements, demand, and price.

    Attributes:
    - fish_data (dict): A dictionary that contain details of fish types:
        - fertilizer (int): amount of fertilizer per unit.
        - feed (int): amount of feed per unit.
        - salt (int): amount of salt per unit.
        - maintenance_time (float): time (in days) for maintenance per unit.
        - demand (int): current demand for fish type.
        - price (int): price per unit of fish.
    """


    def __init__(self):
        """
        Beginning fish data with attributes for different fish types

        Attributes include fertilizer, feed, salt, maintenance time, 
        demand, and price.
        """

        self.fish_data = {
            'Clef Fins': {
                'fertilizer': 100,
                'feed': 12,
                'salt': 2,
                'maintenance_time': 2.0,
                'demand': 25,
                'price': 250,
            },
            'Timpani': {
                'fertilizer': 50,
                'feed': 9,
                'salt': 2,
                'maintenance_time': 1.0,
                'demand': 10,
                'price': 350,
            },
            'Andalusian Brim': {
                'fertilizer': 90,
                'feed': 6,
                'salt': 2,
                'maintenance_time': 0.5,
                'demand': 15,
                'price': 250,
            },
            'Plagal Cod': {
                'fertilizer': 100,
                'feed': 10,
                'salt': 2,
                'maintenance_time': 2.0,
                'demand': 20,
                'price': 400,
            },
            'Fugue Flounder': {
                'fertilizer': 200,
                'feed': 12,
                'salt': 2,
                'maintenance_time': 2.5,
                'demand': 30,
                'price': 550,
            },
            'Modal Bass': {
                'fertilizer': 300,
                'feed': 12,
                'salt': 6,
                'maintenance_time': 3.0,
                'demand': 50,
                'price': 500,
            }
        }

    def reset_fish_demand(self):
        """
        Reset the 'demand' attribute for each fish type to its defult value.

        The default values are stored in dictionary 
        'default_demand' This function is useful for the start of each 
        quarter to reset the demands.
        """
        default_demand = {
            'Clef Fins': 25,
            'Timpani': 10,
            'Andalusian Brim': 15,
            'Plagal Cod': 20,
            'Fugue Flounder': 30,
            'Modal Bass': 50,
        }

        for fish_name, fish_details in self.fish_data.items():
            # Update the 'demand' value with the default value
            fish_details['demand'] = default_demand[fish_name]