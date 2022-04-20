#!/usr/bin/env python

import argparse
parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file', type=str, help='Input name first file')
parser.add_argument('second_file', type=str, help='Input name second file')
parser.add_argument('-f', '--format', help='set format of output')
args = parser.parse_args()


def generate_diff():
    pass
