from gendiff.formatters.stylish import render as stylish


def generate_diff(file1: dict, file2: dict, format=stylish) -> dict:
    print(file1)
    print(file2)
    return format(data_comparison(file1, file2))


def data_comparison(data1: dict, data2: dict) -> dict:
    keys = sorted(list(set(data1) | set(data2)))
    result = {}
    for key in keys:
        status, value = key_check(key, data1, data2)
        result[(status, key)] = value
    return result


def key_check(key: str, data1: dict, data2: dict) -> tuple:
    if key in data1 and key in data2:
        return key_in_both_data(key, data1, data2)
    elif key in data1:
        return "removed", generate_value(data1[key])
    elif key in data2:
        return "added", generate_value(data2[key])


def key_in_both_data(key: str, data1: dict, data2: dict) -> tuple:
    if data1[key] == data2[key]:
        return "no changed", generate_value(data1[key])
    return "changed", key_changed(data1[key], data2[key])


def key_changed(value1: any, value2: any) -> list:
    if is_children(value1) and is_children(value2):
        return ["children", data_comparison(value1, value2)]
    return [generate_value(value1), generate_value(value2)]


def generate_value(value: any) -> list:
    if is_children(value):
        return ["children", data_comparison(value, value)]
    return ["value", value]


def is_children(value: any) -> bool:
    return isinstance(value, dict)
