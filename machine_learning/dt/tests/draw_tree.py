# coding: utf-8

from fabric.api import task

from dt.logic import create_tree
from dt.utils import create_plot


@task
def test():
    tree = create_tree([
        [1, 1, 'yes'],
        [1, 1, 'yes'],
        [1, 0, 'no'],
        [0, 1, 'no'],
        [0, 1, 'no'],
    ], ['no surfacing', 'flippers'])
    create_plot(tree, name='test_tree')
