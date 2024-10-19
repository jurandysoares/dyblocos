"""
dyblocos: Blocos de caracteres para animações
"""

from os import chdir
from pathlib import Path
import string
import turtle

CAM_PACOTE = Path(__file__).parent
CAM_BLOCOS = CAM_PACOTE/'blocos'/'gif'
LADO_QUADRADO = 50
TELA_LARGURA = 16
TELA_ALTURA = 12

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

def adicionaformas(categorias: tuple = ('digitos', 'letras', 'pontuacao')) -> None:
    for categ in categorias:
        CAM_CATEGORIA = CAM_BLOCOS/categ
        cwd = CAM_CATEGORIA.cwd()
        chdir(CAM_CATEGORIA)
        for arq_gif in CAM_CATEGORIA.glob('*.gif'):
            turtle.addshape(arq_gif.name)

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
    _qt_blocos: int = 0
    def __init__(self, 
                 caracter: str, 
                 pos_x: int = 0,
                 pos_y: int = 0,
                 visivel: bool = True) -> None:

        Bloco._qt_blocos += 1
        self.id = Bloco._qt_blocos
        super().__init__(shape=forma(caracter), undobuffersize=1000, visible=visivel)
        self._caracter = caracter
        self.up()
        self.goto(pos_x, pos_y)
        

    def esquerda(self, distancia: int = 1) -> None:
        self.setheading(180)
        self.forward(distance=distancia*LADO_QUADRADO)

    def direita(self, distancia: int = 1) -> None:
        self.setheading(0)
        self.forward(distance=distancia*LADO_QUADRADO)

    def cima(self, distancia: int = 1) -> None:
        self.setheading(90)
        self.forward(distance=distancia*LADO_QUADRADO)

    def baixo(self, distancia: int = 1) -> None:
        self.setheading(270)
        self.forward(distance=distancia*LADO_QUADRADO)

    def desfaz(self):
        self.undo()

    def abaixa(self):
        self.pendown()

    def levanta(self):
        self.penup()

    def carimba(self):
        self.stamp()

    def limpa(self):
        self.clear()

    def muda_visibilidade(self):
        self.hideturtle() if self.isvisible() else self.showturtle()

    def esconde(self):
        self.hideturtle()

    def exibe(self):
        self.showturtle()

    def posicao(self):
        pos_x, pos_y = self.position()
        quad_x = 1+int(pos_x)//LADO_QUADRADO if int(pos_x)>=0 else int(pos_x)//LADO_QUADRADO
        quad_y = 1+int(pos_y)//LADO_QUADRADO if int(pos_y)>=0 else int(pos_y)//LADO_QUADRADO
        return quad_x, quad_y

    def vapara(self, x: int, y: int):
        assert x!=0 or y!=0, f'O bloco "{self._caracter}" não pode ir para  (0, 0)'
        pos_x = (x-1)*LADO_QUADRADO if x>=0 else x*LADO_QUADRADO
        pos_y = (y-1)*LADO_QUADRADO if y>=0 else y*LADO_QUADRADO
        self.goto(pos_x, pos_y)

    def casa(self):
        self.home()

    def __str__(self) -> str:
        return f'Bloco(caracter="{self._caracter}")'

    def __repr__(self) -> str:
        return f'Bloco(caracter="{self._caracter}")'

matriz: dict[(int, int), Bloco] = dict()
for i in range(1, (TELA_LARGURA//2)+1):
    for j in range(1, (TELA_ALTURA//2)+1):
        for sinal_i in [-1, +1]:
            for sinal_j in [-1, +1]:    
                matriz[(i*sinal_i, j*sinal_j)] = None
        

def desenha_texto(texto: str, pos_x: int = 0, pos_y: int = 0) -> None:
    for caracter in texto:
        bloco = Bloco(caracter, pos_x, pos_y)
        pos_x += 50

def desenha_texto_centralizado(texto: str, pos_y: int = 0) -> None:
    largura = 50 * len(texto)
    pos_x = -largura//2
    desenha_texto(texto, pos_x, pos_y)

def desenhagrade(dx: int = -25, dy: int = -25):
    turtle.speed('fastest')
    turtle.up()
    for i in range(-400+dx, 450+dx, 50):
        turtle.goto(i, 300+dy)
        turtle.down()
        turtle.goto(i, -300+dy)
        turtle.up()

    turtle.pensize(2)
    turtle.goto(0+dx, -300+dy)
    turtle.down()
    turtle.goto(0+dx, 300+dy)
    turtle.up()
    turtle.pensize(1)

    for i in range(-300+dy, 350+dy, 50):
        turtle.goto(-400+dx, i)
        turtle.down()
        turtle.goto(400+dx, i)
        turtle.up()

    turtle.pensize(2)
    turtle.goto(-400+dx, 0+dy)
    turtle.down()
    turtle.goto(400+dx, 0+dy)
    turtle.up()
    turtle.pensize(1)

    turtle.speed('normal')
    turtle.goto(0, 0)
    turtle.hideturtle()    

# carrega_blocos()
# desenha_grade()
