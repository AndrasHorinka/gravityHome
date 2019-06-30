# import libraries
import unittest

# import implementations
from services import fileReader


class TestFileReader(unittest.TestCase):

    def setUp(self):
        self.SAMPLE_2 = "~/samples/sample_input_2_8.tsv"
        self.SAMPLE_4 = "~/samples/sample_input_4_4.tsv"

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
        expected_data_file = [
            [float(653725), float(-422117.9078937047), float(-483855), float(-579967)],
            [float(-543446.8852285817), float(-319599.12096280814), float(130119), float(42410.4020668423)],
            [float(-800188), float(58364), float(586736), float(-409415)],
            [float(-607784.1676060366), float(400299), float(-925526.2019860733), float(-779617)]
        ]

        self.assertEqual(
            data_file,
            expected_data_file,
            "FileReader Sample 4 is NOT OK!")
