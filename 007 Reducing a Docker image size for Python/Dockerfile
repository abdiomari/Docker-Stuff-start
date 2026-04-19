# MultiStage build 

#  Stage 1

FROM python:3.12-slim AS builder
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY script.py .

# Stage 2
FROM python:3.12-slim

WORKDIR /app

# Copy only the installed Python packages and script from builder
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /app/script.py .

RUN useradd -m -u 1001 appuser && chown -R appuser:appuser /app
USER appuser

VOLUME /app/data

CMD ["python", "script.py"]