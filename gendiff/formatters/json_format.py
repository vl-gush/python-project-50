from typing import Union
import json


def render(data: dict):
    return json.dumps(generate_dict(data), indent=4)


def generate_dict(data: dict) -> dict:
    keys = data.keys()
    result = {}
    for status, key in keys:
        if status == "changed":
            result[key] = key_changed(status, data[status, key])
        else:
            result[key] = generate_values(status, data[status, key])
    return result


def key_changed(status: str, value: any) -> Union[dict, list]:
    if value[0] == "children":
        value = value[1]
        return generate_dict(value)
    else:
        value1_type, value1 = value[0]
        value2_type, value2 = value[1]
        if value1_type == "children":
            value1 = generate_dict(value1)
        if value2_type == "children":
            value2 = generate_dict(value2)
        return [status, value1, value2]


def generate_values(status: str, value: any) -> Union[dict, list]:
    value_type, value = value
    if status == "no changed":
        if value_type == "children":
            return generate_dict(value)
        else:
            return value
    else:
        if value_type == "children":
            return [status, generate_dict(value)]
        else:
            return [status, value]
