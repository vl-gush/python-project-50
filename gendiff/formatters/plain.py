from gendiff.formatters.stylish import is_children, to_string


def render(data: dict, key_path: list = []) -> str:
    keys = sorted(set(data))
    lines = []
    for key in keys:
        if is_children(data[key]):
            line = render(data[key], key_path + [key])
        else:
            line = generate_lines(key, data[key], key_path)
        if line:
            lines.append(line)
    return "\n".join(lines)


def generate_lines(key, data, key_path):
    status = data[0]
    key_path = ".".join(key_path + [key])
    if status == "added":
        value = data[1]
        return f"Property '{key_path}' was added with value: \
{to_string(unpack_value(value))}"
    elif status == "removed":
        return f"Property '{key_path}' was removed"
    elif status == "changed":
        old_value, new_value = data[1:]
        return f"Property '{key_path}' was updated. From \
{to_string(unpack_value(old_value))} to {to_string(unpack_value(new_value))}"


def unpack_value(value):
    if isinstance(value, str):
        return f"'{value}'"
    elif isinstance(value, (dict, list)):
        return "[complex value]"
    return value
