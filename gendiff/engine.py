from gendiff.parse import parse


def generate_diff(file_before_path: str, file_after_path: str) -> str:
    file_before, file_after = parse(file_before_path, file_after_path)
    keys = sorted(list(set(file_before) | set(file_after)))
    result = "{\n"
    for key in keys:
        if key in file_before and key in file_after:
            if file_before[key] == file_after[key]:
                result += f"    {key}: {normalized_value(file_before[key])}\n"
            else:
                result += f"  - {key}: {normalized_value(file_before[key])}\n"
                result += f"  + {key}: {normalized_value(file_after[key])}\n"
        elif key in file_before:
            result += f"  - {key}: {normalized_value(file_before[key])}\n"
        else:
            result += f"  + {key}: {normalized_value(file_after[key])}\n"
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
