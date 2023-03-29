import json
import yaml


def parse(file_before_path: str, file_after_path: str) -> tuple:
    if file_before_path.endswith('.json') and file_after_path.endswith('.json'):
        file_before = json.load(open(file_before_path))
        file_after = json.load(open(file_after_path))
    elif file_before_path.endswith(('.yaml', '.yml')) and \
            file_after_path.endswith(('.yaml', '.yml')):
        file_before = yaml.load(open(file_before_path), Loader=yaml.SafeLoader)
        file_after = yaml.load(open(file_after_path), Loader=yaml.SafeLoader)
    return file_before, file_after
