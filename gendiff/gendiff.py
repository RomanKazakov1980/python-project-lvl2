import json
import yaml


def generate_diff(pathfile1, pathfile2):
    data_file1 = get_data(pathfile1)
    data_file2 = get_data(pathfile2)
    data_difference = {}
    keys1, keys2 = set(data_file1.keys()), set(data_file2.keys())
    combined_keys = sorted(keys1 | keys2)
    for key in combined_keys:
        if key not in keys1 and key in keys2:
            data_difference[key] = {
                'type': 'add',
                'value': data_file2[key],
            }
        elif key in keys1 and key not in keys2:
            data_difference[key] = {
                'type': 'removed',
                'value': data_file1[key],
            }
        elif data_file1[key] == data_file2[key]:
            data_difference[key] = {
                'type': ' ',
                'value': data_file1[key],
            }
        else:
            data_difference[key] = {
                'type': 'changed',
                'value': {
                    'removed': data_file1[key],
                    'add': data_file2[key],
                },
            }
    return str(data_difference)


def get_data(file_path):
    if file_path.endswith('.json'):
        with open(file_path) as json_file:
            return json.load(json_file)
    elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
        with open(file_path) as yaml_file:
            return yaml.safe_load(yaml_file)
    raise ValueError('Unsupported file format')
