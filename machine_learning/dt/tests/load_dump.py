# coding: utf-8

from fabric.api import task

from dt.logic import create_tree, dump_tree, load_tree


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

    print 'Dump tree:\t', tree
    dump_tree(tree, 'decision_tree/dump_tree.txt')

    print 'Loaded tree:\t', load_tree('decision_tree/dump_tree.txt')
