# Estágio 1: Build (Instalação de dependências)
FROM python:3.12-slim AS builder

WORKDIR /app

# Copia apenas o que é necessário para instalar as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Estágio 2: Runtime (Imagem final leve e segura)
FROM python:3.12-slim

WORKDIR /app

# Copia as bibliotecas instaladas do estágio anterior
COPY --from=builder /install /usr/local

# Copia o código e o modelo
COPY src/ ./src/
COPY src/models/ ./models/

# Variável de ambiente para o Python encontrar o módulo src
ENV PYTHONPATH=.

# Criar um usuário não-root por segurança (Boa prática de DevSecOps!)
RUN useradd -m mluser
USER mluser

# Expondo a porta da API
EXPOSE 8000

# Comando para rodar a API
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]