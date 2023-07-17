from constants import LENGTH_STRENGTH, LANGUAGES

from mnemonic import Mnemonic
from unidecode import unidecode


def strength(length: int) -> int:
    strength = LENGTH_STRENGTH[length]
    return strength


def generate_seed(strength: int, lang: str) -> str:
    mnemo = Mnemonic(LANGUAGES[lang])

    seed_phrase = mnemo.generate(strength=strength)
    seed_list = seed_phrase.split()
    final_seed_list = [unidecode(word) for word in seed_list]
    final_seed_phrase = " ".join(final_seed_list)

    return final_seed_phrase
