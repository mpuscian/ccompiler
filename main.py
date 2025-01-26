import argparse


def main():
    parser = argparse.ArgumentParser(description="Pass path to file")
    parser.add_argument("--path", help="Path to the file")
    args = parser.parse_args()
    print(f"Path given: {args.path}")
    f = open(args.path, "r")
    print(f.read())


if __name__ == "__main__":
    main()
