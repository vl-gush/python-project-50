import json


def generate_diff(path1, path2):
    file1 = json.load(open(path1))
    file2 = json.load(open(path2))
    keys = sorted(list(set(file1) | set(file2)))
    result = "{\n"
    for key in keys:
        if key in file1 and key in file2:
            if file1[key] == file2[key]:
                result += f"    {key}: {normalized_value(file1[key])}\n"
            else:
                result += f"  - {key}: {normalized_value(file1[key])}\n"
                result += f"  + {key}: {normalized_value(file2[key])}\n"
        elif key in file1:
            result += f"  - {key}: {normalized_value(file1[key])}\n"
        else:
            result += f"  + {key}: {normalized_value(file2[key])}\n"
    result += "}"
    return result


def normalized_value(value):
    if value is True:
        return "true"
    elif value is False:
        return "false"
    elif value is None:
        return "null"
    return value
