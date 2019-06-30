# import libraries
import unittest

# import implementations
from implementations import mathematical_imp as mi
from implementations import sciPy_imp as sp
from implementations import pure_numPy_imp as np

# import services
from services import fileReader


class TestResultChecks(unittest.TestCase):

    def setUp(self):
        self.SAMPLE_2 = "../samples/sample_input_2_8.tsv"
        self.SAMPLE_3 = "../samples/sample_input_3_1000.tsv"
        self.SAMPLE_4 = "../samples/sample_input_4_4.tsv"
        self.SAMPLE_10 = "../samples/sample_input_10_100.tsv"
        self.SAMPLE_100 = "../samples/sample_input_100_100.tsv"

    def test_sample2_results_math(self):
        data_file = fileReader.get_table_from_file(self.SAMPLE_2)

        expected_result = (3, 6)
        result = mi.get_the_index_of_the_closest_nodes(data_file)
        self.assertEqual(result, expected_result)

    def test_sample3_results_math(self):
        data_file = fileReader.get_table_from_file(self.SAMPLE_3)

        expected_result = (223, 388)
        result = mi.get_the_index_of_the_closest_nodes(data_file)
        self.assertEqual(result, expected_result)

    def test_sample4_results_math(self):
        data_file = fileReader.get_table_from_file(self.SAMPLE_4)

        expected_result = (2, 3)
        result = mi.get_the_index_of_the_closest_nodes(data_file)
        self.assertEqual(result, expected_result)

    def test_sample10_results_math(self):
        data_file = fileReader.get_table_from_file(self.SAMPLE_10)

        expected_result = (40, 94)
        result = mi.get_the_index_of_the_closest_nodes(data_file)
        self.assertEqual(result, expected_result)

    def test_sample100_results_math(self):
        data_file = fileReader.get_table_from_file(self.SAMPLE_100)

        expected_result = (48, 96)
        result = mi.get_the_index_of_the_closest_nodes(data_file)
        self.assertEqual(result, expected_result)

    def test_sample2_results_sciPy(self):
        data_file = fileReader.get_table_from_file(self.SAMPLE_2)

        expected_result = (3, 6)
        result = sp.get_the_index_of_the_closest_nodes(data_file)
        self.assertEqual(result, expected_result)

    def test_sample3_results_sciPy(self):
        data_file = fileReader.get_table_from_file(self.SAMPLE_3)

        expected_result = (223, 388)
        result = sp.get_the_index_of_the_closest_nodes(data_file)
        self.assertEqual(result, expected_result)

    def test_sample4_results_sciPy(self):
        data_file = fileReader.get_table_from_file(self.SAMPLE_4)

        expected_result = (2, 3)
        result = sp.get_the_index_of_the_closest_nodes(data_file)
        self.assertEqual(result, expected_result)

    def test_sample10_results_sciPy(self):
        data_file = fileReader.get_table_from_file(self.SAMPLE_10)

        expected_result = (40, 94)
        result = sp.get_the_index_of_the_closest_nodes(data_file)
        self.assertEqual(result, expected_result)

    def test_sample100_results_sciPy(self):
        data_file = fileReader.get_table_from_file(self.SAMPLE_100)

        expected_result = (48, 96)
        result = sp.get_the_index_of_the_closest_nodes(data_file)
        self.assertEqual(result, expected_result)

    def test_sample2_results_pureNumPy(self):
        data_file = fileReader.get_table_from_file(self.SAMPLE_2)

        expected_result = (3, 6)
        result = np.get_the_index_of_the_closest_nodes(data_file)
        self.assertEqual(result, expected_result)

    def test_sample3_results_pureNumPy(self):
        data_file = fileReader.get_table_from_file(self.SAMPLE_3)

        expected_result = (223, 388)
        result = np.get_the_index_of_the_closest_nodes(data_file)
        self.assertEqual(result, expected_result)

    def test_sample4_results_pureNumPy(self):
        data_file = fileReader.get_table_from_file(self.SAMPLE_4)

        expected_result = (2, 3)
        result = np.get_the_index_of_the_closest_nodes(data_file)
        self.assertEqual(result, expected_result)

    def test_sample10_results_pureNumPy(self):
        data_file = fileReader.get_table_from_file(self.SAMPLE_10)

        expected_result = (40, 94)
        result = np.get_the_index_of_the_closest_nodes(data_file)
        self.assertEqual(result, expected_result)

    def test_sample100_results_pureNumPy(self):
        data_file = fileReader.get_table_from_file(self.SAMPLE_100)

        expected_result = (48, 96)
        result = np.get_the_index_of_the_closest_nodes(data_file)
        self.assertEqual(result, expected_result)
