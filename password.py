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
    todo
    ----
    ensure at least one of every possible type of character
    exists in the password
    """
    chars=string.ascii_letters
    if not no_numerical:
        chars += string.digits
    if punctuation:
        chars += string.punctuation
    return ''.join(random.SystemRandom().choice(chars) for _ in range(length))

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
