"""
07. front_back

Considere dividir uma string em duas metades.
Caso o comprimento seja par, a metade da frente e de trás tem o mesmo tamanho.
Caso o comprimento seja impar, o caracter extra fica na metade da frente.

Exemplo: 'abcde', a metade da frente é 'abc' e a de trás é 'de'.

Finalmente, dadas duas strings a e b, retorne uma string na forma:
a-frente + b-frente + a-trás + b-trás
"""
def front_back(a, b):
    aprimeiro, asegundo, bprimeiro, bsegundo = '', '', '', ''

    if len(a) % 2 == 0:
        aprimeiro = a[:int(len(a)/2)]
        asegundo = a[int(len(a)/2):]
    else:
        aprimeiro = a[:int(len(a)/2+1)]
        asegundo = a[int(len(a)/2+1):]
    if len(b) % 2 == 0:
        bprimeiro = b[:int(len(b) / 2)]
        bsegundo = b[int(len(b) / 2):]
    else:
        bprimeiro = b[:int(len(b) / 2 + 1)]
        bsegundo = b[int(len(b) / 2 + 1):]
    return ''.join((aprimeiro,bprimeiro,asegundo,bsegundo))


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(front_back, ('abcd', 'xy'), 'abxcdy')
    test(front_back, ('abcde', 'xyz'), 'abcxydez')
    test(front_back, ('Kitten', 'Donut'), 'KitDontenut')
