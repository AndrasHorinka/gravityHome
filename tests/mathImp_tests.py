# import libraries
import unittest

# import implementations
from implementations import mathematical_imp as mi

# import services
from services import fileReader


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


class TestMathematicalImplementationGetTheShortestDistanceForEachNodes(unittest.TestCase):

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


class TestMathematicalImplementationGetTheIndexOfTheClosestNodes(unittest.TestCase):

    def setUp(self):
        self.SAMPLE_2 = "../samples/sample_input_2_8.tsv"

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
