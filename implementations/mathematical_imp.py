# As we are not really interested in the exact distance, but rather the relation between the distances -
# we can omit the sqrt call to save computation time.
# As we can assume that if norm(A) > norm (B) than sqrt(A) > sqrt(B).


def get_the_index_of_the_closest_nodes(nodes):
    """
    :param nodes: List of nodes with coordinates to be analyzed. [node1[x,y], node2[x,y]...] They can be n-dimensional nodes
    :return: index of the two closest node
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

    except TypeError:
        # TODO: add logger
        raise TypeError('Incorrect type passed as parameter {0}', e)

    except AssertionError as e:
        # TODO: add logger
        raise AssertionError(e)

    except Exception as e:
        # TODO: add logger
        raise Exception(e)


def get_the_shortest_distance_for_each_node(nodes):
    try:
        assert len(nodes) > 2, "Only one node found"

        distances = dict()

        for i, node in enumerate(nodes):
            if i == len(nodes) - 1:
                break

            assert len(node) == len(nodes[i + 1]), str(node) + " & " + str(
                nodes[i + 1]) + " don't have the same dimensions"

            distances[i] = get_the_closest_node_from_origin(
                node, nodes[i + 1:])

        return distances

    except TypeError as e:
        # TODO: add logger
        raise TypeError('Incorrect type passed as parameter {0}', e)

    except AssertionError as e:
        # TODO: add logger
        raise AssertionError(e)

    except Exception as e:
        # TODO: add logger
        raise Exception(e)


def get_the_closest_node_from_origin(origin, nodes):
    """
    Returns the index and the distance of the closest other node of a set of nodes.
    :param origin: Origin node with list of coordinates.
    :param nodes: Set of nodes with coordinates to compare to.
    :return: A dictionary with (max_distance_index: max_distance_value)
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

            n_distance = get_distance_square(origin, nodes[i])

            if max_distance > n_distance:
                max_distance = n_distance
                max_distance_index = i

        return max_distance_index, max_distance

    except TypeError as e:
        # TODO: add logger
        raise TypeError('Incorrect type passed as parameter {0}', e)

    except AssertionError as e:
        # TODO: add logger
        raise AssertionError(e)

    except Exception as e:
        # TODO: add logger
        raise Exception(e)


def get_distance_square(node_a, node_b):
    """
    :param node_a: coordinates of node A in a list.
    :param node_b: coordinates of node B in a list.
    :return: Returns the square of distance of two nodes as Float.
    """

    try:
        assert len(node_a) != 0, "Node A has no coordinates."
        assert len(node_b) != 0, "Node B has no coordinates."
        assert len(node_a) == len(node_b), "Nodes have different dimensions"

        dist = 0
        for n in get_squares_of_coordinates(node_a, node_b):
            dist += n

        return dist

    except TypeError:
        # TODO: add logger
        print('Incorrect type passed as parameter')
        raise TypeError

    except AssertionError as e:
        # TODO: add logger
        raise AssertionError(e)

    except Exception as e:
        # TODO: add logger
        raise Exception(e)


def get_squares_of_coordinates(node_a, node_b):
    """
    :param node_a: coordinates of node A in a list.
    :param node_b: coordinates of node B in a list.
    :return: Returns the square of two referring coordinates of the nodes. (A[i] - B[i]) ** 2
    """
    try:
        assert len(node_a) != 0, "Node A has no coordinates."
        assert len(node_b) != 0, "Node B has no coordinates."
        assert len(node_a) == len(node_b), "Nodes have different dimensions"
        # TODO: add logger

        i = 0
        while i < len(node_a):
            yield (float(node_a[i]) - float(node_b[i])) ** 2
            i += 1

    except TypeError:
        # TODO: add logger
        raise TypeError('Incorrect type passed as parameter')

    except AssertionError as e:
        # TODO: add logger
        raise AssertionError(e)

    except Exception as e:
        # TODO: add logger
        raise Exception(e)
