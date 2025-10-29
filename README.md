# 🦄 My Little Pony API

Bem-vindo à **My Little Pony API**!  
Este projeto é uma API RESTful desenvolvida em **FastAPI**, integrada a um **banco de dados MySQL via XAMPP**, e permite realizar **operações CRUD** (Create, Read, Update e Delete) com personagens do universo *My Little Pony*.

## 🚀 Tecnologias utilizadas

- **[FastAPI](https://fastapi.tiangolo.com/)** — framework moderno e rápido para APIs Python  
- **SQLAlchemy (Async)** — ORM para manipulação do banco de dados  
- **MySQL** (via **XAMPP**) — sistema de gerenciamento de banco de dados  
- **Uvicorn** — servidor ASGI para rodar a aplicação  
- **Pydantic** — validação e serialização de dados

## ⚙️ Funcionalidades

- 🐴 **Criar** um novo personagem (`POST /mlp`)
- 📜 **Listar** todos os personagens (`GET /mlp`)
- 🔍 **Buscar** um personagem por ID (`GET /mlp/{id}`)
- ✏️ **Atualizar** informações de um personagem (`PUT /mlp/{id}`)
- ❌ **Excluir** um personagem (`DELETE /mlp/{id}`)

## 🗂️ Estrutura do projeto
```bash
API-MY-LITTLE-PONY/
├── api/
│ └── v1/
│ ├── endpoints/
│ │ ├── api.py
│ │ └── mlp.py
│ ├── core/
│ │ ├── configs.py
│ │ ├── database.py
│ │ └── deps.py
│ ├── models/
│ │ ├── all_models.py
│ │ └── mlp_models.py
│ └── schemas/
│ └── mlp_schemas.py
│
├── front/
│ ├── index.html
│ └── script.js
│
├── criar_tabelas.py
├── main.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```
---

## 💾 Configuração do Banco de Dados (XAMPP / MySQL)

- Inicie o XAMPP e ative o MySQL.
- Acesse o phpMyAdmin (http://localhost/phpmyadmin).
  
- Crie um banco de dados, por exemplo:
CREATE DATABASE my_little_pony;

- Configure sua conexão no arquivo database.py:
DATABASE_URL = "mysql+aiomysql://root:@localhost/my_little_pony"


(Ajuste usuário e senha conforme sua instalação do MySQL.)

## ▶️ Como executar o projeto

### 1. Clonar o repositório
- git clone https://github.com/seuusuario/my-little-pony-api.git
cd my-little-pony-api

### 2. Criar e ativar o ambiente virtual
- python -m venv venv
- venv\Scripts\activate   # Windows
- source venv/bin/activate  # Linux/Mac

### 3. Instalar dependências
- pip install -r requirements.txt

### 4. Rodar a API
- uvicorn app.main:app --reload

### A API ficará disponível em:
- 👉 http://127.0.0.1:8000

## 📘 Documentação automática

O FastAPI gera documentação interativa automaticamente:

- Swagger UI: http://127.0.0.1:8000/docs
- Redoc: http://127.0.0.1:8000/redoc

## 🧪 Exemplo de requisição (POST)

- POST /mlp
```bash
{
  "nome": "Twilight Sparkle",
  "cor": "Roxo",
  "elemento": "Magia"
}
```

- Resposta (201 Created):
```bash
{
  "id": 1,
  "nome": "Twilight Sparkle",
  "cor": "Roxo",
  "elemento": "Magia"
}
```
## ❤️ Créditos
- Criado com amor e magia por Akira Sunsets✨
- Projeto inspirado em My Little Pony: Friendship is Magic.
