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


def run(cmdstr, logfile):
    """Runs the given command str as shell subprocess. If logfile object is provided, then the stdout and stderr of the
    subprocess is written to the log file.
    :param str cmdstr: A shell command formatted as a string variable.
    :param io.TextIOWrapper logfile: optional, File object to log the stdout and stderr of the subprocess.
    """
    if not logfile:
        subprocess.run(cmdstr, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='utf8', shell=True)
    else:
        subprocess.run(cmdstr, stdout=logfile, stderr=subprocess.STDOUT, encoding='utf8', shell=True)


def main():
    return None


if __name__ == "__main__":
    main()
