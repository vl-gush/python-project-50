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
        if status == "changed":
            if data[status, key][0] == "children":
                value = data[status, key][1]
                line = [
                    f"{'    ' * (depth + 1)}{key}: {render(value, depth + 1)}"
                ]
            else:
                value1, value2 = data[status, key]
                value1_type, value1 = value1
                value2_type, value2 = value2
                line = []
                if value1_type == "children":
                    line.append(f"{'    ' * depth}{STATUSES['removed']}{key}: {render(value1, depth + 1)}")
                else:
                    line.append(f"{'    ' * depth}{STATUSES['removed']}{key}: {to_string(value1)}")
                if value2_type == "children":
                    line.append(f"{'    ' * depth}{STATUSES['added']}{key}: {render(value2, depth + 1)}")
                else:
                    line.append(f"{'    ' * depth}{STATUSES['added']}{key}: {to_string(value2)}")
        else:
            value_type, value = data[status, key]
            if value_type == "children":
                line = [f"{'    ' * depth}{STATUSES[status]}{key}: {render(value, depth + 1)}"]
            else:
                line = [f"{'    ' * depth}{STATUSES[status]}{key}: {to_string(value)}"]
        lines.extend(line)
    result = itertools.chain("{", lines, ["    " * depth + "}"])
    return "\n".join(result)


def to_string(value):
    if value is True:
        return "true"
    elif value is False:
        return "false"
    elif value is None:
        return "null"
    return value
