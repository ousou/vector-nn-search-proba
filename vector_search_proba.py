from functools import reduce
import operator


def product(iterable):
    return reduce(operator.mul, iterable, 1)


def calculate_probability_to_find_match(item_count, vectors_per_item, nn_pct):
    vectors = item_count * vectors_per_item
    nn_count = round(item_count * nn_pct)

    prob_no_match = product(range(vectors - nn_count, vectors)) \
                    / product(range(vectors - nn_count + 1, vectors + 1))

    return 1 - prob_no_match

