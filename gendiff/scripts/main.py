from gendiff.cli import generate_parser, FORMATS
from gendiff.engine import generate_diff
from gendiff.parse import parse


def main():
    parser = generate_parser()
    first_file = parse(parser.first_file)
    second_file = parse(parser.second_file)
    formatter = FORMATS[parser.format]
    print(generate_diff(first_file, second_file, formatter))


if __name__ == "__main__":
    main()
