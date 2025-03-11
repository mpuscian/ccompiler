import argparse
import os
import re
import string
import subprocess
from pathlib import Path


# from lexer import *
class Pattern:
    Identifier = r"[a-zA-Z_]\w*\b"
    Constant = r"[0-9]+\b"
    Int_keyword = r"int\b"
    Void_keyword = r"void\b"
    Return_keyword = r"return\b"
    Open_par = r"\("
    Close_par = r"\)"
    Open_brace = r"{"
    Close_brace = r"}"
    Semicolon = r";"


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
    single_string = file.read()  # returns file content as single string
    # r'' - string raw literal
    counter = 0
    tokens = []
    string_lenght = len(single_string)
    while counter < string_lenght:
        char = single_string[counter]
        while char == string.whitespace:
            char = single_string[counter]
            counter += 1
        while re.search(Pattern.Identifier, char):
            temp_identifier = ""
            while re.search(Pattern.Identifier, char) or re.search(
                Pattern.Constant, char
            ):
                temp_identifier += char
                counter += 1
                char = single_string[counter]
            if (
                re.search(Pattern.Int_keyword, temp_identifier)
                or re.search(Pattern.Void_keyword, temp_identifier)
                or re.search(Pattern.Return_keyword, temp_identifier)
            ):
                tokens.append(["keyword", temp_identifier])
            else:
                tokens.append(["identifier", temp_identifier])
        if re.search(Pattern.Constant, char):
            number = ""
            while re.search(Pattern.Constant, char):
                number += char
                counter += 1
                char = single_string[counter]
            tokens.append(["Number", number])
        if (
            re.search(Pattern.Open_brace, char)
            or re.search(Pattern.Open_par, char)
            or re.search(Pattern.Close_brace, char)
            or re.search(Pattern.Close_par, char)
            or re.search(Pattern.Semicolon, char)
        ):
            other = ""
            other += char
            tokens.append(["Others", other])
        counter += 1
        print(char)
        print(tokens)
        print(counter)


if __name__ == "__main__":
    main()
