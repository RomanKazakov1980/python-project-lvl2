# #!/usr/bin/env python
import json
#
# import argparse
# parser = argparse.ArgumentParser(description='Generate diff')
# parser.add_argument('first_file', type=str, help='Input name first file')
# parser.add_argument('second_file', type=str, help='Input name second file')
# parser.add_argument('-f', '--format', help='set format of output')
# args = parser.parse_args()
#
ADD = '+'


def generate_diff(pathfile1, pathfile2):
    data_file1 = json.load(open(pathfile1))
    data_file2 = json.load(open(pathfile2))
    data_difference = {}
    keys1, keys2 = set(data_file1.keys()), set(data_file2.keys())
    combined_keys = sorted(keys1 | keys2)
    for key in combined_keys:
        if key not in keys1 and key in keys2:
            data_difference[key] = {'type': '+', 'value': data_file2[key]}
        elif key in keys1 and key not in keys2:
            data_difference[key] = {'type': '-', 'value': data_file1[key]}
        elif data_file1[key] == data_file2[key]:
            data_difference[key] = {'type': ' ', 'value': data_file1[key]}
        else:
            data_difference[key] = {'type': 'dif', 'value': {'old_value': data_file1[key], 'new_value': data_file2[key]}}
    return data_difference


def main():
    print(generate_diff('file1.json', 'file2.json'))


if __name__ == '__main__':
    main()
