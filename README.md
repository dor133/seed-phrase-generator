# SeedPhraseGenerator
This Python script generates seed phrases of various lengths and in different languages.

This script use the library "mnemonic" (https://github.com/trezor/python-mnemonic) to generate seed phrases, which is an implementation of BIP-0039.

## Getting Started
### Prerequisites
* Python 3.x
* Libraries: mnemonic, unidecode

### Installation
* Install Python 3.x from the official website.

* Install the required libraries by running the following command in your terminal:

    ```
    python pip install -r requirements.txt
    ```

## How to use
For example, to generate a seed phrase of 12 words, run the following command in your terminal:
```
python SeedPhraseGenerator.py 12
```

## Options
It is possible to generate variable length seed, and in different languages.

Type `python SeedPhraseGenerator.py -h` to see the different options available.