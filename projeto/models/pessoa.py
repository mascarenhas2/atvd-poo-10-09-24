from models.endereco import Endereco
from models.enums.sexo import Sexo

class Pessoa:
    def __init__(self, id : int, nome : str, dataNascimento : str, telefone : str, email : str,
                  sexo: Sexo, endereco : Endereco) -> None:
        self.id = id
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.telefone = telefone
        self.email = email
        self.sexo = sexo
        self.endereco = endereco

    def __str__(self) -> str:
        return(
                f"\nId: {self.id}"
                f"\nNome: {self.nome}"
                f"\nData de nascimento: {self.dataNascimento}"
                f"\nTelefone: {self.telefone}"
                f"\nEmail: {self.email}"
                f"\nSexo: {self.sexo.genero} \ {self.sexo.sigla}"
                f"\nEndereco: {self.endereco}"
        )
        

