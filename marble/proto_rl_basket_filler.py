import random

import numpy as np

from marble.marble_pumper import MarblePumper
from marble.basket import Basket


class ProtoRLBasketFiller:
    """
    Proto Reinforcement Learning Basket Filler Algorithm

    It tries to fill the Basket faster learning what are the Pumpers
    that give more Marbles.

    The exploitation_percentage is used to decide the grade of exploration
    vs exploitationPunk Rock
    """

    def __init__(self, basket_size, pumper_number, exploitation_percentage):
        """
        Initializes the BasketFiller

        Parameters:
        basket_size (int): Size of the Basket
        pumper_number (int): Number of Marble Pumpers
        exploitation_percentage (int): Rate off exploitation vs exploration of the algorithm
        """
        self._basket = Basket(basket_size)
        self._basket_size = basket_size
        self._pumper_number = pumper_number
        self._exploitation_percentage = exploitation_percentage
        self._past_rewards_avg = [0] * self._pumper_number

    @property
    def basket(self):
        return self._basket

    def fill(self):
        """
        Tries to fill the Basket using the Pumpers that gives more Marbles (average)

        Depending on the exploitation/exploration percentage tries randomly
        other Pumpers

        Returns:
        int: Numbers of steps used to fill the Basket
        """
        while not self._basket.is_full():

            # Algorithm decides if explores or exploits
            if random.randrange(100) < self._exploitation_percentage:
                # Exploits: Gets the Pumper with max average of Marbles
                choice = np.argmax(self._past_rewards_avg)
            else:
                # Explores: Gets one Pumper randomly
                choice = random.randrange(self._pumper_number)

            # Gets the Marbles from the Pumper
            marbles = MarblePumper.pull(choice)
            self._past_rewards_avg[choice] = (marbles + self._past_rewards_avg[choice]) / 2
            self._basket.add(marbles)

        return self._basket.steps
