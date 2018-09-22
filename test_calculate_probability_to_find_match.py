from itertools import product
from unittest import TestCase
from vector_search_proba import calculate_probability_to_find_match


class TestCalculateProbabilityMatch(TestCase):

    def assertCorrectResult(self, actual, expected, item_count, vectors_per_item, nn_pct):
        self.assertAlmostEqual(actual, expected,
                               msg="Wrong result for \n" +
                                   "item_count: " + str(item_count) + "\n" +
                                   "vectors_per_item: " + str(vectors_per_item) + "\n" +
                                   "nn_pct: " + str(nn_pct))

    def test_calc_prob_one_vector_per_item(self):
        nn_pcts = [0.01, 0.02, 0.05, 0.1, 0.2, 0.3, 0.5]
        item_count = [100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]
        vectors_per_item = 1
        for nn_pct, item_count in product(nn_pcts, item_count):
            result = calculate_probability_to_find_match(item_count, vectors_per_item, nn_pct)
            self.assertCorrectResult(result, nn_pct, item_count, vectors_per_item, nn_pct)
