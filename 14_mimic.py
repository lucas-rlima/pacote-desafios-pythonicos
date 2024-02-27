"""
Leia o arquivo especificado via linha de comando.
Faça um split() no espaço em branco para obter todas as palavras
no arquivo, em vez de ler o arquivo linha a linha, é mais facil obter
uma string gigante e fazer o split uma vez.

Crie um dicionario "imitador" que mapeia cada palavra que aparece no arquivo
com a lista de todas as palavras que seguem imediatamente essa palavra no
arquivo. A lista de palavras pode estar em qualquer ordem, e deve incluir
duplicatas. Por exemplo, a chave 'and' pode ter a listagem
["then","best","then","after", ...] listando todas as palavras que 
vieram depois de 'and' no texto de entrada. Diremos que a string vazia 
é o que vem antes a primeira palavra no arquivo.

Com o dicionario imitador é bastante simples emitir aleatoriamente texto
que imita o original. Imprima uma palavra, depois veja quais palavras podem
vir a seguir e pegue uma aleatoriamente como a proxima palavra do texto.
Use a string vazia como a primeira palavra do texto para preparar as coisas.
Se caso ficar preso em uma palavra que não está no dicionario, apenas volte
para a string vazia para manter as coisas em movimento.

PS: o módulo padrão do python 'random' conta com o
random.choice(list), método que escolhe um elemento aleatório de uma lista
não vazia.
"""

import random
import sys
from collections import defaultdict
from random import choice


def mimic_dict(filename):
    """Retorna o dicionario imitador mapeando cada palavra para a lista de
  palavras subsequentes."""
    # +++ SUA SOLUÇÃO +++
    ref_arquivo = open(filename, 'r')
    arquivo_open = ref_arquivo.read().lower().split()
    mimic = defaultdict(list)
    for index, word in enumerate(arquivo_open):
        try:
            if not mimic:
                mimic[''].append(arquivo_open[index + 1])
            if arquivo_open[index + 1] not in mimic[word]:
                mimic[word].append(arquivo_open[index + 1])
            else:
                pass
        except:
            mimic[word].append('')
    return mimic


def print_mimic(mimic_dict, word):
    """Dado o dicionario imitador e a palavra inicial, imprime texto de 200 palavras."""
    text = ''
    newword = ''
    while len(text) <= 200:
        newword = (choice(mimic_dict[word]))
        text += " " + newword
        word = newword

    return text

# Chama mimic_dict() e print_mimic()
def main():
    if len(sys.argv) != 2:
        print('Utilização: ./14_mimic.py file-to-read')
        sys.exit(1)

    dict = mimic_dict(sys.argv[1])
    print_mimic(dict, '')


if __name__ == '__main__':
    main()
