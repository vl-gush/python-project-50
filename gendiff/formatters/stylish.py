import itertools

STATUSES = {
    "added": "  + ",
    "removed": "  - ",
    "no changed": "    ",
}


def render(data: dict, depth: int = 0) -> str:
    keys = sorted(set(data))
    lines = []
    for key in keys:
        if is_children(data[key]):
            space = "    " * (depth + 1)
            lines.append(
                f"{space}{key}: {render(data[key], depth=depth + 1)}"
            )
        else:
            space = "    " * depth
            lines.append(f"{space}{generate_lines(key, data[key], depth + 1)}")
    result = itertools.chain("{", lines, ["    " * depth + "}"])
    return "\n".join(result)


def generate_lines(key, item, depth):
    status = item[0]
    if status == "changed":
        old_value, new_value = item[1:]
        return ("\n" + "    " * (depth - 1)).join([
            generate_lines(key, ["removed", to_string(old_value)], depth),
            generate_lines(key, ["added", to_string(new_value)], depth)
        ])
    value = item[1]
    if is_children(value):
        return f"{STATUSES[status]}{key}: {render(value, depth)}"
    return f"{STATUSES[status]}{key}: {to_string(value)}"


def is_children(value):
    return isinstance(value, dict)


def to_string(value):
    if value is True:
        return "true"
    elif value is False:
        return "false"
    elif value is None:
        return "null"
    return value
