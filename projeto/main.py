import os 
from models.enums.unidadeFederativa import Unidadefederativa
from models.enums.sexo import Sexo
from models.endereco import Endereco
from models.pessoa import Pessoa

os.system("cls || clear")

pessoa = Pessoa(4002,"Karol","05/08/2008","18991997","karol@braba.com",Sexo.MASCULINO,
                Endereco("Travessa bucui","59","Frente ao bar","54221","Salvador",Unidadefederativa.BAHIA))

print(pessoa)