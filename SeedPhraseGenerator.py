from mnemonic import Mnemonic
import argparse
import os
from unidecode import unidecode


languages_dict = {"en" : "english" ,
                  "zh" : "chinese_simplified",
                  "zh2" : "chinese_traditional",
                  "fr" : "french",
                  "it" : "italian",
                  "ja" : "japanese",
                  "ko" : "korean",
                  "es" : "spanish"}
strengths = [128, 160, 192, 224, 256]
lengths = [12, 15, 18, 21, 24]

parser = argparse.ArgumentParser(description="Generate a seed phrase of variable length.")
parser.add_argument("length", type=int, choices=lengths, metavar="length", help="Length of seed phrase to be generated. The possible lengths are 12, 15, 18, 21 or 24 words.")
parser.add_argument("-s", "--save", action="store_true", help="Save the seed phrase in a file 'seed.txt'.")
parser.add_argument("-l", "--language", choices=languages_dict.keys(), metavar="language", help=f"The language in witch to generate the seed phrase. The possible languages are: en (english), zh (chinese simplified), zh2 (chinese traditional), fr (french), it (italian), ja (japanese), ko (korean), es (spanish). The default language is en (english)", default="en")
args = parser.parse_args()

# define the strength of the seed phrase
c = 0
strength_found = False
while not strength_found:
    if args.length == lengths[c]:
        strength = strengths[c]
        strength_found = True
    c += 1

# generate the seed phrase
mnemo = Mnemonic(languages_dict[args.language])
seed_phrase = mnemo.generate(strength=strength)
seed_list = seed_phrase.split()
final_seed_list = [unidecode(word) for word in seed_list]
final_seed_phrase = " ".join(final_seed_list)

if args.save:
    # save the seed phrase in a .txt
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "seed.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(final_seed_phrase)
        print(f"The seed phrase has been saved in this current directory ({file_path})")
        print("We highly recommend to store this file in a separed and secure repository.")
else:
    # print the seed phrase
    print(f"Seed phrase (length: {args.length} words):\n{final_seed_phrase}")