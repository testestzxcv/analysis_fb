import collections
import os
import pytagcloud
import matplotlib.pyplot as plt


RESULT_DIRECTORY = "__results__/visualization"

def wordcloud(filename, wordfreq):
    taglist = pytagcloud.make_tags(wordfreq.items(), maxsize=80)
    # print(taglist)
    save_filename = '%s/wordcloud_%s.jpg' % (RESULT_DIRECTORY, filename)
    pytagcloud.create_tag_image(
        taglist,
        save_filename,
        size=(900, 600),
        fontname='Malgun',
        rectangular=False,
        background=(0, 0, 0))


def graph_bar(title=None, xlabel=None, ylabel=None, showgrid=False, values=None, ticks=None, filename=None, showgraph=True):
    fig, subplots = plt.subplots(1, 1)
    subplots.bar(range(len(values)), values, align='center')

    # ticks
    if ticks is not None and isinstance(ticks, collections.Sequence):
        subplots.set_xticks(range(len(ticks)))
        subplots.set_xticklabels(ticks, rotation=85, fontsize='xx-small')

    # title
    if title is not None and isinstance(title, str):
        subplots.set_title(title)

    # xlabel
    if xlabel is not None and isinstance(xlabel, str):
        subplots.set_xlabel(xlabel)

    # ylabel
    if ylabel is not None and isinstance(ylabel, str):
        subplots.set_xlabel(ylabel)

    # show grid
    subplots.grid(showgrid)

    if filename is not None and isinstance(filename, str):
        save_filename = '%s/bar_%s.png' % (RESULT_DIRECTORY, filename)
        plt.savefig(save_filename, dpi=400, bbox_inches='tight') # 여백없이



    # show graph
    if showgraph:
        plt.show()



if os.path.exists(RESULT_DIRECTORY) is False:
    os.mkdir(RESULT_DIRECTORY)