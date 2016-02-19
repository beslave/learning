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


def choose_best_feature_to_split(data_set):
    num_features = len(data_set[0]) - 1
    base_entropy = shannon_entropy(data_set)
    best_info_gain = 0.0
    best_feature = -1

    for i in xrange(num_features):
        feature_list = [example[i] for example in data_set]
        unique_values = set(feature_list)
        new_entropy = 0.0

        for value in unique_values:
            sub_data_set = split_data_set(data_set, i, value)
            prob = len(sub_data_set) / float(len(data_set))
            new_entropy += prob * shannon_entropy(sub_data_set)

        info_gain = base_entropy - new_entropy

        if info_gain > best_info_gain:
            best_info_gain = info_gain
            best_feature = i

    return best_feature


def majority_class(class_list):
    return Counter(class_list).most_common()[0][0]


def create_tree(data_set, labels):
    class_list = [example[-1] for example in data_set]

    if class_list.count(class_list[0]) == len(class_list):
        return class_list[0]

    if len(data_set[0]) == 1:
        return majority_class(class_list)

    best_feature = choose_best_feature_to_split(data_set)
    best_feature_label = labels[best_feature]
    tree = {best_feature_label: {}}
    del labels[best_feature]
    feature_values = [example[best_feature] for example in data_set]
    unique_values = set(feature_values)

    for value in unique_values:
        sub_labels = labels[:]
        tree[best_feature_label][value] = create_tree(
            split_data_set(data_set, best_feature, value),
            sub_labels
        )

    return tree


def get_leafs_number(tree):
    num_leafs = 0
    label = tree.keys()[0]

    for value, node in tree[label].iteritems():
        num_leafs += get_leafs_number(node) if isinstance(node, dict) else 1

    return num_leafs


def get_tree_depth(tree):
    max_depth = 0
    label = tree.keys()[0]

    for value, node in tree[label].iteritems():
        depth = 1 + get_tree_depth(node) if isinstance(node, dict) else 1
        max_depth = max(max_depth, depth)

    return max_depth


def classify(tree, labels, data_vector):
    label = tree.keys()[0]
    label_index = labels.index(label)

    for value, node in tree[label].iteritems():
        if data_vector[label_index] == value:
            if isinstance(node, dict):
                class_label = classify(node, labels, data_vector)
            else:
                class_label = node

    return class_label
