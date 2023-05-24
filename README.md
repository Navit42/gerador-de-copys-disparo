# gerador-de-copys-disparo
Este programa se dedica a automatizar o processo de geração de copys para disparos em massa.

Modo de uso:

na pasta ENTRADA, você encontra um arquivo de texto onde deve colocar as seguintes informações: nome da cidade, o local do evento, o endereço do local, ponto de referência e por fima data no formato dia/mes.

* Os valores devem ser separados por ";" (ponto e virgula")
* as linhas com informação devem ser separada por "&" ("E" comercial)

na pasta COPYS, voce encontra 4 arquivos de texto. cada um contendo uma copy.
os valores a serem substituidos devem seguir o padrão de nomenclatura a seguir:

cidade = {city}
endereço = {adress}
local = {place}
ponto de referencia = {landmark}
data = {date}

seguindo esses passos você conseguirá executar o arquivo "EXECUTAVEL.bat" que vai gerar as copys e guarda-las na pasta SAIDA/{city}.
