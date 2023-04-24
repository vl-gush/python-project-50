def generate_diff(file1, file2, format) -> dict:
    return format(data_comparison(file1, file2))


def data_comparison(data1, data2):
    keys = sorted(list(set(data1) | set(data2)))
    result = {}
    for key in keys:
        result[key] = key_check(key, data1, data2)
    return result


def key_check(key, file1: dict, file2: dict):
    if key in file1 and key in file2:
        return key_in_both_files(key, file1, file2)
    elif key in file1:
        return generate_values("removed", file1[key])
    else:
        return generate_values("added", file2[key])


def key_in_both_files(key, file1, file2):
    if file1[key] == file2[key]:
        return generate_values("no changed", file1[key])
    if is_children(file1[key]) and is_children(file2[key]):
        return data_comparison(file1[key], file2[key])
    elif is_children(file1[key]):
        return [
            "changed",
            data_comparison(file1[key], file1[key]),
            file2[key]
        ]
    else:
        return ["changed", file1[key], file2[key]]


def generate_values(status, value):
    if is_children(value):
        return [status, data_comparison(value, value)]
    return [status, value]


def is_children(value):
    return isinstance(value, dict)
