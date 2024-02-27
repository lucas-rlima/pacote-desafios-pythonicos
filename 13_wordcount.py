"""
13. wordcount

Este desafio é um programa que conta palavras de um arquivo qualquer de duas
formas diferentes.

A. Lista todas as palavras por ordem alfabética indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --count letras.txt
Ele deve imprimir todas as palavras em ordem alfabética seguidas
do número de ocorrências.

Por exemplo:

$ python wordcount.py --count letras.txt
a 2
b 4
c 3

B. Lista as 20 palavras mais frequêntes indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --topcount letras.txt
Ele deve imprimir as 20 palavras mais frequêntes seguidas
do número de ocorrências, em ordem crescente de ocorrências.

Por exemplo:

$ python wordcount.py --topcount letras.txt
b 4
c 3
a 2

Abaixo já existe um esqueleto do programa para você preencher.

Você encontrará a função main() chama as funções print_words() e
print_top() de acordo com o parâmetro --count ou --topcount.

Seu trabalho é implementar as funções print_words() e depois print_top().

Dicas:
* Armazene todas as palavras em caixa baixa, assim, as palavras 'A' e 'a'
  contam como a mesma palavra.
* Use str.split() (sem parêmatros) para fazer separar as palavras.
* Não construa todo o programade uma vez. Faça por partes executando
e conferindo cada etapa do seu progresso.
"""

import sys

# +++ SUA SOLUÇÃO +++
# Defina as funções print_words(filename) e print_top(filename).
def print_words(filename):
    ref_arquivo = open(filename, "r")
    order_list = {}
    for line in ref_arquivo:
        for word in line.split():
            if word.lower() in order_list:
                contar = order_list.get(word.lower())
                contar += 1
                order_list[word.lower()] = contar
            else:
                order_list[word.lower()] = 1
    for items in sorted(order_list):
        print(items, order_list.get(items))
    ref_arquivo.close()
def print_top(filename):
    ref_arquivo = open(filename, 'r')
    full_order = {}
    for line in ref_arquivo:
        for word in line.lower().split():
            if word in full_order:
                full_order[word] = full_order.get(word)+1
            else:
                full_order[word] = 1
    for newitens in sorted(full_order, key=full_order.get, reverse=True):
        print(newitens, full_order[newitens])
    ref_arquivo.close()

# A função abaixo chama print_words() ou print_top() de acordo com os
# parêtros do programa.
def main():
    if len(sys.argv) != 3:
        print('Utilização: ./13_wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unçknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
