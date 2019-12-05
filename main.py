import numpy as np

from marble.basket_filler_evaluator import BasketFillerEvaluator
from marble.proto_rl_basket_filler import ProtoRLBasketFiller
from marble.random_basket_filler import RandomBasketFiller

BASKET_SIZE = 50000
PUMPER_NUMBER = 100
ATTEMPTS = 500


def summary(label, values):
    """
    Plot function to show the result of the Evaluation
    """
    max_value = np.amax(values)
    min_value = np.amin(values)
    avg = np.average(values)
    print(f"Eval {label}:\nSteps min: {min_value}\nSteps max: {max_value}\nSteps Avg: {avg}\n\n")


print(f"Basket Size: {BASKET_SIZE} - Num. of Pumpers: {PUMPER_NUMBER}")
print(f"Minimum {BASKET_SIZE / (PUMPER_NUMBER * 10)}\n\n")

# 1ST TEST - RANDOM BASKET FILLER
evaluator = BasketFillerEvaluator(RandomBasketFiller(BASKET_SIZE, PUMPER_NUMBER))
summary("Random Filler", evaluator.eval(ATTEMPTS))

# 2ND TEST - PROTO-RL BASKET FILLER with high Exploitation
evaluator = BasketFillerEvaluator(ProtoRLBasketFiller(BASKET_SIZE, PUMPER_NUMBER, exploitation_percentage=80))
summary("protoRL High Exploitation", evaluator.eval(ATTEMPTS))

# 3RD TEST - PROTO-RL BASKET FILLER with high Exploration
evaluator = BasketFillerEvaluator(ProtoRLBasketFiller(BASKET_SIZE, PUMPER_NUMBER, exploitation_percentage=20))
summary("protoRL High Exploration", evaluator.eval(ATTEMPTS))

# 4rd TEST - PROTO-RL BASKET FILLER with balanced Exploitation/Exploration
evaluator = BasketFillerEvaluator(ProtoRLBasketFiller(BASKET_SIZE, PUMPER_NUMBER, exploitation_percentage=50))
summary("protoRL balanced Exploitation/Exploration", evaluator.eval(ATTEMPTS))
