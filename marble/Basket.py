class Basket:
    """
    The Basket that has to be filled by the BasketFillers
    """

    def __init__(self, size):
        """
        The Basket is initially empty

        Parameters:un
        size (int): Number of marbles needed to fill the Basket
        """
        self._marbles = 0
        self._steps = 0
        self._size = size

    @property
    def num_marbles(self):
        return self._marbles

    @property
    def steps(self):
        return self._steps

    def add(self, num_marbles):
        """
        Adds some marbles to the Basket

        Parameters:
        num_marbles (int): Marbles that are added to the basket

        Returns:
        Basket: returns the Basket itself
        """
        self._marbles += num_marbles
        self._steps += 1
        return self

    def empty(self):
        """
        All marbles of the Basket are removed

        Returns:
        Basket: returns the Basket itself
        """
        self._marbles = 0
        self._steps = 0
        return self

    def is_full(self):
        """
        Returns if the Basket is full of Marbles

        Returns:
        boolean: returns if the basket is full
        """
        return self._marbles >= self._size
