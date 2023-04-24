import argparse
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain

FORMATS = {
    "stylish": stylish,
    "plain": plain,
}


def generate_parser():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.",
    )
    parser.add_argument(
        "-f", "--format",
        default="stylish",
        help="set format of output (default: stylish)"
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    args = parser.parse_args()
    return args
