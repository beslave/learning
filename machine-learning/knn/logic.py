# coding: utf-8

from numpy import tile
from operator import itemgetter


def classify(x, data_set, labels, k):
    data_set_size = data_set.shape[0]
    diff_mat = tile(x, (data_set_size, 1)) - data_set
    sq_diff_mat = diff_mat ** 2
    sq_distances = sq_diff_mat.sum(axis=1)
    sorted_dist_indices = sq_distances.argsort()
    class_count = {}

    for i in range(k):
        vote_label = labels[sorted_dist_indices[i]]
        class_count[vote_label] = class_count.get(vote_label, 0) + 1

    sorted_class_count = sorted(
        class_count.iteritems(),
        key=itemgetter(1),
        reverse=True
    )

    return sorted_class_count[0][0]
