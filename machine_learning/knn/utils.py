# coding: utf-8

from fabric.api import task
from numpy import array

from .logic import classify, import_dataset, normalize
from helpers import data_path


@task
def classify_person():
    filepath = data_path('datingTestSet2.txt')
    result_list = ['not at all', 'in small doses', 'in large doses']
    play_games = float(raw_input(
        'percentage of time spent playing video games? '
    ))
    ff_miles = float(raw_input(
        'frequent flier miles earned per year? '
    ))
    ice_cream = float(raw_input(
        'liters of ice cream consumed per year? '
    ))

    data_set, labels = import_dataset(filepath)
    norm_data_set, ranges, min_vals = normalize(data_set)
    data = array([ff_miles, play_games, ice_cream])
    norm_data = (data - min_vals) / ranges
    result = classify(norm_data, norm_data_set, labels, 7)

    print 'you will probably like this person: {}'.format(
        result_list[result - 1]
    )
