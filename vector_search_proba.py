from functools import reduce
import operator


def prod(iterable):
    return reduce(operator.mul, iterable, 1)


def calculate_probability_to_find_match(item_count, vectors_per_item, nn_pct):
    """
    Calculates the probability of finding a match for a given item in a
    nearest neighbor search when vectors for items are placed randomly in a space.

    :param item_count: The number of items for which vectors are generated
    :param vectors_per_item: The number of vectors per item
    :param nn_pct: The percentage of items to search in by nearest neighbor algorithm.
                   For instance if nn_pct is 0.01 and item_count is 1000 then the
                   0.1 * 1000 = 10 nearest neighbors are searched. The probability
                   returned is the probability of finding the given item in the
                   10 nearest neighbors.

    :return: The probability of finding the vector for a given item in the NN search.
    """
    vectors = item_count * vectors_per_item
    nn_count = round(item_count * nn_pct)

    numerator_range = range(vectors - nn_count - vectors_per_item + 1,
                            vectors - vectors_per_item + 1)
    denominator_range = range(vectors - nn_count + 1, vectors + 1)

    prob_no_match = 1
    for num_item, dem_item in zip(numerator_range, denominator_range):
        prob_no_match *= num_item / dem_item

    return 1 - prob_no_match

