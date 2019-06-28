import unittest

from implementations import mathematical_imp as mi
from services import fileReader


class TestFileReader(unittest.TestCase):

    def setUp(self):
        self.SAMPLE_2 = "samples/sample_input_2_8.tsv"
        self.SAMPLE_4 = "samples/sample_input_4_4.tsv"

    def test_fileReader_sample_2(self):
        data_file = fileReader.get_table_from_file(self.SAMPLE_2)
        expected_data_file = [
            [str(-262972), str(508697)],
            [str(-311943.65362731507), str(370239.3559213022)],
            [str(742431), str(-772652)],
            [str(-346046), str(696615.3537438104)],
            [str(194172), str(103527)],
            [str(726621.8167057682), str(-813087.8844925504)],
            [str(167923), str(-312455.0459619701)],
            [str(499664.42762545496), str(72395.09685360803)]
        ]

        self.assertEqual(
            data_file,
            expected_data_file,
            "FileReader Sample 2 is NOT OK!")

    def test_fileReader_sample_4(self):
        data_file = fileReader.get_table_from_file(self.SAMPLE_4)
        expected_data_file = [
            [str(653725), str(-422117.9078937047), str(-483855), str(-579967)],
            [str(-543446.8852285817), str(-319599.12096280814), str(130119), str(42410.4020668423)],
            [str(-800188), str(58364), str(586736), str(-409415)],
            [str(-607784.1676060366), str(400299), str(-925526.2019860733), str(-779617)]
        ]

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

    def test_get_squares_of_coordinates_incorrect_type(self):
        # TODO: check why typeerror is not raised
        node_a = 2
        node_b = [0, 0]
        with self.assertRaises(TypeError):
            mi.get_squares_of_coordinates(node_a, node_b)

    def test_get_squares_of_coordinates_zeroLengthList(self):
        # TODO: check why assertion error is not thrown
        node_a = []
        node_b = [0, 0]
        with self.assertRaises(AssertionError):
            mi.get_squares_of_coordinates(node_a, node_b)


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

    def test_get_the_closest_node_from_origin_noDestinationCoordinates(self):
        node_a = [1, 1]
        nodes = [[0], [1, 1]]
        with self.assertRaises(TypeError):
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


class TestMathematicalImplementationResultChecks(
        unittest.TestCase):

    def setUp(self):
        self.SAMPLE_2 = "samples/sample_input_2_8.tsv"
        self.SAMPLE_3 = "samples/sample_input_3_1000.tsv"
        self.SAMPLE_4 = "samples/sample_input_4_4.tsv"
        self.SAMPLE_10 = "samples/sample_input_10_100.tsv"
        self.SAMPLE_100 = "samples/sample_input_100_100.tsv"

    def test_sample2_results(self):
        # TODO: mock out the fileReader
        data_file = fileReader.get_table_from_file(self.SAMPLE_2)

        expected_result = (3, 6)
        result = mi.get_the_index_of_the_closest_nodes(data_file)
        self.assertEqual(result, expected_result)

    def test_sample3_results(self):
        # TODO: mock out the fileReader
        data_file = fileReader.get_table_from_file(self.SAMPLE_3)

        expected_result = (223, 388)
        result = mi.get_the_index_of_the_closest_nodes(data_file)
        self.assertEqual(result, expected_result)

    def test_sample4_results(self):
        # TODO: mock out the fileReader
        data_file = fileReader.get_table_from_file(self.SAMPLE_4)

        expected_result = (2, 3)
        result = mi.get_the_index_of_the_closest_nodes(data_file)
        self.assertEqual(result, expected_result)

    def test_sample10_results(self):
        # TODO: mock out the fileReader
        data_file = fileReader.get_table_from_file(self.SAMPLE_10)

        expected_result = (40, 94)
        result = mi.get_the_index_of_the_closest_nodes(data_file)
        self.assertEqual(result, expected_result)

    def test_sample100_results(self):
        # TODO: mock out the fileReader
        data_file = fileReader.get_table_from_file(self.SAMPLE_100)

        expected_result = (48, 96)
        result = mi.get_the_index_of_the_closest_nodes(data_file)
        self.assertEqual(result, expected_result)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
