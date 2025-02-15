import argparse
import os
import re
import subprocess
from pathlib import Path

# from lexer import *


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", type=Path)
    parser.add_argument("--lex", action="store_true", default=False)
    parser.add_argument("--parse", action="store_true", default=False)
    parser.add_argument("--codegen", action="store_true", default=False)

    p = parser.parse_args()
    f = open(p.file_path, "r")
    print(f.name)  # prints file path
    preprocessed_file = os.path.basename(f.name)
    preprocessed_file = preprocessed_file[:-1] + "i"
    print(preprocessed_file)
    cmd = (
        "gcc -E -P " + f.name + " -o " + preprocessed_file
    )  # command ran by shell
    subprocess.Popen(cmd, shell=True)
    if p.lex:
        tokenizing(preprocessed_file)
    if p.parse:
        print("Place for parse init")
    if p.codegen:
        print("Place for codegen init")
    return 0


def tokenizing(filename):
    file = open(filename, "r")
    single_string = file.read()  # returns file content as signle string
    # r'' - string raw literal
    pattern_identifier = r"[A-zA-Z_]\w*\b"
    x = re.findall(pattern_identifier, single_string)
    print(x)
    return 0


if __name__ == "__main__":
    main()
