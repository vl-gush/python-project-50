from gendiff.engine import generate_diff


def test_flat():
    json_file1 = "tests/fixtures/flat1.json"
    json_file2 = "tests/fixtures/flat2.json"

    yaml_file1 = "tests/fixtures/flat1.yaml"
    yaml_file2 = "tests/fixtures/flat2.yaml"

    result = open("tests/fixtures/plain_flat_result.txt").read()
    assert generate_diff(json_file1, json_file2, "plain") == result
    assert generate_diff(yaml_file1, yaml_file2, "plain") == result


def test_nested():
    json_file1 = "tests/fixtures/nested1.json"
    json_file2 = "tests/fixtures/nested2.json"

    yaml_file1 = "tests/fixtures/nested1.yaml"
    yaml_file2 = "tests/fixtures/nested2.yaml"

    result = open("tests/fixtures/plain_nested_result.txt").read()
    assert generate_diff(json_file1, json_file2, "plain") == result
    assert generate_diff(yaml_file1, yaml_file2, "plain") == result
