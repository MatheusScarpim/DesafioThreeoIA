#!/bin/sh
# Aguarda o Ollama responder na porta 11434
until curl -sf http://ollama:11434/api/tags | grep '"name":"llama3:8b"' ; do
  echo "Aguardando o modelo llama3:8b ser baixado pelo Ollama..."
  sleep 5
done
echo "Ollama e modelo prontos!"
exec "$@"