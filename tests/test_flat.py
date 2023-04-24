from gendiff.engine import generate_diff
from gendiff.parse import parse
from gendiff.formatters.stylish import formatter as stylish


def test_flat():
    json_file1 = parse("tests/fixtures/flat1.json")
    json_file2 = parse("tests/fixtures/flat2.json")

    yaml_file1 = parse("tests/fixtures/flat1.yaml")
    yaml_file2 = parse("tests/fixtures/flat2.yaml")

    result = open("tests/fixtures/flat_result.txt").read()
    assert generate_diff(json_file1, json_file2, stylish) == result
    assert generate_diff(yaml_file1, yaml_file2, stylish) == result
