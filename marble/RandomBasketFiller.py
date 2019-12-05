import random

from marble.Basket import Basket
from marble.MarblePumper import MarblePumper


class RandomBasketFiller:
    """
    Random Basket Filler - tries to fil_basketl the Basket pulling randomly the pumpers
    """

    def __init__(self, basket_size, pumper_number):
        """
        Initializes the Basket and the number of pumpers

        Parameters:
        basket_size (int): Size of the Basket
        pumper_number (int): Number of pumperss
        """
        self._basket = Basket(basket_size)
        self._pumper_number = pumper_number

    @property
    def basket(self):
        return self._basket

    def fill(self):
        """
        Tries to fill the Basket selecting the Pumper randomly

        Returns:
        int: Number of steps needed to fill the Basket
        """
        while not self._basket.is_full():
            choice = random.randrange(self._pumper_number)
            self._basket.add(MarblePumper.pull(choice))

        return self._basket.steps
