# coding: utf-8

from os import listdir, path

from fabric.api import task
from numpy import zeros

from ..logic import classify, import_image
from helpers import data_path


def over_files(dir_relative_path):
    dirpath = data_path(dir_relative_path)
    filenames = listdir(dirpath)
    m = len(filenames)

    def generator():
        for i in xrange(m):
            filename = filenames[i]
            name, ext = path.splitext(filename)
            class_num = int(name.split('_')[0])
            data = import_image(path.join(dirpath, filename))
            yield i, class_num, data

    return m, generator()


@task
def test():
    width, height = 32, 32
    labels = []

    m, train_iterator = over_files('digits/training')
    training_mat = zeros((m, width * height))

    for i, class_num, data in train_iterator:
        labels.append(class_num)
        training_mat[i, :] = data

    error_count = 0.0
    m_test, test_iterator = over_files('digits/test')

    for i, test_class_num, data in test_iterator:
        classifier_result = classify(data, training_mat, labels, 3)

        msg = 'the classifier came back with: {:d}, the real answer is: {:d}'
        print msg.format(classifier_result, test_class_num)

        if classifier_result != test_class_num:
            error_count += 1

    print '\nthe total number of errors is: {}'.format(error_count)
    print '\nthe total error rate is: {:f}'.format(error_count / m_test)
