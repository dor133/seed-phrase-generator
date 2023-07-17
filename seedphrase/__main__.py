from constants import LANGUAGES, LENGTHS
from generator import strength, generate_seed

import argparse
import os


parser = argparse.ArgumentParser(
    description="Generate a seed phrase of variable length.")

parser.add_argument("length", type=int, choices=LENGTHS, metavar="length",
                    help="Length of seed phrase to be generated. The possible lengths are 12, 15, 18, 21 or 24 words.")
parser.add_argument("-s", "--save", action="store_true",
                    help="Save the seed phrase in a file 'seed.txt'.")
parser.add_argument("-l", "--language", choices=LANGUAGES.keys(), metavar="language",
                    help=f"The language in witch to generate the seed phrase. The possible languages are: en (english), zh (chinese simplified), zh2 (chinese traditional), fr (french), it (italian), ja (japanese), ko (korean), es (spanish). The default language is en (english)", default="en")

args = parser.parse_args()


try:
    strength = strength(args.length)

    seed = generate_seed(strength, args.language)
except Exception as e:
    print(f"An error occured: {e}")
    exit(1)

if args.save:
    file_path = os.path.abspath(__file__)
    current_dir = os.path.dirname(file_path)
    parent_dir = os.path.dirname(current_dir)

    output_path = os.path.join(parent_dir, "seed.txt")

    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(seed)
            print(
                f"The seed phrase has been saved in this current directory ({output_path})")
            print(
                "We highly recommend to store this file in a separed and secure repository.")
    except Exception as e:
        print(f"An error occured: {e}")
        exit(1)
else:
    print(f"Seed phrase (length: {args.length} words):\n{seed}")
