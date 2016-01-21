# coding: utf-8

from numpy import array

from .logic import classify


def create_data_set():
    features = array([
        [1.0, 1.1],
        [1.0, 1.0],
        [0.0, 0.0],
        [0.0, 0.1],
    ])
    labels = ['A', 'A', 'B', 'B']
    return features, labels


def test():
    features, labels = create_data_set()

    assert(classify([0, 0], features, labels, 3) == 'B')
