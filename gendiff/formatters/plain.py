from gendiff.formatters.stylish import to_string


def render(data: dict, key_path: list = []) -> str:
    keys = data.keys()
    lines = []
    for status, key in keys:
        if status == "changed":
            if data[status, key][0] == "children":
                value = data[status, key][1]
                lines.append(render(value, key_path + [key]))
            else:
                value1, value2 = data[status, key][0][1], data[status, key][1][1]
                key = ".".join(key_path + [key])
                lines.append(f"Property '{key}' was updated. From {to_string(unpack_value(value1))} to {to_string(unpack_value(value2))}")
        else:
            value_type, value = data[status, key]
            key = ".".join(key_path + [key])
            if status == "added":
                lines.append(f"Property '{key}' was added with value: {to_string(unpack_value(value))}")
            elif status == "removed":
                lines.append(f"Property '{key}' was removed")
    cleaning_from_empty_lines(lines)
    return "\n".join(lines)


def unpack_value(value):
    if isinstance(value, str):
        return f"'{value}'"
    elif isinstance(value, (dict, list)):
        return "[complex value]"
    return value


def cleaning_from_empty_lines(data):
    while "" in data:
        data.remove("")
