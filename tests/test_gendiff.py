from gendiff.engine import generate_diff
import pytest


@pytest.mark.parametrize(
    "file1, file2, result, formatter", [
        ("tests/fixtures/file1.json",
         "tests/fixtures/file2.json",
         "tests/fixtures/stylish_result.txt",
         "stylish"),
        ("tests/fixtures/file1.yaml",
         "tests/fixtures/file2.yaml",
         "tests/fixtures/stylish_result.txt",
         "stylish"),
        ("tests/fixtures/file1.json",
         "tests/fixtures/file2.json",
         "tests/fixtures/plain_result.txt",
         "plain"),
        ("tests/fixtures/file1.yaml",
         "tests/fixtures/file2.yaml",
         "tests/fixtures/plain_result.txt",
         "plain"),
        ("tests/fixtures/file1.json",
         "tests/fixtures/file2.json",
         "tests/fixtures/json_result.txt",
         "json"),
        ("tests/fixtures/file1.yaml",
         "tests/fixtures/file2.yaml",
         "tests/fixtures/json_result.txt",
         "json"),
    ]
)
def test_gendiff(file1, file2, result, formatter):
    result = open(result).read()
    assert generate_diff(file1, file2, formatter) == result
