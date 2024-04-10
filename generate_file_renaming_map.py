#!/usr/local/bin/python3
"""
Generate JSON file that maps current filenames to new filenames.
This is meant as a companion to the filemapper module written by Eric Earl.
"""
import argparse
import subprocess
from pathlib import Path
import pandas as pd
import re
import json


def get_args():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, description=__doc__)

    parser.add_argument('-i', '--input-dir', type=Path, action='store', dest='input_dir', metavar='INPUT_DIR',
                        help='Path to input BIDS directory with current filenames.')
    parser.add_argument('-m', '--id-mapping-file', required=True, dest='id_file', metavar='ID_MAPPING_FILE',
                        help=f"Path to a comma-separated file with exactly two columns named CURR_ID and NEW_ID. "
                             f"As the name suggests the CURR_ID column is expected to have current subject ids, "
                             f"and NEW_ID column is expected have the replacement to the current subject ids.")
    parser.add_argument('-o', '--output-dir', type=Path, action='store', dest='output_dir', metavar='OUTPUT_DIR',
                        help="Path to directory that will contain renamed BIDS file tree.")
    args = parser.parse_args()

    return args


def run(cmdstr):
    p = subprocess.run(cmdstr, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='utf8', shell=True)
    return p.stdout


def main():
    args = get_args()
    id_map_df = pd.read_csv(args.id_file)
    curr_to_new_filepaths = dict()
    for idx, curr_id in id_map_df.CURR_ID.items():
        new_id = id_map_df.at[idx, 'NEW_ID']
        curr_filepaths = args.input_dir.joinpath(f'sub-{curr_id}').rglob('*')
        for curr_filepath in curr_filepaths:
            new_filepath = re.sub(curr_id, new_id, str(curr_filepath))
            new_filepath = re.sub(str(args.input_dir), str(args.output_dir), new_filepath)
            curr_to_new_filepaths[str(curr_filepath)] = new_filepath

    with open(args.output_dir.joinpath('filerenaming_map.json'), 'w') as f:
        json.dump(curr_to_new_filepaths, f, indent=4)


if __name__ == "__main__":
    main()
