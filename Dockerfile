FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

COPY wait_for_ollama.sh /wait_for_ollama.sh
RUN chmod +x /wait_for_ollama.sh

ENV PYTHONPATH=/app/src

ENTRYPOINT ["/wait_for_ollama.sh"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]