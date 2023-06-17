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
    return generate_value(value, indent)


def generate_value(old_value, indent):
    status = old_value[0]
    if status == "no changed":
        new_value = check_values(old_value[1], indent + 4)
    elif status == "changed":
        new_value = (
            status,
            check_values(old_value[1], indent + 4),
            check_values(old_value[2], indent + 4),
        )
    else:
        new_value = (status, check_values(old_value[1], indent + 4))
    return new_value
