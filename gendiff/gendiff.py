import json


def generate_diff(pathfile1, pathfile2):
    data_file1 = json.loads(get_data(pathfile1))
    data_file2 = json.loads(get_data(pathfile2))
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


def get_data(pathfile):
    with open(pathfile) as file:
        data = file.read()
        return data
