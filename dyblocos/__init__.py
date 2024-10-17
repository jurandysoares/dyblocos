"""
dyblocos: Blocos de caracteres para animações
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

    def carimba(self):
        self.stamp()

    def va_para(self, x: int, y: int):
        self.goto(x, y)

    def limpa(self):
        self.clear()

    def muda_visibilidade(self):
        self.hideturtle() if self.isvisible() else self.showturtle()

    def esconde(self):
        self.hideturtle()

    def exibe(self):
        self.showturtle()

    def __str__(self) -> str:
        return f'Bloco(caracter="{self._caracter}")'

    def __repr__(self) -> str:
        return f'Bloco(caracter="{self._caracter}")'
    
def desenha_texto(texto: str, pos_x: int = 0, pos_y: int = 0) -> None:
    for caracter in texto:
        bloco = Bloco(caracter, pos_x, pos_y)
        pos_x += 50

def desenha_texto_centralizado(texto: str, pos_y: int = 0) -> None:
    largura = 50 * len(texto)
    pos_x = -largura//2
    desenha_texto(texto, pos_x, pos_y)

def desenha_grade():
    turtle.speed('fastest')
    turtle.up()
    for i in range(-400, 450, 50):
        turtle.goto(i, 300)
        turtle.down()
        turtle.goto(i, -300)
        turtle.up()

    turtle.pensize(2)
    turtle.goto(0, -300)
    turtle.down()
    turtle.goto(0, 300)
    turtle.up()
    turtle.pensize(1)

    for i in range(-300, 350, 50):
        turtle.goto(-400, i)
        turtle.down()
        turtle.goto(400, i)
        turtle.up()

    turtle.pensize(2)
    turtle.goto(-400, 0)
    turtle.down()
    turtle.goto(400, 0)
    turtle.up()
    turtle.pensize(1)

    turtle.speed('normal')
    turtle.goto(0, 0)
    turtle.hideturtle()

tela: turtle.Screen = turtle.Screen()
tela.title('dyblocos: Animações com blocos de letras, dígitos e sinais de pontuação')
tela.setup(width=850, height=650)

carrega_blocos()