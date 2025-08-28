FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

ENV PYTHONPATH=/app/src

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]