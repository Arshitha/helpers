#!/usr/local/bin/python3
"""
Generate a list of new identifiers from old identifier strings.
"""
import argparse
import subprocess
from pathlib import Path
import csv
import hashlib
import time
from itertools import permutations
from os import fspath

import numpy as np
import pandas as pd


def get_args():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, description=__doc__)

    parser.add_argument('-c', '--current-ids-list', type=Path, action='store', dest='curr_ids_list',
                        metavar='CURR_IDS_LIST',
                        help='Path to file with a list of current identifiers with one identifier per line.')
    parser.add_argument('-o', '--output-dir', type=Path, action='store', dest='output_dir', metavar='OUTPUT_DIR',
                        help="Path to output directory.")
    args = parser.parse_args()

    return args


def run(cmdstr):
    p = subprocess.run(cmdstr, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='utf8', shell=True)
    return p.stdout


def isduplicate(inp):
    """Checks for duplicates for an input list"""
    dupes = set([e for e in inp if inp.count(e) > 1])
    return list(dupes)


def generate_onid(onidlist, rvid):
    """Checks for duplicates for an input list"""
    hashcode = int(hashlib.sha256(rvid.encode('utf-8')).hexdigest(), 16) % 100000
    perms = set([''.join(c) for c in permutations(str(hashcode))])
    perms = sorted([int(p) for p in perms], reverse=True)
    ctr = 0
    onid = f'A0{perms[ctr]:06d}'
    # check for any potential duplicates
    while onid in onidlist:
        ctr += 1
        onid = f'A0{perms[ctr]:06d}'
    return onid


def main():
    args = get_args()

    with open(args.curr_ids_list, 'r') as f:
        curr_ids = [curr_id.strip() for curr_id in f.readlines()]

    # verifies if there are any duplicate openneuro_ids in the current id_linking_file
    curr_to_new_mapping = dict()
    new_ids = []
    if isduplicate(curr_ids):
        print(isduplicate(curr_ids))

    for curr_id in curr_ids:
        new_id = generate_onid(new_ids, curr_id)
        new_ids.append(new_id)
        curr_to_new_mapping[curr_id] = new_id

    # writing to a csv file
    timestr = time.strftime('%Y%m%d_%H%M%S')
    with open(args.output_dir.joinpath('id_linking_file_' + timestr + '.csv'), 'w', newline='') as csvfile:
        header = ['OLD_ID', 'NEW_ID']
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        for key, value in curr_to_new_mapping.items():
            writer.writerow({'OLD_ID': key, 'NEW_ID': value})


if __name__ == "__main__":
    main()
