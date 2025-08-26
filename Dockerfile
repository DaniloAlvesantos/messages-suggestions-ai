# Use official Python base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Ollama CLI
RUN curl -L https://ollama.com/download/ollama-linux.zip -o ollama.zip \
    && unzip ollama.zip -d /usr/local/bin \
    && rm ollama.zip \
    && chmod +x /usr/local/bin/ollama

# Copy Python requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your API code (if any)
COPY . .

# Expose port for Ollama API (default is 11434)
EXPOSE 11434

# Start Ollama model server
# Replace 'your-model' with the Ollama model you want to run
CMD ["ollama", "serve", "your-model", "--port", "11434"]
