from gendiff.engine import generate_diff
from gendiff.parse import parse
from gendiff.formatters.plain import plain


def test_plain():
    json_file1 = parse("tests/fixtures/nested1.json")
    json_file2 = parse("tests/fixtures/nested2.json")

    yaml_file1 = parse("tests/fixtures/nested1.yaml")
    yaml_file2 = parse("tests/fixtures/nested2.yaml")

    result = open("tests/fixtures/plain_result.txt").read()
    assert generate_diff(json_file1, json_file2, plain) == result
    assert generate_diff(yaml_file1, yaml_file2, plain) == result
