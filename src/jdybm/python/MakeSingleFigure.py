# -*- coding: utf-8 -*-

__author__ = "Takayuki Osogami"
__copyright__ = "(C) Copyright IBM Corp. 2015"

import numpy as np
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def subplot(N, n, i, title=True):
    ax = fig.add_subplot(N, 1, i)
    image = np.array(x[n]).T
    ax.imshow(image, cmap=plt.cm.gray, interpolation="nearest")
    if title:
        if n == 0:
            ax.set_title('Before training', **title_font)
        else:
            num = str(n)
            if len(num) > 3:
                num = num[:-3] + "," + num[-3:]
            if len(num) > 7:
                num = num[:-7] + "," + num[-7:]
            ax.set_title('After training ' + num + " times", **title_font)
    plt.tick_params(axis='both', which='both', bottom='off', top='off',
                    right="off", left="off", labelleft="off",
                    labelbottom='off')
    if i == N:
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()
        plt.arrow(xlim[0], ylim[0] + 1, xlim[1] - xlim[0] - 1.5, 0, width=.1,
                  color="k", clip_on=False, head_width=1., head_length=1.5)


if __name__ == "__main__":

    from single import x, ScienseLL, sciense

    # nlist = [0, 10, 1000, 100000, 120000, 130000]
    nlist_all = sorted(x.keys())
    print "Found steps:", nlist_all
    nlist = [nlist_all[0]] + nlist_all[-2:]
    for n in nlist_all[1:-2]:
        if str(n)[0] == "1":
            nlist.append(n)
    nlist = sorted(nlist)
    print "Using steps:", nlist

    title_font = {'fontname': 'Times', 'size': '16', 'color': 'black',
                  'weight': 'normal', 'verticalalignment': 'bottom'}

    for i in range(len(nlist)):
        if i > 0:
            n = nlist[i]
        else:
            n = 0
        fig = plt.figure(figsize=(12, 2))
        subplot(1, n, 1, False)

        filename = "fig/SingleSCIENCE" + str(n) + ".png"
        fig.savefig(filename, format="png", bbox_inches='tight')

        filename = "fig/SingleSCIENCE" + str(n) + ".pdf"
        fig.savefig(filename, format="pdf", bbox_inches='tight')
        plt.clf()

    fig = plt.figure(figsize=(16, 6))
    ax = plt.axes([0, 0.3, 1, 0.7])  # [left, bottom, width, height]
    n = nlist[-1]
    y = []
    for v in ScienseLL[n]:
        y.append(-v)
        y.append(-v)
    z = []
    for i in range(len(y)):
        m = (i + 1) / 2
        z.append(m)
    ax.set_xlim([min(z), max(z)])
    ax.plot(z, y, linewidth=2)
    plt.tick_params(axis='x', which='both', bottom='off', top='off',
                    right="off", labelbottom="off")
    ax = plt.axes([0, 0, 1, 0.3])
    image = np.array(sciense).T
    ax.imshow(image, cmap=plt.cm.gray, interpolation="nearest")
    plt.tick_params(axis='both', which='both', bottom='off', top='off',
                    right="off", left="off", labelleft="off",
                    labelbottom='off')
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    plt.arrow(xlim[0], ylim[0] + 1, xlim[1] - xlim[0] - 1.5, 0, width=.1, color="k",
              clip_on=False, head_width=1., head_length=1.5)

    filename = "fig/AnomalySCIENCE.png"
    fig.savefig(filename, format="png", bbox_inches='tight')

    filename = "fig/AnomalySCIENCE.pdf"
    fig.savefig(filename, format="pdf", bbox_inches='tight')
    plt.clf()

