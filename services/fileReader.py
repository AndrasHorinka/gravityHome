def get_table_from_file(file_name):
    """
    Reads a file and returns it as a list of lists.
    Values within the columns are converted to floats!
    Lines are rows columns are separated by "\t"

    Args:
        file_name (str): name of file to read

    Returns:
         list: List of lists read from a file.
    """
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()

        table = [element.replace("\n", "").split("\t") for element in lines]

        nodes = list()
        for node in table:
            new_node = []
            for coordinate in node:
                new_node.append(float(coordinate))

            nodes.append(new_node)

        return nodes

    except FileNotFoundError as f:
        raise f from None
    except Exception as e:
        raise e from None
