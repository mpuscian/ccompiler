import argparse
import subprocess
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("file_path", type=Path)
p = parser.parse_args()
f = open(p.file_path, "r")
print(f.name)
cmd = "gcc " + f.name
subprocess.Popen(cmd, shell=True)
