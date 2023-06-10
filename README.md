# Três vozes - O Jornal do Conhecimento Compartilhado

## Para rodar o projeto:

- 1. Clone o repositório

- 2. Instale as dependências python com o pip

```bash
pip install -r requirements.txt
```

- 3. Inicie o bando de dados postgres

```bash
docker compose up -d
```

- 4. Inicie o projeto

```bash
python main.py
```

### Modelo lógico do banco de dados:

![image](https://user-images.githubusercontent.com/73846881/233884996-b471d0fb-e7f3-4f4b-9962-aa3f2899328f.png)

## Deploy

Nosso projeto está hospedado no Heroku, e pode ser acessado através do link: https://tresvozesnewsapi.herokuapp.com/
