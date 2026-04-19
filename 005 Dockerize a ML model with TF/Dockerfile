FROM python:3.12-slim

WORKDIR /app
# install tensoflow
RUN pip install --no-cache-dir tensorflow==2.16.1
COPY . .

CMD ["python", "model.py"]