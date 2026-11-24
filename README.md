# API de Chamados de Suporte

**Aluno:** JOSE IVAN SIMAO DA SILVA  
**Atividade:** 01 – Primeira API com Flask

## Sobre o projeto

Este projeto foi desenvolvido como parte da atividade individual de introdução ao Flask. O objetivo é criar a estrutura inicial de uma API para chamados de suporte, utilizando Python e a ferramenta uv para gerenciar as dependências.

Nesta primeira etapa, foi criada uma rota inicial para verificar se a API está funcionando corretamente.

## Tecnologias utilizadas

- Python
- Flask
- uv
- Git
- GitHub
- GitHub Codespaces

## Estrutura do projeto

O projeto está organizado da seguinte forma:

```text
chamados-ads/
├── src/
│   └── chamados_ads/
│       └── __init__.py
├── .gitignore
├── .python-version
├── app.py
├── LICENSE
├── pyproject.toml
├── README.md
└── uv.lock
```

## Instalação das dependências

Com o projeto aberto no terminal, execute o comando:

```bash
uv sync --locked
```

Esse comando instala as dependências necessárias para executar a aplicação, utilizando as versões definidas no arquivo `uv.lock`.

## Como executar a aplicação

Para iniciar o servidor Flask no GitHub Codespaces, utilize:

```bash
uv run flask --app app run --host=0.0.0.0 --port=5000
```

Após iniciar o servidor, a aplicação estará disponível na porta 5000.

## Rota inicial

A API possui uma rota inicial com as seguintes características:

- **Método:** GET
- **Caminho:** /
- **Resposta HTTP:** 200 OK
- **Formato:** JSON

Para acessar, utilize:

http://localhost:5000/

A resposta esperada é:

```json
{
  "mensagem": "API de chamados em funcionamento"
}
```

## Teste da API

Para verificar o funcionamento pelo terminal, utilize:

```bash
curl -i http://localhost:5000/
```

A resposta deve apresentar o status HTTP 200, o cabeçalho `Content-Type: application/json` e a mensagem definida na rota inicial.

## Conclusão

Com esta atividade, foi possível colocar em prática os primeiros passos para desenvolver uma API utilizando Flask, configurar o ambiente com uv e testar uma requisição HTTP.

Esta é a estrutura inicial do projeto de chamados de suporte, que poderá receber novas funcionalidades nas próximas etapas.