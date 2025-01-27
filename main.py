import argparse
import os
import subprocess
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("file_path", type=Path)
p = parser.parse_args()
f = open(p.file_path, "r")
print(f.name)  # prints file path
preprocessed_file = os.path.basename(f.name)
preprocessed_file = preprocessed_file[:-1] + "i"
print(preprocessed_file)
cmd = "gcc -E -P " + f.name + " -o " + preprocessed_file  # command ran by shell
subprocess.Popen(cmd, shell=True)
