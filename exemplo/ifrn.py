import dyblocos

I = dyblocos.bloco('I')
F = dyblocos.Bloco('F')
R = dyblocos.Bloco('R')
N = dyblocos.Bloco('N')

I.esquerda(100)
F.esquerda(50)
R.direita(50)
N.direita(100)

exit()
