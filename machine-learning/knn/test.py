# coding: utf-8

import os

from matplotlib import pyplot as plt
from numpy import array

from .logic import classify, import_dataset


def create_data_set():
    features = array([
        [1.0, 1.1],
        [1.0, 1.0],
        [0.0, 0.0],
        [0.0, 0.1],
    ])
    labels = ['A', 'A', 'B', 'B']
    return features, labels


def test_base():
    features, labels = create_data_set()
    assert(classify([0, 0], features, labels, 3) == 'B')


def test_dating_set():
    filepath = os.path.join(
        os.getcwd(),
        os.path.dirname(__file__),
        '..',
        'data',
        'datingTestSet2.txt'
    )
    data_set, labels = import_dataset(filepath)

    colors = []
    sizes = 15.0 * array(labels)

    for label in labels:
        if label == 1:
            color = 'red'
        elif label == 2:
            color = 'green'
        elif label == 3:
            color = 'blue'
        else:
            color = 'gray'

        colors.append(color)

    _fig = plt.figure()
    _ax = _fig.add_subplot(111)
    type1 = _ax.scatter([-10], [-10], s=15, c='red')
    type2 = _ax.scatter([-10], [-15], s=30, c='green')
    type3 = _ax.scatter([-10], [-20], s=45, c='blue')

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(data_set[:, 0], data_set[:, 1], c=colors, s=sizes)
    ax.set_xlabel('Frequent Flyier Miles Earned Per Year')
    ax.set_ylabel('Percentage of Time Spent Playing Video Games')

    ax.legend(
        [type1, type2, type3],
        ['Did Not Like', 'Liked in Small Doses', 'Liked in Large Doses'],
        loc=2
    )
    ax.grid(True)

    fig.savefig('games_vs_miles.png')

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(data_set[:, 1], data_set[:, 2], c=colors, s=sizes)
    ax.set_xlabel('Percentage of Time Spent Playing Video Games')
    ax.set_ylabel('Liters of Ice Cream Consumed Per Week')
    ax.legend(
        [type1, type2, type3],
        ['Did Not Like', 'Liked in Small Doses', 'Liked in Large Doses'],
        loc=4
    )
    ax.grid(True)
    fig.savefig('ice_cream_vs_games.png')
