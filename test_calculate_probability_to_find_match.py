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

    def test_calc_prob_one_nn(self):
        item_count = [1000, 2000, 5000, 10000, 20000, 50000, 100000, 500000, 1000000]
        vectors_per_item = [1, 5, 10, 100]
        for vectors_per_item, item_count in product(vectors_per_item, item_count):
            nn_pct = 1 / item_count
            result = calculate_probability_to_find_match(item_count, vectors_per_item, nn_pct)
            self.assertCorrectResult(result, nn_pct, item_count, vectors_per_item, nn_pct)

    def test_calc_prob_two_vectors_per_item(self):
        nn_pct = 0.4
        item_count = 5

        result_1_item = calculate_probability_to_find_match(item_count, 1, nn_pct)
        self.assertCorrectResult(result_1_item, nn_pct, item_count, 1, nn_pct)

        result_2_items = calculate_probability_to_find_match(item_count, 2, nn_pct)
        self.assertCorrectResult(result_2_items, 0.3777777777777, item_count, 2, nn_pct)

    def test_calc_prob_ten_vectors_per_item(self):
        nn_pct = 0.5
        item_count = 10

        result_1_item = calculate_probability_to_find_match(item_count, 1, nn_pct)
        self.assertCorrectResult(result_1_item, nn_pct, item_count, 1, nn_pct)

        result_10_items = calculate_probability_to_find_match(item_count, 10, nn_pct)
        self.assertCorrectResult(result_10_items, 0.4162476331, item_count, 2, nn_pct)