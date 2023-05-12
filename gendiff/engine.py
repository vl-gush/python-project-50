from gendiff.formatters.stylish import render as stylish


def generate_diff(file1, file2, format=stylish) -> dict:
    return format(data_comparison(file1, file2))


def data_comparison(data1, data2):
    keys = sorted(list(set(data1) | set(data2)))
    result = {}
    for key in keys:
        status, value = key_check(key, data1, data2)
        result[(status, key)] = value
    return result


def key_check(key, data1, data2):
    if key in data1 and key in data2:
        if data1[key] == data2[key]:
            status = "no changed"
            value = generate_value(data1[key])
        else:
            status = "changed"
            return status, key_changed(data1[key], data2[key])
    elif key in data1:
        status = "removed"
        value = generate_value(data1[key])
    elif key in data2:
        status = "added"
        value = generate_value(data2[key])
    return status, value


def generate_value(value):
    if is_children(value):
        return ["children", data_comparison(value, value)]
    return ["value", value]


def key_changed(value1, value2):
    if is_children(value1) and is_children(value2):
        return ["children", data_comparison(value1, value2)]
    return [generate_value(value1), generate_value(value2)]


def is_children(value):
    return isinstance(value, dict)


if __name__ == "__main__":
    from gendiff.parse import parse
    a = parse("tests/fixtures/nested1.json")
    b = parse("tests/fixtures/nested2.json")
    print(data_comparison(a, b))
