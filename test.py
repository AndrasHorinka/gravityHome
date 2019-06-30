import unittest

from implementations import mathematical_imp as mi
from implementations import pure_numPy_imp as np
from implementations import sciPy_imp as sp
from services import fileReader


class TestFileReader(unittest.TestCase):

    def setUp(self):
        self.SAMPLE_2 = "samples/sample_input_2_8.tsv"
        self.SAMPLE_4 = "samples/sample_input_4_4.tsv"

    def test_fileReader_sample_2(self):
        data_file = fileReader.get_table_from_file(self.SAMPLE_2)
        expected_data_file = [
            [float(-262972), float(508697)],
            [float(-311943.65362731507), float(370239.3559213022)],
            [float(742431), float(-772652)],
            [float(-346046), float(696615.3537438104)],
            [float(194172), float(103527)],
            [float(726621.8167057682), float(-813087.8844925504)],
            [float(167923), float(-312455.0459619701)],
            [float(499664.42762545496), float(72395.09685360803)]
        ]

        self.assertEqual(
            data_file,
            expected_data_file,
            "FileReader Sample 2 is NOT OK!")

    def test_fileReader_sample_4(self):
        data_file = fileReader.get_table_from_file(self.SAMPLE_4)
        expected_data_file = [[float(653725),
                               float(-422117.9078937047),
                               float(-483855),
                               float(-579967)],
                              [float(-543446.8852285817),
                               float(-319599.12096280814),
                               float(130119),
                               float(42410.4020668423)],
                              [float(-800188),
                               float(58364),
                               float(586736),
                               float(-409415)],
                              [float(-607784.1676060366),
                               float(400299),
                               float(-925526.2019860733),
                               float(-779617)]]

        self.assertEqual(
            data_file,
            expected_data_file,
            "FileReader Sample 4 is NOT OK!")


class TestMathematicalImplementationGetSquareOfCoordinates(unittest.TestCase):

    def test_get_squares_of_coordinates_2d_0_0_0_0(self):
        node_a = [0, 0]
        node_b = [0, 0]
        result = 0
        for n in mi.get_squares_of_coordinates(node_a, node_b):
            result += n

        self.assertEqual(result, 0)

    def test_get_squares_of_coordinates_2d_1_1_1_1(self):
        node_a = [1, 1]
        node_b = [1, 1]
        result = 0
        for n in mi.get_squares_of_coordinates(node_a, node_b):
            result += n

        self.assertEqual(result, 0)

    def test_get_squares_of_coordinates_2d_m1_p1_p1_m1(self):
        node_a = [-1, 1]
        node_b = [1, -1]
        result = int()
        for n in mi.get_squares_of_coordinates(node_a, node_b):
            result += n

        self.assertEqual(result, 8)

    def test_get_squares_of_coordinates_2d_m10_m20_p10_m20(self):
        node_a = [-10, -20]
        node_b = [10, 20]
        result = int()
        for n in mi.get_squares_of_coordinates(node_a, node_b):
            result += n

        self.assertEqual(result, 2000)

    def test_get_squares_of_coordinates_2d_m10_m20_p0_m0(self):
        node_a = [-10, -20]
        node_b = [0, 0]
        result = int()
        for n in mi.get_squares_of_coordinates(node_a, node_b):
            result += n

        self.assertEqual(result, 500)

    def test_get_squares_of_coordinates_3d_m10_m20_p0_m0(self):
        node_a = [-10, -20]
        node_b = [0, 0]
        result = int()
        for n in mi.get_squares_of_coordinates(node_a, node_b):
            result += n

        self.assertEqual(result, 500)


class TestMathematicalImplementationGetDistanceSquare(unittest.TestCase):

    def test_get_distance_square_incorrectNodeAType(self):
        node_a = 2
        node_b = [0, 0]
        with self.assertRaises(TypeError):
            mi.get_distance_square(node_a, node_b)

    def test_get_distance_square_incorrectNodeBType(self):
        node_a = [2, 2]
        node_b = 2
        with self.assertRaises(TypeError):
            mi.get_distance_square(node_a, node_b)

    def test_get_distance_square_zeroLengthList(self):
        node_a = []
        node_b = [0, 0]
        with self.assertRaises(AssertionError):
            mi.get_distance_square(node_a, node_b)

    def test_get_distance_square_differentLengthLists(self):
        node_a = [1, 1]
        node_b = [2, 2, 2]
        with self.assertRaises(AssertionError):
            mi.get_distance_square(node_a, node_b)


class TestMathematicalImplementationGetTheClosestNodeFromOrigin(
        unittest.TestCase):

    def test_get_the_closest_node_from_origin_incorrectOriginType(self):
        node_a = 2
        nodes = [[0, 0], [1, 1]]
        with self.assertRaises(TypeError):
            mi.get_the_closest_node_from_origin(node_a, nodes)

    def test_get_the_closest_node_from_origin_incorrectNodesType(self):
        node_a = [1, 1]
        nodes = [2, 3]
        with self.assertRaises(TypeError):
            mi.get_the_closest_node_from_origin(node_a, nodes)

    def test_get_the_closest_node_from_origin_noOriginCoordinates(self):
        node_a = []
        nodes = [[0, 0], [1, 1]]
        with self.assertRaises(AssertionError):
            mi.get_the_closest_node_from_origin(node_a, nodes)


class TestMathematicalImplementationGetTheShortestDistanceForEachNodes(
        unittest.TestCase):

    def test_get_the_shortest_distance_for_each_node_nodesWithNoElements(self):
        nodes = []
        with self.assertRaises(AssertionError):
            mi.get_the_shortest_distance_for_each_node(nodes)

    def test_get_the_shortest_distance_for_each_node_nodesWithOneElementOnly(
            self):
        nodes = [1, 1]
        with self.assertRaises(AssertionError):
            mi.get_the_shortest_distance_for_each_node(nodes)

    def test_get_the_shortest_distance_for_each_node_nodesWithDifferentDimensions(
            self):
        nodes = [[1, 1], [0, 1, 2]]
        with self.assertRaises(AssertionError):
            mi.get_the_shortest_distance_for_each_node(nodes)


class TestMathematicalImplementationGetTheIndexOfTheClosestNodes(
        unittest.TestCase):

    def setUp(self):
        self.SAMPLE_2 = "samples/sample_input_2_8.tsv"

    def test_get_the_index_of_the_closest_nodes_nodesWithNoElements(self):
        nodes = []
        with self.assertRaises(AssertionError):
            mi.get_the_index_of_the_closest_nodes(nodes)

    def test_get_the_index_of_the_closest_nodes_nodesWithOneElementOnly(self):
        nodes = [1, 1]
        with self.assertRaises(AssertionError):
            mi.get_the_index_of_the_closest_nodes(nodes)

    def test_get_the_index_of_the_closest_nodes_TwoIndexesOnly(self):
        data_file = fileReader.get_table_from_file(self.SAMPLE_2)

        result = mi.get_the_index_of_the_closest_nodes(data_file)
        self.assertEqual(len(result), 2)


class TestResultChecks(unittest.TestCase):

    def setUp(self):
        self.SAMPLE_2 = "samples/sample_input_2_8.tsv"
        self.SAMPLE_3 = "samples/sample_input_3_1000.tsv"
        self.SAMPLE_4 = "samples/sample_input_4_4.tsv"
        self.SAMPLE_10 = "samples/sample_input_10_100.tsv"
        self.SAMPLE_100 = "samples/sample_input_100_100.tsv"

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


def main():
    unittest.main()


if __name__ == '__main__':
    main()
