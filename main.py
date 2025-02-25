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
        tokenization(preprocessed_file)
    if p.parse:
        print("Place for parse init")
    if p.codegen:
        print("Place for codegen init")
    return 0


def tokenization(filename):
    file = open(filename, "r")
    single_string = file.read()  # returns file content as signle string
    # r'' - string raw literal
    pattern_identifier = r"[A-zA-Z_]\w*\b"
    pattern_constant = r"[0-9]+\b"
    pattern_int_keyword = r"int\b"
    pattern_void_keyword = r"void\b"
    pattern_return_keyword = r"return\b"
    pattern_op_par = r"\("
    pattern_clse_par = r"\)"
    pattern_op_brace = r"{"
    pattern_clse_brace = r"}"
    patter_semicolon = r";"
    tokens_list = []
    for char in single_string:
        token_identifier = re.search(pattern_identifier, char)
        if token_identifier is not None:
            tokens_list.append(char)
        token_constant = re.search(pattern_constant, char)
        if token_constant is not None:
            tokens_list.append(char)
        token_op_par = re.search(pattern_op_par, char)
        if token_op_par is not None:
            tokens_list.append(char)
        token_clse_par = re.search(pattern_clse_par, char)
        if token_clse_par is not None:
            tokens_list.append(char)
        token_op_brace = re.search(pattern_op_brace, char)
        if token_op_brace is not None:
            tokens_list.append(char)
        token_cls_brace = re.search(pattern_clse_brace, char)
        if token_cls_brace is not None:
            tokens_list.append(char)
        token_semicolon = re.search(patter_semicolon, char)
        if token_semicolon is not None:
            tokens_list.append(char)
    semicolons_found = re.findall(patter_semicolon, single_string)
    constant_found = re.findall(pattern_constant, single_string)
    identifiers_found = re.findall(pattern_identifier, single_string)
    ints_found = re.findall(pattern_int_keyword, single_string)
    voids_found = re.findall(pattern_void_keyword, single_string)
    returns_found = re.findall(pattern_return_keyword, single_string)
    op_pars_found = re.findall(pattern_op_par, single_string)
    op_braces_found = re.findall(pattern_op_brace, single_string)
    clse_braces_found = re.findall(pattern_clse_brace, single_string)
    print(tokens_list)
    pos = find_order(tokens_list, pattern_void_keyword)
    for x in range(pos[0] + 1, pos[1]):
        tokens_list[pos[0]] = tokens_list[pos[0]] + tokens_list[x]
        print(tokens_list[x])
    tokens_list = tokens_list[: pos[0] + 1] + tokens_list[pos[1] :]
    print(tokens_list)

    return 0


def find_order(list, pattern):
    pattern = pattern[:-2]
    temp_string = "".join(list)
    match = re.search(pattern, temp_string)
    first = match.start()
    last = match.end()
    pos = [first, last]
    return pos


if __name__ == "__main__":
    main()
