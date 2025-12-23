FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY __init__.py .
COPY tests ./tests
COPY elasticsearch_client.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "-m", "pytest", "-v"]