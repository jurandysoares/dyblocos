"""
ifblocos: Blocos de caracteres para animações
"""

from os import chdir
from pathlib import Path
import string
import turtle

CAM_PACOTE = Path(__file__).parent
CAM_BLOCOS = CAM_PACOTE/'blocos'/'gif'

nome_sinal_pontuacao = {
    ' ': "Espaço",
    '!': "Exclamação",
    '"': "Aspas",
    '#': "Cifrão",
    '$': "Cifrão",
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
    '\\': "Barra invertida",
    ']': "Colchete Direito",
    '^': "Circunflexo",
    '_': "Sublinhado",
    '`': "Grave",
    '{': "Chave Esquerda",
    '|': "Barra vertical",
    '}': "Chave Direita",
    '~': "Til",
}

slug_sinal_pontuacao = {
    ' ': "espaco",
    '!': "exclamacao",
    '"': "aspas",
    '#': "cerquilha",
    '$': "dolar",
    '%': "porcentagem",
    '&': "e-comercial",
    "'": "apostrofo",
    '(': "parentese-esquerdo",
    ')': "parentese-direito",
    '*': "asterisco",
    '+': "sinal-de-mais",
    ',': "virgula",
    '-': "hifen",
    '.': "ponto",
    '/': "barra",
    ':': "dois-pontos",
    ';': "ponto-e-virgula",
    '<': "menor-que",
    '=': "igual",
    '>': "maior-que",
    '?': "interrogacao",
    '@': "arroba",
    '[': "colchete-esquerdo",
    '\\': "barra-invertida",
    ']': "colchete-direito",
    '^': "circunflexo",
    '_': "sublinhado",
    '`': "grave",
    '{': "chave-esquerda",
    '|': "barra-vertical",
    '}': "chave-direita",
    '~': "til",
}

def carrega_blocos():
    for categoria in ('digitos', 'letras', 'pontuacao'):
        CAM_CATEGORIA = CAM_BLOCOS/categoria
        cwd = CAM_CATEGORIA.cwd()
        chdir(CAM_CATEGORIA)
        for digito in CAM_CATEGORIA.glob('*.gif'):
            turtle.addshape(digito.name)

        chdir(cwd)


def forma(caracter: str) -> str:
    assert len(caracter)==1
    if caracter.isdigit() or caracter.islower():
        return f'bloco-{caracter}.gif'
    elif caracter.isupper():
        return f'bloco-{caracter}{caracter}.gif'
    elif caracter in string.punctuation+' ':
        return f'bloco-{slug_sinal_pontuacao[caracter]}.gif'
    else:
        return 'turtle'
    
class Bloco(turtle.Pen):

    def __init__(self, 
                 caracter: str, 
                 pos_x: int = 0,
                 pos_y: int = 0,
                 visivel: bool = True) -> None:
        super().__init__(shape=forma(caracter), undobuffersize=1000, visible=visivel)
        self._caracter = caracter
        self.up()
        self.goto(pos_x, pos_y)

    def esquerda(self, distancia: int) -> None:
        self.setheading(180)
        self.forward(distance=distancia)

    def direita(self, distancia: int) -> None:
        self.setheading(0)
        self.forward(distance=distancia)

    def cima(self, distancia: int) -> None:
        self.setheading(90)
        self.forward(distance=distancia)

    def baixo(self, distancia: int) -> None:
        self.setheading(270)
        self.forward(distance=distancia)

    def desfaz(self):
        self.undo()

    def abaixa(self):
        self.pendown()

    def levanta(self):
        self.penup()

    def __repr__(self) -> str:
        return f'Bloco(caracter="{self._caracter}")'

turtle.title('IFBlocos: Animações com blocos de letras, dígitos e sinais de pontuação')
turtle.setup(width=800, height=600)
carrega_blocos()