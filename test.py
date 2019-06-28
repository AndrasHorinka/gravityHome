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
            [-262972, 508697],
            [-311943.65362731507, 370239.3559213022],
            [742431, 772652],
            [-346046, 696615.3537438104],
            [194172, 103527],
            [726621.8167057682, 813087.8844925504],
            [167923, 312455.0459619701],
            [499664.42762545496, 72395.09685360803]
        ]

        self.assertEqual(data_file, expected_data_file, "FileReader Sample 2 is NOT OK!")

    def test_fileReader_sample_4(self):
        data_file = fileReader.get_table_from_file(self.SAMPLE_4)
        expected_data_file = [
            [653725, -422117.9078937047, -483855, -579967],
            [-543446.8852285817, -319599.12096280814, 130119, 42410.4020668423],
            [-800188, 58364, 586736, -409415],
            [-607784.1676060366, 400299, -925526.2019860733, -779617]
        ]

        self.assertEqual(data_file, expected_data_file, "FileReader Sample 4 is NOT OK!")


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
        result = 8
        for n in mi.get_squares_of_coordinates(node_a, node_b):
            result += n

        self.assertEqual(result, 0)

    def test_get_squares_of_coordinates_2d_m10_m20_p10_m20(self):
        node_a = [-10, -20]
        node_b = [10, 20]
        result = 2000
        for n in mi.get_squares_of_coordinates(node_a, node_b):
            result += n

        self.assertEqual(result, 0)

    def test_get_squares_of_coordinates_2d_m10_m20_p0_m0(self):
        node_a = [-10, -20]
        node_b = [0, 0]
        result = 500
        for n in mi.get_squares_of_coordinates(node_a, node_b):
            result += n

        self.assertEqual(result, 0)

    def test_get_squares_of_coordinates_3d_m10_m20_p0_m0(self):
        node_a = [-10, -20]
        node_b = [0, 0]
        result = 500
        for n in mi.get_squares_of_coordinates(node_a, node_b):
            result += n

        self.assertEqual(result, 0)

    def test_get_squares_of_coordinates_null_node(self):
        node_a = []
        node_b = [0, 0]
        self.assertRaises
        self.assertEqual(result, 0)

# class TestMathematicalImplementationGetSquareOfCoordinates(unittest.TestCase):

# TODO: create assertion tests if the two nodes doesn't have the same length
# TODO: create assertion test if the coordinates are null of a node (node_a[])
# TODO: create TypeAssertion test if the coordinates are not int/float - or can't be converted to it

def main():
    unittest.main()


if __name__ == '__main__':
    main()
