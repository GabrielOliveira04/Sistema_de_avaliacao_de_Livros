# 📚 Projeto de API para Gerenciamento de Livros

Este projeto é uma API desenvolvida com Django Ninja para gerenciar livros, categorias e avaliações. Ele permite a criação, avaliação, exclusão e sorteio de livros de maneira simples e eficiente.

🚀 Tecnologias Utilizadas

# Python 🐍

### Django & Django Ninja 🦸‍♂️

SQLite (ou outro banco de dados configurado no Django)

# 📌 Funcionalidades

## 📖 Criar livros com nome, categoria e tipo de streaming (Amazon Kindle ou Físico).

## ⭐ Avaliar livros com notas e comentários.

## ❌ Deletar livros do banco de dados.

## 🎲 Sortear um livro baseado em filtros personalizados.

## 📂 Estrutura do Projeto

# 📦 livros_api
 ┣ 📂 api
 ┃ ┣ 📜 __init__.py
 ┃ ┣ 📜 views.py  # Lógica dos endpoints
 ┃ ┣ 📜 schemas.py  # Definição dos Schemas da API
 ┃ ┣ 📜 models.py  # Modelos do banco de dados
 ┃ ┗ 📜 urls.py  # Rotas da API
 ┣ 📜 manage.py
 ┗ 📜 requirements.txt  # Dependências do projeto

# 🛠 Instalação e Configuração

# 1️⃣ Clonar o repositório

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

# 2️⃣ Criar e ativar um ambiente virtual

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows

# 3️⃣ Instalar as dependências

pip install -r requirements.txt

# 4️⃣ Rodar as migrações

python manage.py migrate

# 5️⃣ Iniciar o servidor

python manage.py runserver

# A API estará disponível em: http://127.0.0.1:8000/api/

### 🛠 Endpoints Principais

## 📌 Criar um Livro

POST /livros/

{
  "nome": "O Senhor dos Anéis",
  "streaming": "F",
  "categorias": [1, 2]
}

## 📌 Avaliar um Livro

PUT /livros/{livro_id}

{
  "comentarios": "Ótimo livro!",
  "nota": 5
}

## 📌 Deletar um Livro

DELETE /livros/{livro_id}

## 📌 Sortear um Livro

GET /livros/sortear/
