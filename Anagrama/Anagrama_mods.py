# -*- coding: utf-8 -*-
"""
Este script serve para testar se uma palavra é anagrama de outra.
A ideia é usar a fatorização única em primos para testar esta propriedade
Associamos a cada palavra o produto das suas letras depois de atribuidas 
os valores dos primeiros 26 números primos.
A - 2, B - 3, C - 5, D - 7, ...

Ideia tirada de https://twitter.com/fermatslibrary/status/988399621402656773
"""

from math import sqrt, floor 
import numpy as np

# =============================================================================
# FUNÇÕES MATEMÁTICAS
# =============================================================================

def prime_tester(p):
    """
    Esta função vai receber um número inteiro e testar se é primo
    Argumentos: p - inteiros
    """
    if not isinstance(p,int):
        raise TypeError('Não é inteiro')
        #Se não for um inteiro, como um float, isto não funciona.
    elif abs(p)<2:
        raise ValueError('Deve ser maior que 2')
        #Excluimos o 0 e o 1 por serem desnecessários
    else:
        p = abs(p)
        #Há primos negativos. Esta linha troca o sinal ao número
    for i in range(2,floor(sqrt(p))+1): #Percorremos os números de 2 até à raíz
        if (p % i) == 0:
            return False #Se tiver algum divisor, cai em falso
    return True

def get_primes_up_to(n):
    """
    Esta função vai recolher todos os primos até um certo limite superior
    Argumentos: 
        n - int
    Devolve:
        prime_list - list
    """
    prime_list = [i for i in range(2,n+1) if prime_tester(i)==True]
    return prime_list

def get_n_primes(n):
    """
    Esta função devolve os primeiros n primos
    Argumentos: 
        n - int
    Devolve:
        list_prime - list
    """
    if not isinstance(n, [int, np.int16, np.int32, np.int64]):
        raise TypeError("{} deve ser um inteiro".format(n))
    list_prime = [] #Começamos com a lista vazia
    prime = 2 #Primeiro primo a adicionar	
    counter = 0 #Diz-nos a quantos primos vamos
    while (counter < n): #Enquanto não temos o número de primos necessário
        if prime_tester(prime): #Se o teste de primos funcionar
            list_prime.append(prime) #Adiciona à lista criada
            counter+=1 #Progride o contador
        prime+=1 #Avançamos pelos números
    return list_prime #Recupera a lista criada

def prod(wuple):
    """
    Faz um produto dos elementos num tuplo
    Argumento: 
        wuple - tuple
    Devolve:
        p - int ou float
    """
    if not isinstance(wuple, tuple):
        raise TypeError("{} deve ser um tuplo".format(wuple))
    p = 1 #inicializamos em 1, o produto vazio
    for j in wuple:
        p *= j #Isto multiplica todos os elementos no tuplo
    return p


def assign_prime_numbered_letters(alphabet):
    """
    Cria um dicionário que atribui os valores dos primeiros n primos a n letras
    Argumentos: 
        alphabet - string
    Devolve:
        result - dict
    """
    if not isinstance(alphabet, str):
        raise TypeError("{} deve ser uma string".format(alphabet))
    n = len(alphabet)
    #Escolhemos como número de primos o comprimento do nosso alfabeto
    result = dict(zip(alphabet, get_n_primes(n)))
    #Isto cria o nosso dicionário
    return result

# =============================================================================
# ANAGRAMA
# =============================================================================

def is_anagram(string1, string2, value_letters):
    """
    Recebe 2 strings e uma atribuição de valores primos ao seu alfabeto
    Argumentos: 
        string1, string2 - string; 
        value_letters - dicionário 
    Devolve:
        True, False - bool
    """
    if len(string1) != len(string2):
        return False
    #Se o comprimento das duas strings for já diferente, não podem ser anagramas
    primes_list1 = [value_letters[x] for x in string1]
    primes_list2 = [value_letters[x] for x in string2]
    #Isto pega nas strings e cria uma lista nova com a atribuição de valores
    #Consoante o dicionário    
    if prod(primes_list1) == prod(primes_list2):
        return True
    #Isto compara ambos os produtos. 
    return False