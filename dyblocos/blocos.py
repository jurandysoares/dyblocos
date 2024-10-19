from string import ascii_letters, digits
from .nucleo import adicionaformas, Bloco, slug_sinal_pontuacao

sinal_slug = {slug: sinal for sinal,slug in slug_sinal_pontuacao.items()}

class Pontuacao:
    def __init__(self):
        self._blocos = {}

    def __getitem__(self, sinal: str) -> Bloco:
        print(sinal)
        return self._blocos[sinal]
    
    def __getattr__(self, snake_sinal: str) -> Bloco:
        slug_sinal = snake_sinal.replace('_', '-')
        sinal = sinal_slug[slug_sinal]
        if sinal in self._blocos:
            return self._blocos[sinal]
        else:
            raise AttributeError(f'O bloco para o sinal de pontuação descrito como "{snake_sinal}" não foi encontrado.')
        
    def __setitem__(self, sinal: str, bloco: Bloco) -> None:
        self._blocos[sinal] = bloco

class Digitos:
    def __init__(self):
        self._blocos = {}

    def __getitem__(self, digito: int) -> Bloco:
        return self._blocos[digito]
    
    def __getattr__(self, d_digito: str) -> Bloco:
        digito: int = int(d_digito[-1])
        if digito in self._blocos:
            return self._blocos[digito]
        else:
            raise AttributeError(f'O bloco para o dígito "{digito}" não foi encontrado.')
    
    def __setitem__(self, digito: int, bloco: Bloco) -> Bloco:
        self._blocos[digito] = bloco
        return self._blocos[digito]

class Letras:
    def __init__(self):
        self._blocos = {}

    def __getitem__(self, letra: str) -> Bloco:
        return self._blocos[letra]
    
    def __getattr__(self, letra: str) -> Bloco:
        if letra in self._blocos:
            return self._blocos[letra]
        else:
            raise AttributeError(f'O bloco para a letra "{letra}" não foi encontrado.')
    
    def __setitem__(self, letra: str, bloco: Bloco) -> None:
        self._blocos[letra] = bloco


def carregadigitos(visibilidade: bool = True) -> Digitos:
    adicionaformas(('digitos',))
    digitos = Digitos()
    for digito in digits:
        digitos[int(digito)] = Bloco(digito, visivel=visibilidade)

    return digitos

def carregaletras(visibilidade: bool = True) -> Letras:
    adicionaformas(('letras',))
    letras = Letras()
    for letra in ascii_letters:
        letras[letra] = Bloco(letra, visivel=visibilidade)

    return letras


def carregapontuacao(visibilidade: bool = True) -> Pontuacao:
    adicionaformas(('pontuacao',))
    pontuacao = Pontuacao()
    for sinal in slug_sinal_pontuacao:
        pontuacao[sinal] = Bloco(sinal, visivel=visibilidade)

    return pontuacao
    