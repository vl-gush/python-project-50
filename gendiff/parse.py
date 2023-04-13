import json
import yaml


def parse(file_path: str) -> dict:
    if file_path.endswith('.json'):
        file = json.load(open(file_path))
    elif file_path.endswith(('.yaml', '.yml')):
        file = yaml.load(open(file_path), Loader=yaml.SafeLoader)
    return file
