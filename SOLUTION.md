## Desafio Big Data

#### Cenário

Implementação de um projeto envolvendo aquisição e análise de dados referentes à navegação
do usuário. O objetivo é montar uma ferramenta que consiga relacionar urls de vídeos e
sugerir novos vídeos a serem assistidos baseado na navegação dos demais usuários.
A estratégia para recomendação é o Filtro Colaborativo, com a aplicação de um algoritmo
de livre escolha para o cálculo de similaridade.

#### Dependências

O projeto possui as seguintes dependências:
  - [Docker](https://www.docker.com) - utilização obrigatória
  - [Docker Compose](https://docs.docker.com/compose/)
  - [Flask](https://palletsprojects.com/p/flask/)
  - [SQLite3](https://www.sqlite.org/index.html)

#### Arquitetura

Foi escolhido o micro web framework Flask, que é um escrito em Python, para construção da
API. Como trata-se de um desafio, não foi implementado nenhuma camada responsável por
atender às requisições além do próprio framework. Se fosse um sistema em produção,
provavelmente seria configurado um load balancer para atender às requisições e um número
determinado de servidores rodando Flask, capazes de aguentar as solicitações à API. Uma
outra possibilidade seria: para a action `/<url>/view`, utilizar um sistema de fila para
que um número menor de máquinas fosse utilizada. Já para a action `/<url>/similar`, temos
que responder imediatamente. Logo, um número maior de servidores ficará disponível para
atender essas requisições. Outra opção seria utilizar similaridades pré-calculadas do
dia anterior. Porém, isso acarretaria em recomendações aleatórias para URLs novas - ou seja,
que não possuem histórico algum.

Outro detalhe foi a utilização de um banco de dados relacional. Poderia ter sido utilizada
uma outra estrutura, ou mesmo um banco de dados relacional mais robusto. Visando um
desenvolvimento mais rápido, foi escolhido o banco SQLite3. Para facilitar o manuseio dos
dados, optou-se pela utilização do ORM [Peewee](http://docs.peewee-orm.com). O mesmo possui
como características: leveza, funcionalidades básicas de interação com o SGBD e fácil
configuração.

#### Dataset

Para elaboração de um dataset com histórico de visualizações de vídeos, utilizamos as
bibliotecas: [requests](https://2.python-requests.org/en/master/) e
[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#). A ideia foi
acessar a home page da Globo.com e obter todas as tags `a` existentes e seus respectivos
`href`. Foi possível identificar `~350` urls. Após, iteramos em um loop visando a
construção de um dataset com `~1k` de tamanho e `50` usuários distintos. O objetivo foi
gerar repetições de URLs, com o intuito de deixar o dataset pouco esparso.

#### Testes

Foi utilizado o framework para testes unitários
[unittest](https://docs.python.org/3/library/unittest.html), que também é escrito em Python.
Apenas os métodos do modelo `VideoHistory` foram testados. Idealmente, seria recomendado
testar as três actions (ou rotas) do controlador. Esta etapa poderia ser melhor explorada
no desafio.

#### Algoritmo de Similaridade

Para o cálculo de score foi utilizada a distância de Jaccard, conforme exemplificado no
enunciado do desafio. Outra opção que foi pensada seria a utilização da similaridade de
Cossenos. Porém, não foi possível implementar devido ao mal gerenciamento do tempo de
desenvolvimento.

Ambos os algoritmos deveriam ser mais explorados, na tentativa de obter-se melhores
resultados. O contexto deste problema tem por característica, nem que apenas por um
período inicial, um dataset esparso. Ou seja, o score da maioria dos resultados fica
próximo a zero. Um possível ponto de melhoria seria a utilização de algoritmos que
performam melhor no cenário de dados esparsos, ou a customização desses dois para
esse cenário (ex.: similaridade de cossenos com normalização dos vetores através do
coeficiente de correlação de Pearson).

#### Inicialização

Para executar o projeto, basta utilizar os comandos definidos no arquivo `Makefile`,
conforme exigido no enunciado.

```
make setup  # build das imagens docker
make run    # inicializa aplicação
make test   # executa testes unitários
```

#### Estruturação do Projeto

O arquivo `docker-compose.yml` possui dois serviços cadastrados: api e test. Dentro do
serviço api, está o banco de dados SQLite3. Caso o projeto fosse para produção, seria
interessante criar um serviço específico para a camada de dados, desacoplando a aplicação.

O arquivo `docker/Dockerfile` possui a customização do OS Alpine utilizado e explicita as
bibliotecas Python utilizadas no projeto.

O diretório `app/` é o principal do projeto. Há uma separação de responsabilidades em
arquivos python. Segue a lista de arquivos e suas responsabilidades:

- `app.py`: arquivo com configurações globais do projeto
- `main.py`: arquivo responsável por iniciar a aplicação
- `models.py`: arquivo com classes relacionadas à camada de dados
- `similarity.py`: módulo com os algoritmos de cálculo de score disponibilizados
- `tests.py`: arquivo com os testes unitários realizados
- `views.py`: controlador com o comportamento das actions (ou rotas) da API
