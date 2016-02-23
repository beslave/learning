# coding: utf-8

from fabric.api import task

from ..logic import create_tree
from ..utils import create_plot

from helpers import data_path


@task
def test():
    with open(data_path('lenses.txt')) as f:
        lenses = [x.strip().split('\t') for x in f]
    lenses_labels = ['age', 'prescript', 'astigmatic', 'tear rate']
    tree = create_tree(lenses, lenses_labels)
    print tree
    create_plot(tree, name='lenses tree')
