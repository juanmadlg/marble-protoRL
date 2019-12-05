class BasketFillerEvaluator:
    """
    Evaluator class used to see what are the different BasketFillers performance
    """
    def __init__(self, basket_filler):
        self._filler = basket_filler

    def eval(self, attempts):
        """
        Evaluates the algorithm for 'attempts'

        Returns:
        list[int]: List of steps required for each attempt
        """
        steps = []
        for _ in range(attempts):

            self._filler.basket.empty()
            steps.append(self._filler.fill())

        return steps
