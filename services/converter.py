def replace_zeros(distances):
    """
    :param distances: an NxM matrix where N stands for the Nodes and M stands for the distance of N(i) to N(each other)
    :return: an NxM matrix where N stands for the Nodes and M stands for the distance of N(i) to N(each other); where all zeroes are replaced by max+2 value.
    """
    try:
        assert len(distances) > 2, "There aren't enough nodes to compare"

        return [[max(dist_from_node) + 2 if dist == 0 else dist for dist in dist_from_node]
                for dist_from_node in distances]

    except AssertionError as a:
        raise a from None
    except TypeError as t:
        raise t from None
    except Exception as e:
        raise e from None


def get_the_minimum_distance_of_nodes(distances):
    """
    :param distances: an NxM matrix where N stands for the Nodes and M stands for the distance of N(i) to N(each other)
    :return: the smallest value from NxM matrix
    """
    try:
        return min([min(dist_from_node) for dist_from_node in distances])

    except TypeError as t:
        raise t from None
    except Exception as e:
        raise e from None
