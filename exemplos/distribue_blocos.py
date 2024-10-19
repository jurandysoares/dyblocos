from dyblocos.blocos import carregaletras, carregadigitos, carregapontuacao
from dyblocos.nucleo import matriz, desenhagrade
desenhagrade()
letras = carregaletras()
for letra in letras:
    print(letra)
matriz
coords_matriz = matriz.keys()
coords_matriz
from string import ascii_letters
for i,letra in enumerate(ascii_letters):
    matriz[*coords_matriz[i]] = letra
for i,letra in enumerate(ascii_letters):
    matriz[**coords_matriz[i]] = letra
for i,letra in enumerate(ascii_letters):
    print(f'matriz[*{coords_matriz[i]}] = letra')
for i,letra in enumerate(ascii_letters):
    print(f'matriz[*{coords_matriz[i]}] = letra')
coords_matriz
list(coords_matriz)
coords_matriz = list(matriz.keys())
for i,letra in enumerate(ascii_letters):
    print(f'matriz[*{coords_matriz[i]}] = letra')
for i,letra in enumerate(ascii_letters):
    matriz[coords_matriz[i]] = letra
matriz
for i,letra in enumerate(ascii_letters):
    matriz[coords_matriz[i]] = letra
    letra.vapara(*coords_matriz[i])
for i,letra in enumerate(ascii_letters):
    matriz[coords_matriz[i]] = letras[letra]
    letras[letra].vapara(*coords_matriz[i])
letras
matriz
matriz[-3, -2]
matriz.index(-3, -2)
matriz.index((-3, -2))
coords_matriz.index((-3, -2))
digitos = carregadigitos()
for i,digito in enumerate(range(10)):
    matriz[coords_matriz[i+52]] = digitos[digito]
    digitos[digito].vapara(*coords_matriz[i+52])
i
i+52
coords_matriz[61]
coords_matriz[60]
matriz[60]
coords_matriz[60]
matriz[coords_matriz[60]]
matriz[coords_matriz[61]]
pontuacao = carregapontuacao()
#for i,pontuacao in enumerate():
#    matriz[coords_matriz[i+52]] = digitos[digito]
#    digitos[digito].vapara(*coords_matriz[i+52])
from dyblocos.nucleo import nome_sinal_pontuacao
for i,sinal in enumerate(nome_sinal_pontuacao.keys()):
    matriz[coords_matriz[i+62]] = pontuacao[sinal]
    pontuacao[sinal].vapara(*coords_matriz[i+62])
import turtle
turtle.done()
%hist
%hist -f exemplos/distribue_blocos.py
