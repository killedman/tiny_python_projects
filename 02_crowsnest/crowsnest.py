#!/usr/bin/env python

import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("word", help="a word")
    return parser.parse_args()


def main():
    args = get_args()
    word = args.word
    article = 'an' if word[0].lower() in 'aeiou' else 'a'
    print(f'Ahoy, Captain, {article} {word} off the larboard bow!')


if __name__ == "__main__":
    main()
