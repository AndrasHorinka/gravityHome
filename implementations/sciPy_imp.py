from scipy.spatial import distance


def replace_zeros(nodes):
    return [[max(node) + 2 if coord == 0 else coord for coord in node] for node in nodes]


def get_distance_of_closest_nodes(nodes):
    return min([min(node) for node in nodes])


def calculate_distance_of_each_nodes(nodes):
    return distance.cdist(nodes, nodes, 'euclidean')
