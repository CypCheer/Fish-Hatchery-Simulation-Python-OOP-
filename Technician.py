"""
Filename: technician.py
Author: Chayaporn Makchuay
Date: 16 November 2024
Description:
    This module defines the Technicians class, which shows the staffs
    of the fish hatchery, including their names, pay rates, and specializations.
"""

class Technicians:
    """
    This class is made to represents a technician in the hatchery.

    Purpose:
    This class is made to create objects to represent technicians.
    Each technician has attributes, including name, weekly rate, and 
    a specialty (if any).

    Attributes:
        - name (str): the name of the technician.
        - weekly_rate (int): the weekly pay rate for the technicians.
        - speciality (str or None): the speciality that each technician 
          have with each type of fishes or None if no specialization.
    """

    def __init__(self, name, weekly_rate=500, speciality=None):
        """
        Beginning a Technician object with properties.

        Args:
            name (str): the name of the technician.
            weekly_rate (int, optional): weekly pay rate for the technician. 
                                         defaults to 500.
            speciality (str or None, optional): specific fish type the technician
                specializes in, or None for no specialization.
        """
        self.name = name
        self.weekly_rate = weekly_rate
        self.speciality = speciality