"""Solution to Stack Overflow Challenge #15: Mystery Alphabet Decoder."""

import argparse
from pathlib import Path

from .decode import decode_input
from .deduce_alphabet_order import deduce_alphabet_order

DIR = Path(__file__).parent
INPUT_FILE = DIR / 'input.txt'
ALPHABET_FILE = DIR / 'alphabet.txt'

def find_order():
    alphabet = deduce_alphabet_order(INPUT_FILE)
    with ALPHABET_FILE.open('w') as alphabet_file:
        alphabet_file.write(alphabet)
    print(alphabet)
    print(f'length: {len(alphabet)} letters')

def get_language():
    parser = argparse.ArgumentParser()
    parser.add_argument('language')
    args = parser.parse_args()
    return args.language

def decode():
    language = get_language()
    input_file = INPUT_FILE
    with ALPHABET_FILE.open('r') as file:
        input_alphabet = file.read()
    output_file = DIR / f'decoded_as_{language}.txt'
    with (DIR / f'{language}.txt').open('r') as file:
        output_alphabet = file.read()
    decode_input(input_file, input_alphabet, output_file, output_alphabet)
