from enum import Enum

class Sexo(Enum):
    MASCULINO = ("Masculino",'M')
    FEMININO = ("Feminino",'F')

    def __init__(self, genero : str, sigla : str) -> None:
        self.genero = genero
        self.sigla = sigla
        
