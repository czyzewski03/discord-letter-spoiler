#!/usr/bin/env python3

import sys
import argparse

def insert(text, symbol, mode='separate'):
    """Surround or separate every character in the input text with the symbol (or symbols) provided."""

    # 'separate' mode inserts the symbol between adjacent characters.
    if mode == 'separate':
        output = f'{symbol}'.join(list(text))
    
    # 'surround mode inserts the symbol around every character.
    elif mode == 'surround':
        output = ''.join([f'{symbol}{char}{symbol}' for char in text])
        # ignores spaces:    output = ''.join([f'{symbol}{char}{symbol}' if not char.isspace() else char for char in text])
    return output


parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', dest='input', help='input', required=True)
parser.add_argument('-s', '--symbol', dest='symbol', help='symbol', required=True)
parser.add_argument('-m', '--mode', dest='mode', help="mode (surround/separate); 'separate' mode inserts the symbol between adjacent characters, 'surround' mode inserts the symbol around every character", default='separate')
args = parser.parse_args()

if args.mode.lower() != 'separate' and args.mode.lower() != 'surround':
    parser.error("argument -m/--mode: expected 'surround' or 'separate'")

output = insert(args.input, args.symbol, args.mode.lower())
print(output)