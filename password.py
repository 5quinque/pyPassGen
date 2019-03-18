#!/usr/bin/env python3

"""Securely generate random passwords
This scripts allows you to generate passwords
Using command line arguments you can:
- Set the length of the password
- Number of passwords to generate
- Generate password without numerical values 0-9
- Generate password with punctuation
"""

import random
import string
import argparse

def gen_pass(length, no_numerical=False, punctuation=False):
    """Generate a random password
    Parameters
    ----------
    length : int
        The length of the password
    no_numerical : bool, optional
        If true the password will be generated without 0-9
    punctuation : bool, optional
        If true the password will be generated with punctuation

    Returns
    -------
    string
        The generated password
    """
    characters = [string.ascii_letters]
    if not no_numerical:
        characters.append(string.digits)
    if punctuation:
        characters.append(string.punctuation)

    random.SystemRandom().shuffle(characters)

    chars_left = length - (len(characters) - 1)
    char_amounts = []

    for char_set in characters:
        i = random.SystemRandom().randint(1, chars_left)
        char_amounts.append(i)
        chars_left -= i - 1
    char_amounts[-1] += chars_left - 1

    password = ''
    for i, length in enumerate(char_amounts):
        password +=''.join(random.SystemRandom().choice(characters[i]) for _ in range(length))
    
    password = list(password)
    random.SystemRandom().shuffle(password)

    password = ''.join(password)

    return password

def main():
    """ Handle command line arguments and print passwords """
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--length", help="Length of password", type=int, default=8)
    parser.add_argument("-c", "--count", help="Number of passwords to generate", type=int, default=1)
    parser.add_argument("-n", "--no-numerical", help="Generate password without numerical values 0-9", action='store_true', default=False)
    parser.add_argument("-p", "--punctuation", help="Generate password with punctuation", action='store_true', default=False)
    args = parser.parse_args()

    for i in range(0, args.count):
        print(gen_pass(args.length, args.no_numerical, args.punctuation))

if __name__ == "__main__":
    main()
