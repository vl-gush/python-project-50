from gendiff.gendiff import generate_diff


def test_flat():
    file_before = "tests/fixtures/json_flat_before.json"
    file_after = "tests/fixtures/json_flat_after.json"
    result = open("tests/fixtures/json_flat_result.txt").read()
    assert generate_diff(file_before, file_after) == result
