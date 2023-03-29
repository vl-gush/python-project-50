from gendiff.engine import generate_diff


def test_flat():
    json_file_before = "tests/fixtures/json_flat_before.json"
    json_file_after = "tests/fixtures/json_flat_after.json"

    yaml_file_before = "tests/fixtures/yaml_flat_before.yaml"
    yaml_file_after = "tests/fixtures/yaml_flat_after.yaml"

    result = open("tests/fixtures/flat_result.txt").read()
    assert generate_diff(json_file_before, json_file_after) == result
    assert generate_diff(yaml_file_before, yaml_file_after) == result
