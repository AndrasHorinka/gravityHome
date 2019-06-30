from scipy.spatial import distance
from services import converter


def calculate_distance_of_each_nodes(nodes):
    """
    :param nodes: an NxM matrix where N stands for Nodes and M stands for the coordinates of the Nodes
    :return: an NxM matrix where N stands for the Nodes and M stands for the distance of N(i) to N(each other)
    """
    try:
        assert all([True for node in nodes if len(node) == len(
            nodes[0])]), "Not all nodes share the same dimension"
        assert all([[True for dist in node if isinstance(float(dist), float)]
                    for node in nodes]), "Not all coordinates are numbers"

        return distance.cdist(nodes, nodes, 'euclidean')

    except AssertionError as a:
        raise a from None
    except TypeError as t:
        raise t from None
    except Exception as e:
        raise e from None


def get_the_index_of_the_closest_nodes(nodes):
    """
    :param nodes: an NxM matrix where N stands for Nodes and M stands for the coordinates of the Nodes
    :return: tuple(index of Node_a, index of Node_b) --> indexes of the two closest nodes in the list of Nodes (N)
    """
    try:
        assert all([True for node in nodes if len(node) == len(
            nodes[0])]), "Not all nodes share the same dimension"
        assert all([[True for dist in node if isinstance(float(dist), float)]
                    for node in nodes]), "Not all coordinates are numbers"

        distances = converter.replace_zeros(
            calculate_distance_of_each_nodes(nodes))
        min_distance = converter.get_the_minimum_distance_of_nodes(distances)

        for outer_index, dist_from_node in enumerate(distances):
            for inner_index, dist in enumerate(dist_from_node):
                if dist == min_distance:
                    return outer_index + 1, inner_index + 1

    except AssertionError as a:
        raise a from None
    except TypeError as t:
        raise t from None
    except Exception as e:
        raise e from None
