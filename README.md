# Seed Phrase Generator
This Python script generates seed phrases of various lengths and in different languages.

This script use the library "mnemonic" (https://github.com/trezor/python-mnemonic) to generate seed phrases, which is an implementation of BIP-0039.

## Getting Started
### Prerequisites
* Python 3.x
* Libraries: mnemonic, unidecode

### Installation
* Install Python 3.x from the official website.

* Clone this repository where you want it:
    ```
    cd <YOUR_PATH>
    git clone https://github.com/dor133/seed-phrase-generator
    ```

* Install the required libraries by running the following command in your terminal:

    ```
    python pip install -r requirements.txt
    ```

## How to use
For example, to generate a seed phrase of 12 words, run the following command in your terminal:
```
python seedphrase 12
```
By default, it will print the seed in your terminal.

## Options
It is possible to generate variable length seed, and in different languages.

It is also possible to save the seed phrase in a .txt file.

Type `python seedphrase -h` to see the different options available.