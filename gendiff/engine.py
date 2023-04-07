from gendiff.parse import parse


def generate_diff(file1_path: str, file2_path: str) -> str:
    file1, file2 = parse(file1_path, file2_path)
    keys = sorted(list(set(file1) | set(file2)))
    result = "{\n"
    for key in keys:
        result += key_comparison(key, file1, file2)
    result += "}"
    return result


def key_comparison(key, file1: dict, file2: dict):
    if key in file1 and key in file2:
        return key_in_both_files(key, file1, file2)
    elif key in file1:
        return f"  - {key}: {normalized_value(file1[key])}\n"
    else:
        return f"  + {key}: {normalized_value(file2[key])}\n"


def key_in_both_files(key, file1, file2):
    if file1[key] == file2[key]:
        return f"    {key}: {normalized_value(file1[key])}\n"
    else:
        return ''.join((
            f"  - {key}: {normalized_value(file1[key])}\n",
            f"  + {key}: {normalized_value(file2[key])}\n"
        ))


def normalized_value(value):
    if value is True:
        return "true"
    elif value is False:
        return "false"
    elif value is None:
        return "null"
    return value
