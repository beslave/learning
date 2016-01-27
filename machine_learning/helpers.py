# coding: utf-8

import os


def data_path(filename):
    return os.path.join(
        os.getcwd(),
        'data',
        filename
    )


def data_out_path(filename):
    path = os.path.join(os.getcwd(), 'output', filename)
    dirpath = os.path.dirname(path)
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)
    return path
