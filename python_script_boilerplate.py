import argparse
import subprocess
from pathlib import Path


def parse_arguments():
  parser = argparse.ArgumentParser(description="Does something worth doing.")

  parser.add_argument("--input_dir", type=Path, action='store', dest='inputdir', help="Path to input directory.")
  parser.add_argument("--output_dir", type=Path, action='store', dest='outdir', help="Path to output directory.")
  
  return parser.parse_args()
  
  
def run_shell_cmd(cmdstr):
  pipe = subprocess.Popen(cmdstr, bufsize=1, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                            universal_newlines=True, encoding='utf8', shell=True)
  return pipe.stdout
    
def main():
  return None


if __name__=="__main__":
  main()
  
