import pytest 

from ..models.pessoa import Pessoa
from ..models.endereco import Endereco
from ..models.enums.sexo import Sexo
from ..models.enums.unidadeFederativa import Unidadefederativa

@pytest.fixture
def criar_pessoa():
    pessoa_1 = Pessoa(4002,"Karol","05/08/2008","18991997","karol@braba.com",Sexo.MASCULINO,
                Endereco("Travessa bucui","59","Frente ao bar","54221","Salvador",Unidadefederativa.BAHIA))
    
    return pessoa_1

def test_pessoa_valido_nome(criar_pessoa):
    assert criar_pessoa.nome == "Marta"
    
def test_pessoa_atributo_idade(criar_pessoa):
    assert criar_pessoa.idade == 22

