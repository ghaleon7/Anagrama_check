# -*- coding: utf-8 -*-

# =============================================================================
# IMPORTS
# =============================================================================

import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from Anagrama_mods import is_anagram, assign_prime_numbered_letters
from string import ascii_lowercase

# =============================================================================
# TRATAMENTO DAS PALAVRAS
# =============================================================================

lang = input("""Que lingua estamos a estudar?\n
             1. pt \n
             2. eng \n
             3. esp \n
             4. cat \n  
             -- Resposta: """)

## CONVERSÃO DO ALFABETO DAS PALAVRAS
replace_vowel_dct = {}
replace_consonant_dct = {}

if lang == 'pt':
    replace_vowel_dct = {'a': ['à', 'á', 'ã', 'â'],
                         'e': ['é', 'ê'],
                         'i': ['í'],
                         'o': ['ô', 'õ', 'ó'],
                         'u': ['ú']}
    replace_consonant_dct = {'c':['ç']}
elif lang == 'esp':
    replace_vowel_dct = {'a': ['á'],
                         'e': ['é'],
                         'i': ['í'],
                         'o': ['ó'],
                         'u': ['ú']}
    replace_consonant_dct = {'n':['ñ']}
elif lang == 'cat':
    replace_vowel_dct = {'a': ['à'],
                         'e': ['é', 'è'],
                         'i': ['í', 'ï'],
                         'o': ['ò', 'ó'],
                         'u': ['ú', 'ü']}
    replace_consonant_dct = {'c':['ç']}
else:
    if lang!='eng':
        raise Exception("The script is not ready for this language")


## PRIMEIRA CONVERSÃO: REMOÇÃO DE MAIUSCULAS

word_1 = input('Escreva a primeira palavra: \n')
word1 = word_1.lower()
word_2 = input('Escreva a segunda palavra: \n')
word2 = word_2.lower()

## SEGUNDA CONVERSÃO: REMOÇÃO DE ESPAÇOS 

word1 = word1.replace(' ', '')
word2 = word2.replace(' ', '')

## TERCEIRA CONVERSÃO: TRATAMENTO DO PUNT VOLAT
if lang == 'cat':
    word1 = word1.replace('·', '')
    word2 = word2.replace('·', '')
 
## QUARTA CONVERSÃO: TRATAMENTO DOS CARACTERES A SUBSTITUIR  

replace_lst = []
for vowel in replace_vowel_dct.keys():
    for char in replace_vowel_dct[vowel]:
        replace_lst.append(tuple([char, vowel]))
        
for consonant in replace_consonant_dct.keys():
    for char in replace_consonant_dct[consonant]:
        replace_lst.append(tuple([char, consonant]))
        
for pair in replace_lst:
    word1 = word1.replace(*pair)
    word2 = word2.replace(*pair)
        
alfabeto = ascii_lowercase
val_atri = assign_prime_numbered_letters(alfabeto)

# =============================================================================
# Check
# =============================================================================

if is_anagram(word1, word2, val_atri):
    print('"{}" é anagrama de "{}".'.format(word_1, word_2))
else:
    print('"{}" e "{}" não são anagramas.'.format(word_1, word_2))