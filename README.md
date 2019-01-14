# Quake 3 Parser

O Quake 3 Parser é uma aplicação escrita em Python 3.6, com o auxilio do microframework [Flask](http://flask.pocoo.org/).

A aplicação faz o parse de um log de um servidor de Quake 3 e expõe, por meio de uma API RESTful, as estatisticas de mortes de cada partida no seguinte formato:

```
    "game_1": {
        "total_kills": 4,
        "players": [
            "Dono da Bola",
            "Mocinha",
            "Isgalamido",
            "Zeh"
        ],
        "kills": {
            "Dono da Bola": -1,
            "Mocinha": 0,
            "Isgalamido": 1,
            "Zeh": -2
        }
    }
```

### Endpoints

A API possui dois endpoints:

###### GET
`/games` : retorna as estatísticas de todos os jogos

###### GET
`/games/{id}` : retorna as estatísticas de um jogo específico

### Pré-requisitos
Para rodar a aplicação é necessário ter instalado o [Python 3](https://www.python.org/downloads/) e o [pip](https://pip.pypa.io/en/stable/installing/)

Também sugere-se que se tenha o [Docker](https://docs.docker.com/install/) e o [virtualenv](https://virtualenv.pypa.io/en/latest/installation/) instalado, apesar de não ser obrigatório.


### Rodando a aplicação
Existem três possiveis maneiras de rodar a aplicação:

#### Docker
A maneira mais simples e rapida de executar a aplição é a partir do docker com o comando:

```
$ docker run -p 5000:5000 henriqueamitay/quake_parser:v2
```

Que irá baixar a imagem já upada no [Docker-hub](https://cloud.docker.com/u/henriqueamitay/repository/docker/henriqueamitay/quake_parser) e executá-la. Com isso a API poderá ser utilizada em `127.0.0.1:5000`


#### Via scripts (virtualenv)
O repositório possui dois scripts que sobem um _virtualenv_ e rodam a aplicação neste ambiente virtual. Apenas rode:

```
$ git clone git@github.com:Hamitay/quake3_parser.git
$ cd quake3_parser
$ ./setup_venv.sh
$ ./run_server.sh
```

Com isso a API poderá ser utilizada em `127.0.0.1:5000`

* **Observação**: Talvez seja necessário alterar o perssionamento destes scripts para poder executá-los.

#### Manualmente
Para rodar a aplição manualmente e no mesmo ambiente é necessário executar os seguintes passos:

1. Clonar o repositório:
```
$ git clone git@github.com:Hamitay/quake3_parser.git
$ cd quake3_parser
```

2. Instalar as dependências:
```
$ pip install -r requirements.txt
```

3. Setar as variaveis de ambiente:
```
$ EXPORT FLASK_APP=api
```
Caso queira usar algum outro arquivo de log para testar a api, pode-se alterar o caminho alterando a seguinte variável
```
$ EXPORT GAME_LOG_PATH=<caminho do .log>
```
4. Rodar a aplicação:
```
$ python -m api.server
```

Com isso a API poderá ser utilizada em `127.0.0.1:5000`

### Testes

Os testes unitários podem ser rodados facilmente com o pytest. Para executar os testes:

#### Caso tenha utilizado Docker:
```
$ docker exec -it <id do container> pytest
```

#### Caso tenha utilizado os scripts:

Garanta que o _virtualenv_ já exista e rode:
```
$ source env/bin/activate
$ pytest
```

#### Caso tenha instalado manualmente:
Apenas esteja no diretório da aplicação e rode:
```
$ pytest
```

### Discussões sobre a solução
A aplicação funciona por meio de dois pacotes:
* parser : pacote que executa o _parseamento_. Basicamente o log do servidor é aberto e suas informações são filtradas por meio de um série de expressões regulares.

* api : pacote com a API propriamente dita, desenvolvida em Flask devido à sua simplicidade. 

Uma questão interessante durante o desenvolvimento foi a necessidade de se usar cookies (ou algum tipo de cacheamento) ou algum banco de dados (ou outro tipo de permanência de informação) para que o arquivo não precise ser _parseado_ em toda requisição.

Porém, apesar desta questão, foi decidido manter o _parseamento_ em toda requisição devido a possibilidade de garantir que esta aplicação tenha uma resposta dinâmica. Poderiamos por exemplo, direcionar o output de um servidor de Quake 3 para a pasta que a aplicação acessa, com isso a API retornaria as informações do servidor em tempo real.