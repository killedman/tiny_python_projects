#! /usr/bin/env python

import argparse


def get_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('str', help='need input str')
    args = parser.parse_args()
    return args


def main():
    args = get_arg()
    str_ = args.str
    jump_dict = {'1': '9', '2': '8', '3': '7', '4': '6', '5': '0', '6': '4', '7': '3', '8': '2', '9': '1', '0': '5'}
    ans = []
    for x in str_:
        if x in jump_dict:
            x = jump_dict[x]
        ans.append(x)
    print(''.join(ans))





if __name__ == "__main__":
    main()
