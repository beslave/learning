# coding: utf-8

from fabric.api import task

from dt.logic import create_tree


@task
def test():
    labels = ['no surfacing', 'flippers']

    print create_tree([
        [1, 1, 'yes'],
        [1, 1, 'yes'],
        [1, 0, 'no'],
        [0, 1, 'no'],
        [0, 1, 'no'],
    ], labels[:])

    print create_tree([
        [1, 1, 'maybe'],
        [1, 1, 'yes'],
        [1, 0, 'no'],
        [0, 1, 'no'],
        [0, 1, 'no'],
    ], labels[:])
