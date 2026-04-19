FROM python:3.12-slim

WORKDIR /app

# Install PyTorch and torchvision for a Linux container runtime.
RUN pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Copy requirements and install extra packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the model script
COPY model.py .

CMD ["python", "model.py"]
