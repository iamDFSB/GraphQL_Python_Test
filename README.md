# Projeto GraphQL com CRUD em Python

Este repositório contém um projeto simples de GraphQL desenvolvido em Python, com o objetivo de explorar e aprender os conceitos básicos do GraphQL. O projeto implementa um CRUD (Create, Read, Update, Delete) utilizando um arquivo JSON como base de dados.

## O que é GraphQL?

GraphQL é uma linguagem de consulta para APIs e um runtime para executar essas consultas com seus dados existentes. Diferentemente das APIs REST, onde você obtém dados de múltiplos endpoints, o GraphQL permite que você solicite exatamente os dados que precisa em uma única consulta.

## Funcionalidades Implementadas

* **Consultas (Queries):**
    * Recuperar todos os itens do arquivo JSON.
    * Recuperar um item específico por ID.
* **Mutações (Mutations):**
    * Criar um novo item.
    * Atualizar um item existente.
    * Deletar um item.
* **Base de Dados:**
    * Utilização de um arquivo JSON simples para armazenar os dados.

## Como Executar

1.  **Clone o repositório:**

    ```bash
    git clone [https://github.com/iamDFSB/GraphQL_Python_Test.git](https://www.google.com/search?q=https://github.com/iamDFSB/GraphQL_Python_Test.git)
    cd GraphQL_Python_Test
    ```

2.  **Instale as dependências:**

    ```bash
    pip install strawberry-graphql
    ```

3.  **Execute o servidor GraphQL:**

    ```bash
    python main.py
    ```

4.  **Acesse o GraphiQL:**

    * Abra o navegador e acesse `http://127.0.0.1:8000/graphql`.
    * O GraphiQL é uma interface interativa que permite testar suas consultas e mutações GraphQL.

## Exploração dos Métodos

* **Queries:**
    * Utilize o GraphiQL para realizar consultas e recuperar dados do arquivo JSON.
* **Mutations:**
    * Utilize o GraphiQL para criar, atualizar e deletar itens no arquivo JSON.
* **Arquivo JSON:**
    * Explore o arquivo `users.json` para entender como os dados estão estruturados e como as operações GraphQL interagem com ele.

## Contribuição

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está sob a licença [MIT](LICENSE).
