# coding: utf-8

from matplotlib import pyplot as plt

from dt.logic import get_leafs_number, get_tree_depth
from helpers import data_out_path


decision_node = dict(boxstyle='sawtooth', fc='0.8')
leaf_node = dict(boxstyle='round4', fc='0.8')
arrow_args = dict(arrowstyle='<-')


def plot_node(node_text, center_node, parent_node, node_type):
    create_plot.ax1.annotate(
        node_text,
        xy=parent_node,
        xycoords='axes fraction',
        xytext=center_node,
        textcoords='axes fraction',
        va='center',
        ha='center',
        bbox=node_type,
        arrowprops=arrow_args
    )


def plot_mid_text(center_plot, parent_plot, text):
    x_mid = (parent_plot[0] - center_plot[0]) / 2.0 + center_plot[0]
    y_mid = (parent_plot[1] - center_plot[1]) / 2.0 + center_plot[1]
    create_plot.ax1.text(x_mid, y_mid, text)


def plot_tree(tree, parent_plot, node_text):
    num_leafs = get_leafs_number(tree)
    label = tree.keys()[0]
    center_plot = (
        plot_tree.x_off + (1.0 + num_leafs) / 2.0 / plot_tree.total_w,
        plot_tree.y_off
    )
    plot_mid_text(center_plot, parent_plot, node_text)
    plot_node(label, center_plot, parent_plot, decision_node)
    plot_tree.y_off = plot_tree.y_off - 1.0 / plot_tree.total_d

    for value, node in tree[label].iteritems():
        if isinstance(node, dict):
            plot_tree(node, center_plot, unicode(value))
        else:
            plot_tree.x_off = plot_tree.x_off + 1.0 / plot_tree.total_w
            plot_node(
                node,
                (plot_tree.x_off, plot_tree.y_off),
                center_plot,
                leaf_node
            )
            plot_mid_text(
                (plot_tree.x_off, plot_tree.y_off),
                center_plot,
                unicode(value)
            )

    plot_tree.y_off = plot_tree.y_off + 1.0 / plot_tree.total_d


def create_plot(tree, name='tree'):
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    create_plot.ax1 = plt.subplot(111, frameon=False, xticks=[], yticks=[])
    plot_tree.total_w = float(get_leafs_number(tree))
    plot_tree.total_d = float(get_tree_depth(tree))
    plot_tree.x_off = -0.5 / plot_tree.total_w
    plot_tree.y_off = 1.0
    plot_tree(tree, (0.5, 1.0), '')
    fig.savefig(data_out_path('decision_tree/{}.png').format(name))
