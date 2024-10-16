#!/usr/bin/env python3

from string import \
    ascii_lowercase as letras_minusculas, \
    ascii_uppercase as letras_maiusculas

from slugify import slugify

nome_sinal_pontuacao = {
    ' ': "Espaço",
    '!': "Exclamação",
    r'\"': "Aspas",
    '#': "Cerquilha",
    '$': "Dólar",
    '%': "Porcentagem",
    '&': "E comercial",
    "'": "Apóstrofo",
    '(': "Parêntese Esquerdo",
    ')': "Parêntese Direito",
    '*': "Asterisco",
    '+': "Sinal de mais",
    ',': "Vírgula",
    '-': "Hífen",
    '.': "Ponto",
    '/': "Barra",
    ':': "Dois Pontos",
    ';': "Ponto e Vírgula",
    '<': "Menor que",
    '=': "Igual",
    '>': "Maior que",
    '?': "Interrogação",
    '@': "Arroba",
    '[': "Colchete Esquerdo",
    r'\\': "Barra invertida",
    ']': "Colchete Direito",
    '^': "Circunflexo",
    '_': "Sublinhado",
    '`': "Grave",
    '{': "Chave Esquerda",
    '|': "Barra vertical",
    '}': "Chave Direita",
    '~': "Til",
}

BLOCO_MODELO = '''\
graph bloco {{
    no[label="{texto}",shape={forma}];
}}
'''

def gera_bloco(texto: str, forma: str) -> str:    
    return BLOCO_MODELO.format(texto=texto, forma=forma)

def main():
    print('Gerando os dígitos...')
    for digito in "0123456789":
        conteudo = gera_bloco(digito, "square")
        with open(f'bloco-{digito}.dot', mode='w', encoding='utf-8') as arq_dot:
            arq_dot.write(conteudo)
    print('Todos os dígitos foram gerados.')

    print('Gerando os letras minúsculas...')
    for letra in letras_minusculas:
        conteudo = gera_bloco(letra, "square")
        with open(f'bloco-{letra}.dot', mode='w', encoding='utf-8') as arq_dot:
            arq_dot.write(conteudo)
    print('Todas as letras minúsculas foram geradas.')

    print('Gerando os letras maiúsculas...')
    for letra in letras_maiusculas:
        conteudo = gera_bloco(letra, "square")
        with open(f'bloco-{letra}{letra}.dot', mode='w', encoding='utf-8') as arq_dot:
            arq_dot.write(conteudo)
    print('Todas as letras maiúsculas foram geradas.')

    print('Gerando sinais de pontuação e espaço...')
    for sinal,nome_sinal in nome_sinal_pontuacao.items():
        conteudo = gera_bloco(sinal, "square")
        with open(f'bloco-{slugify(nome_sinal)}.dot', mode='w', encoding='utf-8') as arq_dot:
            arq_dot.write(conteudo)
    print('Todos os sinais de pontuação e espaço foram gerados.')

if __name__ == '__main__':
    main()

