# coding: utf-8

from fabric.api import task

from dt.logic import classify, create_tree


@task
def test():
    labels = ['no surfacing', 'flippers']
    tree = create_tree([
        [1, 1, 'yes'],
        [1, 1, 'yes'],
        [1, 0, 'no'],
        [0, 1, 'no'],
        [0, 1, 'no'],
    ], labels[:])

    print classify(tree, labels, [1, 0])
    print classify(tree, labels, [1, 1])
