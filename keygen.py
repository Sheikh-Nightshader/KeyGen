import random
import string

RESET = '\033[0m'
BANNER_COLOR = '\033[1;32m'
SUCCESS_COLOR = '\033[1;34m'

BANNER_TEXT = r"""
    __ __           ______
   / //_/__  __  __/ ____/__  ____
  / ,< / _ \/ / / / / __/ _ \/ __ \
 / /| /  __/ /_/ / /_/ /  __/ / / /
/_/ |_\___/\__, /\____/\___/_/ /_/
          /____/ By Sheikh Nightshader
"""

def print_banner():
    print(f"{BANNER_COLOR}{BANNER_TEXT}{RESET}")

def generate_random_key(segment_length, num_segments, use_letters, use_digits):
    char_pool = ""
    if use_letters:
        char_pool += string.ascii_uppercase
    if use_digits:
        char_pool += string.digits

    segments = []
    for _ in range(num_segments):
        segment = ''.join(random.choices(char_pool, k=segment_length))
        segments.append(segment)

    return ''.join(segments)

def generate_multiple_keys(num_keys, segment_length, num_segments, use_letters, use_digits, add_dashes):
    keys = []
    for _ in range(num_keys):
        key = generate_random_key(segment_length, num_segments, use_letters, use_digits)
        if add_dashes:
            key = '-'.join([key[i:i+segment_length] for i in range(0, len(key), segment_length)])
        keys.append(key)
    return keys

def save_keys_to_file(keys, filename):
    with open(filename, 'w') as file:
        for key in keys:
            file.write(key + '\n')

print_banner()

num_keys = int(input("Enter the number of keys to generate: "))
segment_length = int(input("Enter the length of each segment: "))
num_segments = int(input("Enter the number of segments in each key, if not use 1: ") or 1)
use_letters = input("Use letters in keys? (y/n): ").strip().lower() == 'y'
use_digits = input("Use digits in keys? (y/n): ").strip().lower() == 'y'
add_dashes = input("Add dashes between characters? (y/n): ").strip().lower() == 'y'
filename = input("Enter the name of the output file: ").strip()

random_keys = generate_multiple_keys(num_keys, segment_length, num_segments, use_letters, use_digits, add_dashes)
save_keys_to_file(random_keys, filename)

print(f"{SUCCESS_COLOR}Generated {num_keys} keys and saved them to {filename}{RESET}")
