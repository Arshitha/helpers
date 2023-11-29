#!/usr/local/bin/python3
"""
Add program description here.
"""
import argparse
import subprocess
from pathlib import Path


def get_args():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, description=__doc__)

    parser.add_argument('-i', '--input', type=Path, action='store', dest='inputdir', metavar='INPUT_DIR',
                        help='Path to input BIDS directory.')
    parser.add_argument('-o', '--output', type=Path, action='store', dest='outdir', metavar='OUTPUT_DIR',
                        default=Path('.'), help="Path to directory that'll contain the outputs.")
    args = parser.parse_args()

    return args.inputdir.resolve(), args.outdir.resolve()


def run(cmdstr):
    p = subprocess.run(cmdstr, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='utf8', shell=True)
    return p.stdout


def main():
    return None


if __name__ == "__main__":
    main()
