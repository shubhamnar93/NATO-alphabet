import pandas as pd

alpha=pd.read_csv('nato_phonetic_alphabet.csv')
m={value.letter:value.code for (key, value) in alpha.iterrows()}


def generate_phonetic():
    i= input('write what do you want to translate: ').upper()
    try:
        d=[m[letter] for letter in i]
    except KeyError:
        print('sorry, only letters in alphabet')
        generate_phonetic()
    else:
        print(d)

generate_phonetic()