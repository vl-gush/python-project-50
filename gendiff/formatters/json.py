from gendiff.formatters.stylish import is_children
import json


def render(data):
    return json.dumps(generate_dict(data), indent=4)


def generate_dict(data, indent=4):
    keys = sorted(set(data))
    result = {}
    for key in keys:
        result[key] = check_values(data[key], indent)
    return result


def check_values(value, indent):
    if is_children(value):
        return generate_dict(value, indent + 4)
    elif not isinstance(value, list):
        return value
    status = value[0]
    if status == "no changed":
        new_value = check_values(value[1], indent + 4)
    elif status == "changed":
        new_value = (
            status,
            check_values(value[1], indent + 4),
            check_values(value[2], indent + 4),
        )
    else:
        new_value = (status, check_values(value[1], indent + 4))
    return new_value
