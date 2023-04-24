from gendiff.engine import generate_diff
from gendiff.parse import parse
from gendiff.formatters.stylish import stylish


def test_nested():
    json_file1 = parse("tests/fixtures/nested1.json")
    json_file2 = parse("tests/fixtures/nested2.json")

    yaml_file1 = parse("tests/fixtures/nested1.yaml")
    yaml_file2 = parse("tests/fixtures/nested2.yaml")

    result = open("tests/fixtures/nested_result.txt").read()
    assert generate_diff(json_file1, json_file2, stylish) == result
    assert generate_diff(yaml_file1, yaml_file2, stylish) == result
