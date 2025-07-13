FROM python:3.12-slim

WORKDIR /api

COPY requirements.txt .

RUN apt update \
 && apt install -y --no-install-recommends netcat-openbsd \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

# Copia el script de espera y da permisos de ejecución
COPY wait-for-db.sh /wait-for-db.sh
RUN chmod +x /wait-for-db.sh


COPY . .


EXPOSE 8000

CMD ["/wait-for-db.sh", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
