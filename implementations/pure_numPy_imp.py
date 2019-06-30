import numpy as np

from services import converter


def get_euclidean_distance(vector1, vector2):
    """
    :param vector1: numPy.Array Node(A) containing coordinates
    :param vector2: numPy.Array Node(B) containing coordinates
    :return: float(square of distance of Node(A) and Node(B)
    """
    dist = [(a - b) ** 2 for a, b in zip(vector1, vector2)]
    return sum(dist)


def calculate_distance_of_each_nodes(
        nodes, _get_euclidean_distance=get_euclidean_distance):
    """
    :param nodes: an NxM matrix where N stands for Nodes and M stands for the coordinates of the Nodes
    :param _get_euclidean_distance: it is to pass the reference to the signature for performance optimalization
    :return: list(N) of lists (M) where N is Node(Source) and M is calculated distance of Node(others) from Source
    """
    distances = []

    for outer_index, source_node in enumerate(nodes):
        if outer_index == len(nodes) - 1:
            break

        source_vector = np.array(source_node)
        source_node_distances = list()

        for target_node in nodes[outer_index + 1:]:
            source_node_distances.append(
                _get_euclidean_distance(
                    source_vector,
                    np.array(target_node)))

        distances.append(source_node_distances)

    return distances


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

        distances = calculate_distance_of_each_nodes(nodes)
        min_distance = converter.get_the_minimum_distance_of_nodes(distances)

        for outer_index, dist_from_node in enumerate(distances):
            for inner_index, dist in enumerate(dist_from_node):
                if dist == min_distance:
                    return outer_index + 1, inner_index + outer_index + 2

    except AssertionError as a:
        raise a from None
    except TypeError as t:
        raise t from None
    except Exception as e:
        raise e from None
