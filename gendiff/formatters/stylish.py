import itertools

STATUSES = {
    "added": "  + ",
    "removed": "  - ",
    "no changed": "    ",
}


def render(data: dict, depth: int = 0) -> str:
    keys = data.keys()
    lines = []
    for status, key in keys:
        lines.extend(generate_lines(key, status, data[status, key], depth))
    result = itertools.chain("{", lines, ["    " * depth + "}"])
    return "\n".join(result)


def generate_lines(key: str, status: str, value: list, depth: int = 0):
    if status == "changed":
        line = key_changed(key, value, depth)
    else:
        value_type, old_value = value
        prefix = '    ' * depth + STATUSES[status]
        if value_type == "children":
            new_value = render(old_value, depth + 1)
        else:
            new_value = to_string(old_value)
        line = [f"{prefix}{key}: {new_value}"]
    return line


def key_changed(key: str, value: list, depth: int = 0):
    if value[0] == "children":
        value = value[1]
        line = [
            f"{'    ' * (depth + 1)}{key}: {render(value, depth + 1)}"
        ]
    else:
        value1, value2 = value
        value1_type, old_value1 = value1
        value2_type, old_value2 = value2
        line = []
        prefixes = [
            '    ' * depth + STATUSES['removed'],
            '    ' * depth + STATUSES['added'],
        ]
        new_values = [
            generate_value(value1_type, old_value1, depth + 1),
            generate_value(value2_type, old_value2, depth + 1)
        ]
        for prefix, new_value in zip(prefixes, new_values):
            line.append(f"{prefix}{key}: {new_value}")
    return line


def generate_value(value_type, old_value, depth):
    if value_type == "children":
        return render(old_value, depth)
    else:
        return to_string(old_value)


def to_string(value):
    if value is True:
        return "true"
    elif value is False:
        return "false"
    elif value is None:
        return "null"
    return value
