#!/usr/bin/env python

import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('brings', nargs='+', help='input brings')
    parser.add_argument('-s', '--sorted', action='store_true', help='first sort and output')
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    # print(f"args is {args}")
    brings = args.brings
    # print(f'before sort: {brings}')

    if args.sorted:
        # print("sorted is True")
        brings.sort()
        # print(f"after sort: {brings}")
    len_ = len(brings)

    if len_ == 1:
        print(f"You are bringing {brings[0]}.")
    elif len_ == 2:
        print(f"You are bringing {brings[0]} and {brings[1]}.")
    elif len_ >= 2:
        last = brings[-1]
        other = ', '.join(brings[:-1])+','
        print(f"You are bringing {other} and {last}.")


if __name__ == "__main__":
    main()
