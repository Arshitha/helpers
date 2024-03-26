#!/usr/local/bin/python3
"""
Converts CTDB legends (generally) in BIDS valid JSON sidecar files.

@Authors: Arshitha Basavaraj, Eric Earl
@Date: 2023-11-04
"""
import argparse
import subprocess
from collections import defaultdict
from pathlib import Path

import pandas as pd


def get_args():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, description=__doc__)

    parser.add_argument('-i', '--input', type=Path, action='store', dest='input_dir', metavar='INPUT_DIR',
                        help='Path to input BIDS directory.')
    parser.add_argument('-o', '--output', type=Path, action='store', dest='output_dir', metavar='OUTPUT_DIR',
                        help="Path to directory that'll contain the outputs.")
    args = parser.parse_args()

    return args


def run(cmdstr):
    p = subprocess.run(cmdstr, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='utf8', shell=True)
    return p.stdout


def main():
    args = get_args()
    ffill_cols = ['QUESTION_TEXT', 'QUESTION_NAME', 'QUESTION_ALIAS']
    dict_of_dfs = pd.read_excel(args.input_dir, sheet_name=None)
    for sheetname in dict_of_dfs.keys():
        if "Legend" in sheetname:
            print(sheetname)
            df = dict_of_dfs[sheetname]
            for col in ffill_cols:
                if col in df.columns:
                    df[col] = df[col].ffill()

            d = defaultdict(lambda: defaultdict(dict))
            d['participant_id']['LongName'] = 'Participant Identifier'
            d["participant_id"]["Description"] = "Unique BIDS identifier for the participant in this study."

            for idx, row in df.iterrows():
                if 'QUESTION_ALIAS' in df.columns:
                    shortname = row['QUESTION_ALIAS']


if __name__ == "__main__":
    main()
