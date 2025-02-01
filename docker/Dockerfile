# Use NVIDIA CUDA base image
FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04

# Set working directory
WORKDIR /app

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    ffmpeg \
    libsm6 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
COPY config/requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Command to run when starting the container
CMD ["python3", "app.py"]