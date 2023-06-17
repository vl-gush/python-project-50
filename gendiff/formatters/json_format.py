import json


def render(data: dict):
    def inner(data):
        keys = data.keys()
        result = {}
        for status, key in keys:
            if status == "changed":
                if data[status, key][0] == "children":
                    value = data[status, key][1]
                    result[key] = inner(value)
                else:
                    value1_type, value1 = data[status, key][0]
                    value2_type, value2 = data[status, key][1]
                    if value1_type == "children":
                        value1 = inner(value1)
                    if value2_type == "children":
                        value2 = inner(value2)
                    result[key] = [status, value1, value2]
            else:
                value_type, value = data[status, key]
                if status == "no changed":
                    if value_type == "children":
                        result[key] = inner(value)
                    else:
                        result[key] = value
                else:
                    if value_type == "children":
                        result[key] = [status, inner(value)]
                    else:
                        result[key] = [status, value]
        return result
    return json.dumps(inner(data), indent=4)
