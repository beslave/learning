# coding: utf-8

from numpy import shape, tile, zeros
from operator import itemgetter


def import_dataset(filename, features_number=3):
    with open(filename) as f:
        lines_number = len(f.readlines())

    data_set = zeros((lines_number, features_number))
    labels = []

    with open(filename) as f:
        for i, line in enumerate(f.readlines()):
            line = line.strip()
            list_from_line = line.split('\t')
            data_set[i, :] = list_from_line[0: features_number]
            labels.append(int(list_from_line[-1]))

    return data_set, labels


def import_image(filename, width=32, height=32):
    data_set = zeros((1, width * height))

    with open(filename) as f:
        for i in range(height):
            line_str = f.readline()
            for j in range(width):
                data_set[0, 32 * i + j] = int(line_str[j])

    return data_set


def normalize(data_set):
    min_vals = data_set.min(0)
    max_vals = data_set.max(0)
    ranges = max_vals - min_vals
    norm_data_set = zeros(shape(data_set))
    m = data_set.shape[0]
    norm_data_set = data_set - tile(min_vals, (m, 1))
    norm_data_set = norm_data_set / tile(ranges, (m, 1))
    return norm_data_set, ranges, min_vals


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
