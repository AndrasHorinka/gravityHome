# As we are not really interested in the exact distance, but rather the relation between the distances -
# we can ommit the sqrt call to save computation time.
# As we can assume that if norm(A) > norm (B) than sqrt(A) > sqrt(B).

def get_the_index_of_the_closest_node(nodes):
    """
    :param nodes: List of nodes with coordinates to be analyzed. [node1[x,y], node2[x,y]...] They can be n-dimensional nodes
    :return: index of the two closest node
    """
    distances = get_the_shortest_distance_for_each_node(nodes)
    min_distance = float("inf")
    node_a_index = int()
    node_b_index = int()

    for key, value in distances.items():
        if value[1] < min_distance:
            min_distance = value[1]
            node_a_index = key
            node_b_index = value[0] + key + 1

    return node_a_index, node_b_index


def get_the_shortest_distance_for_each_node(nodes):
    distances = dict()
    for i, node in enumerate(nodes):
        distances[i] = get_the_closest_node_from_origin(node, nodes[i+1:])

    return distances


def get_the_closest_node_from_origin(origin, nodes):
    """
    Returns the index and the distance of the closest other node of a set of nodes.
    :param origin: Origin node with list of coordinates.
    :param nodes: Set of nodes with coordinates to compare to.
    :return: A dictionary with (max_distance_index: max_distance_value)
    """
    max_distance = float("inf")
    max_distance_index = int()

    for i, node in enumerate(nodes):
        n_distance = get_distance_square(origin, nodes[i])

        if max_distance > n_distance:
            max_distance = n_distance
            max_distance_index = i

    return max_distance_index, max_distance


def get_distance_square(node_a, node_b):
    """
    :param node_a: coordinates of node A in a list.
    :param node_b: coordinates of node B in a list.
    :return: Returns the square of distance of two nodes as Float.
    """
    dist = 0
    for n in get_squares_of_coordinates(node_a, node_b):
        dist += n

    return dist


def get_squares_of_coordinates(node_a, node_b):
    """
    :param node_a: coordinates of node A in a list.
    :param node_b: coordinates of node B in a list.
    :return: Returns the square of two referring coordinates of the nodes. (A[i] - B[i]) ** 2
    """
    i = 0
    while i < len(node_a):
        yield (float(node_a[i]) - float(node_b[i])) ** 2
        i += 1
