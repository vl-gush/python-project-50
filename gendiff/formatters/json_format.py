from typing import Union
import json


def render(data: dict):
    return json.dumps(generate_dict(data), indent=4)


def generate_dict(data: dict) -> dict:
    keys = data.keys()
    result = {}
    for status, key in keys:
        if status == "changed":
            result[key] = key_changed(data[status, key])
        else:
            result[key] = generate_values(status, data[status, key])
    return result


def key_changed(value: any) -> Union[dict, list]:
    if value[0] == "children":
        value = value[1]
        return generate_dict(value)
    else:
        value1 = generate_values("changed", value[0])
        value2 = generate_values("changed", value[1])
        return ["changed", value1, value2]


def generate_values(status: str, value: any) -> Union[dict, list]:
    value_type = value[0]
    new_value = generate_dict(value[1]) \
        if value_type == "children" else value[1]
    if status == "no changed" or status == "changed":
        return new_value
    return [status, new_value]
