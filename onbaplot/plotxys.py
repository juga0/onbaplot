import logging
import os.path

import pylab as plt

from sbws.util.timestamp import now_fname

X_LABEL = 'Relays'
Y_LABEL = 'Bw (KB/s)'

colors = "krbgcmy"

plt.rcParams.update({
    'axes.grid': True,
})

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


def plot_xys(x, ys, labels, dpath, inverse=False, xlabel=X_LABEL,
             ylabel=Y_LABEL):
    log.debug('plot_data')
    plt.figure()
    for idx, y in enumerate(ys):
        label = labels[idx]
        plt.scatter(x, y, label=label, marker=".", s=1)
    plt.legend()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    # plt.show()
    outfname = "{}_{}.png".format(now_fname(), "_".join(labels))
    outfpath = os.path.join(dpath, outfname)
    log.debug('Saving plot in %s', outfpath)
    plt.savefig(outfpath)


def combine_bwfiles(bwfiles, sorted_by=None, inverse=False):
    assert len(bwfiles) == 2
    x = 0
    y1 = []
    y2 = []
    bwfile0 = bwfiles[0]
    bwfile1 = bwfiles[1]

    for bw_line in bwfile0.bw_lines:
        other_bw_line = bwfile1.bw_line_for_node_id(bw_line.node_id)
        if other_bw_line is not None:
            x += 1
            # TODO: attr instead of bw
            y1.append(bw_line.bw)
            y2.append(other_bw_line.bw)
    if inverse:
        return [i for i in range(0, x)], [y2, y1]
    return [i for i in range(0, x)], [y1, y2]
