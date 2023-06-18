from typing import NoReturn, Union
from gendiff.formatters.stylish import to_string


def render(data: dict, key_path: list = []) -> str:
    keys = data.keys()
    lines = []
    for status, key in keys:
        lines.append(generate_lines(key, status, data[status, key], key_path))
    cleaning_from_empty_lines(lines)
    return "\n".join(lines)


def generate_lines(key: str, status: str, value: list, key_path: list) -> str:
    if status == "changed":
        return key_changed(key, value, key_path + [key])
    else:
        return key_added_or_removed(key, status, value, key_path + [key])


def key_changed(key: str, value: list, key_path: list) -> str:
    if value[0] == "children":
        value = value[1]
        return render(value, key_path)
    value1 = to_string(unpack_value(value[0][1]))
    value2 = to_string(unpack_value(value[1][1]))
    key = ".".join(key_path)
    return f"Property '{key}' was updated. From {value1} to {value2}"


def key_added_or_removed(
        key: str,
        status: str,
        value: list,
        key_path: list
) -> str:
    value = to_string(unpack_value(value[1]))
    key = ".".join(key_path)
    if status == "added":
        return f"Property '{key}' was added with value: {value}"
    elif status == "removed":
        return f"Property '{key}' was removed"
    return ""


def unpack_value(value: any) -> Union[str, int]:
    if isinstance(value, str):
        return f"'{value}'"
    elif isinstance(value, (dict, list)):
        return "[complex value]"
    return value


def cleaning_from_empty_lines(data: list) -> NoReturn:
    while "" in data:
        data.remove("")
