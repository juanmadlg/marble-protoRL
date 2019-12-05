import random


class MarblePumper:
    """
    Pumpers used by the BasketFillers to fill the Basket
    """

    @staticmethod
    def pull(index):
        """
        Returns the number of Marbles for the Pumper 'index'.

        This code is the secret algorithm that the BasketFillers don't know.
        """
        return random.randrange((index*5), (index*10)+1)
