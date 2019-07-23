## Joao Pedro Pinheiro
Desafio Big Data
================

## Considerações Gerais

Sua solução deve ser simples de ser executada, seguindo as condições abaixo:

* Seu sistema deve estar encapsulado em container(s) Docker;
* Registre no arquivo SOLUTION.md a arquitetura do projeto e as ideias que gostaria de implementar se tivesse mais tempo e explique como você as faria.


## O Problema

O seu desafio consiste em recomendar documentos similares a um outro no estilo ["quem viu isso, também viu..."](https://en.wikipedia.org/wiki/Collaborative_filtering).

>Exemplo: se o usuário **A** viu os documentos 1, 2 e 3; o **B** viu 1, 2 e 5; e o **C** viu 1, 2 e 4, a API deve dizer que o documento 1 é similar ao 2.

A escolha do algoritmo de similaridade é livre (ex: distância de Jaccard) e é permitido o uso de uma biblioteca já existente para isso.

## A API

Você deve criar uma API HTTP com as seguintes interfaces:

### POST `/<url>/view`:

  Esse interface será chamada cada vez que um usuário ver um documento. Recebe o parâmetro `user` no **body** do request.

  >Exemplo de uso: `$ curl -d "user=user1" http://localhost:8080/www.globoplay.com/v/1234567/view/`

### GET `/<url>/similar`:

Essa interface deve retornar no formato json uma lista com os dez documentos mais similares em ordem decrescente.

>Exemplo de uso: `$ curl http://localhost:8080/g1.globo.com/monitor-da-violencia/noticia/2019/03/08/cai-o-no-de-mulheres-vitimas-de-homicidio-mas-registros-de-feminicidio-crescem-no-brasil.ghtml/similar/`

Exemplo de retorno:
```json
    [{
        "url": "g1.globo.com/educacao/enem/noticia/2019/04/02/inep-diz-que-enem-2019-nao-sofrera-alteracao-apos-grafica-declarar-falencia.ghtml",
        "score": 0.9
     }, {
        "url": "www.globoplay.com/v/12758494",
        "score": 0.85
    }, {
        "url": "g1.globo.com/pop-arte/musica/blog/mauro-ferreira/post/2019/04/02/los-hermanos-experimenta-leveza-na-primeira-musica-inedita-da-banda-em-14-anos.ghtml",
        "score": 0.8
    },{
        "url": "globoesporte.globo.com/blogs/blog-do-rodrigo-capelo/post/2019/04/02/o-flamengo-nao-investiu-mais-de-r-100-milhoes-em-jogadores-por-acaso-eis-os-numeros-de-2018.ghtml",
        "score": 0.5
    }]
```

### DELETE `/`:

Remove todos os dados da base.

>Exemplo de uso: `$ curl -X "DELETE" http://localhost:8080/`

**Será eliminatório se a aplicação não respeitar os contratos a cima.**

## Requisitos

### Inicialização

Devemos ser capazes de rodar sua aplicação e iniciar o serviço com os seguintes passos
```
make setup  # build da(s) imagem(ns) docker
make run    # inicializa aplicação
```

Devemos ser capazes de rodar os testes com o comando
```
make test
```

**Será eliminatório se a aplicação não funcionar com os comandos a cima.**

## Avaliação

1. Você deverá entregar seu código e uma documentação **SOLUTION.md**.

2. A aplicação **precisa** executar em container(s) **Docker**, respeitar os contratos de API e os comandos de inicialização descritos aqui.

3. Seu código e documentação serão observados por uma equipe de desenvolvedores que avaliará a simplicidade e clareza da solução, arquitetura, estilo de código, testes unitários, nível de automação dos testes, implementação do código, e a organização geral projeto.


### Dicas

- Use ferramentas e bibliotecas open-source (desde que não façam todo o trabalho para você);
- Documente as decisões e porquês;
- Automatize o máximo possível;
- Em caso de dúvidas, pergunte.
