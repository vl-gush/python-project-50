from gendiff.cli import generate_parser
from gendiff.engine import generate_diff


def main():
    parser = generate_parser()
    first_file = parser.first_file
    second_file = parser.second_file
    formatter = parser.format
    print(generate_diff(first_file, second_file, formatter))


if __name__ == "__main__":
    main()
