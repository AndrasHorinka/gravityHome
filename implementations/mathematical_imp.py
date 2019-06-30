# As we are not really interested in the exact distance, but rather the relation between the distances -
# we can omit the sqrt call to save computation time.
# As we can assume that if norm(A) > norm (B) than sqrt(A) > sqrt(B).


def get_squares_of_coordinates(node_a, node_b):
    """
    :param node_a: Node(A) with coordinates. N = [coord1, coord2, ... coordn)
    :param node_b: Node(B) with coordinates. N = [coord1, coord2, ... coordn)
    :return: An int referring to the square of the difference of coordinates at the same dimension. (A[i] - B[i]) ** 2
    """
    try:
        assert len(node_a) != 0, "Node A has no coordinates."
        assert len(node_b) != 0, "Node B has no coordinates."
        assert len(node_a) == len(node_b), "Nodes have different dimensions"

        i = 0
        while i < len(node_a):
            yield (node_a[i] - node_b[i]) ** 2
            i += 1

    except AssertionError as e:
        raise e from None
    except TypeError as t:
        raise t from None
    except Exception as e:
        raise e from None


def get_distance_square(
        node_a,
        node_b,
        _get_squares_of_coordinates=get_squares_of_coordinates):
    """
    :param node_a: Node(A) with coordinates. N = [coord1, coord2, ... coordn)
    :param node_b: Node(B) with coordinates. N = [coord1, coord2, ... coordn)
    :return: An int referring to the square of distance of Node(A) - Node(B).
    """
    try:
        assert len(node_a) != 0, "Node A has no coordinates."
        assert len(node_b) != 0, "Node B has no coordinates."
        assert len(node_a) == len(node_b), "Nodes have different dimensions"

        dist = 0
        for n in _get_squares_of_coordinates(node_a, node_b):
            dist += n

        return dist

    except AssertionError as e:
        raise e from None
    except TypeError as t:
        raise t from None
    except Exception as e:
        raise e from None


def get_the_closest_node_from_origin(
        origin, nodes, _get_distance_square=get_distance_square):
    """
    :param origin: Source Node to compare N(others) to. N = [coord1, coord2, ... coordn)
    :param nodes: an NxM matrix where N stands for Nodes and M stands for the coordinates of the Nodes
    :return: a tuple holding(index of Node(other), distance from Node(other)). The closest Node is referred to.
    """
    max_distance = float("inf")
    max_distance_index = int()

    try:
        assert len(origin) != 0, "Node has no coordinates."
        assert len(nodes) != 0, "No other coordinates found."

        for i, node in enumerate(nodes):
            assert len(nodes[i]) != 0, str(i) + ". Node has no coordinates"
            assert len(origin) == len(nodes[i]), str(
                origin) + " & " + str(nodes[i]) + " don't have the same dimensions"

            n_distance = _get_distance_square(origin, nodes[i])

            if max_distance > n_distance:
                max_distance = n_distance
                max_distance_index = i

        return max_distance_index, max_distance

    except AssertionError as e:
        raise e from None
    except TypeError as t:
        raise t from None
    except Exception as e:
        raise e from None


def get_the_shortest_distance_for_each_node(
        nodes, _get_the_closest_node_from_origin=get_the_closest_node_from_origin):
    """
    :param nodes: an NxM matrix where N stands for Nodes and M stands for the coordinates of the Nodes
    :return: a dictionary where index of N(i) is the key and value holds a tuple of (index N(other), distance from N(other))
    """
    try:
        assert len(nodes) > 2, "Only one node found"

        distances = dict()

        for i, node in enumerate(nodes):
            if i == len(nodes) - 1:
                break

            assert len(node) == len(nodes[i + 1]), str(node) + " & " + str(
                nodes[i + 1]) + " don't have the same dimensions"

            distances[i] = _get_the_closest_node_from_origin(
                node, nodes[i + 1:])

        return distances

    except AssertionError as e:
        raise e from None
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
        assert len(nodes) > 2, "Only one node found"

        distances = get_the_shortest_distance_for_each_node(nodes)
        min_distance = float("inf")
        node_a_index = int()
        node_b_index = int()

        for key, value in distances.items():
            if value[1] < min_distance:
                min_distance = value[1]
                node_a_index = key + 1
                node_b_index = value[0] + key + 2

        return node_a_index, node_b_index

    except AssertionError as e:
        raise e from None
    except TypeError as t:
        raise t from None
    except Exception as e:
        raise e from None
