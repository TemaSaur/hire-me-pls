FROM python:3.12-slim AS base

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml .
COPY poetry.lock .

RUN poetry install

COPY . .

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "main:app", "--port", "8000", "--host", "0.0.0.0"]
