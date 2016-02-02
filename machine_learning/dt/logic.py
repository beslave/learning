# coding: utf-8

from collections import Counter
from math import log


def shannon_entropy(data_set):
    entropy = 0.0
    labels_counter = Counter()
    num_entries = len(data_set)

    for data_vector in data_set:
        labels_counter[data_vector[-1]] += 1

    for label, count in labels_counter.iteritems():
        probability = float(count) / num_entries
        entropy -= probability * log(probability, 2)

    return entropy


def split_data_set(data_set, axis, value):
    ret_data_set = []

    for data_vector in data_set:
        if data_vector[axis] == value:
            reduced_data_vector = data_vector[:axis]
            reduced_data_vector.extend(data_vector[axis + 1:])
            ret_data_set.append(reduced_data_vector)

    return ret_data_set
