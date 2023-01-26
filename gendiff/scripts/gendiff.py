#!/usr/bin/env python

from gendiff.gendiff import generate_diff
import argparse


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str, help='Input name first file')
    parser.add_argument('second_file', type=str, help='Input name second file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
