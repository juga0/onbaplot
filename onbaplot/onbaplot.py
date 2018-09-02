#!/usr/bin/env python3
import logging
import os
from argparse import ArgumentParser

# from sbws.lib.resultdump import load_recent_results_in_datadir
from sbws.lib.v3bwfile import V3BWFile

from .plotxys import plot_xys, combine_bwfiles

log = logging.getLogger(__name__)
OUT_DNAME = 'bw_graphs_data'
OUT_DPATH = os.path.join(os.path.dirname(os.path.abspath('.')),
                         'bw_graphs_data')


def main():
    p = ArgumentParser(description='Bw stats.')
    p.add_argument('-t', '--torflow')
    p.add_argument('-u', '--torflow2')
    p.add_argument('-s', '--sbws')
    p.add_argument('-w', '--sbws2')
    p.add_argument('-p', '--torflow-compare')
    p.add_argument('-o', '--output-dir')
    args = p.parse_args()

    output_dir = args.output_dir if args.output_dir else OUT_DPATH
    os.makedirs(output_dir, exist_ok=True)
    
    if args.torflow:
        log.debug('torflow')
        v100 = V3BWFile.from_v100_fpath(args.torflow_raw)
        x, ys, labels = v100.to_plt()
        plot_xys(x, ys, labels, output_dir)
        if args.torflow2:
            v110 = V3BWFile.from_v100_lines(args.storflow)
            x, ys, labels = combine_bwfiles([v100, v110])
            plot_xys(x, ys, labels, output_dir)
            x, ys, labels = combine_bwfiles([v110, v100], inverse=True)
            plot_xys(x, ys, labels, output_dir, inverse=True)
    elif args.sbws:
        log.debug('sbws')
        v110 = V3BWFile.from_v110_fpath(args.sbws)
        x, ys, labels = v110.to_plt()
        plot_xys(x, ys, labels, output_dir)
        if args.sbws2:
            v1102 = V3BWFile.from_v110_fpath(args.sbws2)
            # v1102.info_stats
            x, ys = combine_bwfiles([v1102, v110])
            plot_xys(x, ys, ['2nd sbws', 'sbws'], output_dir)
            x, ys = combine_bwfiles([v110, v1102], 'bw')
            plot_xys(x, ys, ['sbws', '2nd sbws'], output_dir)
        if args.torflow_compare:
            log.debug('')
            v100 = V3BWFile.from_v100_fpath(args.torflow_compare)
            # v100.info_stats
            x, ys = combine_bwfiles([v100, v110])
            plot_xys(x, ys, ['torflow', 'sbws'], output_dir)
            plot_xys(x, reversed(ys), ['sbws', 'torflow'], output_dir)


if __name__ == '__main__':
    main()
