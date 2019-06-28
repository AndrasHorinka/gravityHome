from services import fileReader
from implementations import mathematical_imp as mi

SAMPLE_2 = "samples/sample_input_2_8.tsv"
SAMPLE_3 = "samples/sample_input_3_1000.tsv"
SAMPLE_4 = "samples/sample_input_4_4.tsv"
SAMPLE_10 = "samples/sample_input_10_100.tsv"
SAMPLE_100 = "samples/sample_input_100_100.tsv"

OUTPUT_2 = "samples/sample_output_2_8.txt"
OUTPUT_3 = "samples/sample_output_3_100.txt"
OUTPUT_4 = "samples/sample_output_4_4.txt"
OUTPUT_10 = "samples/sample_output_10_100.txt"
OUTPUT_100 = "samples/sample_output_100_100.txt"


def main():
    sample2 = fileReader.get_table_from_file(SAMPLE_2)
    print("-" * 20)
    print(mi.get_the_index_of_the_closest_node(sample2))

    sample3 = fileReader.get_table_from_file((SAMPLE_3))
    print("-" * 20)
    print(mi.get_the_index_of_the_closest_node(sample3))


if __name__ == '__main__':
    main()
