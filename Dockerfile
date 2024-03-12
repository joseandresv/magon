# Use an official NVIDIA CUDA image as a parent image
FROM nvidia/cuda:11.3.0-base-ubuntu20.04

# Set the working directory in the container
WORKDIR /usr/src/app

# Install necessary packages
RUN apt-get update && apt-get install -y \
    python3-pip \
    git \
    curl

RUN curl -fsSL https://ollama.com/install.sh | sh

# Upgrade pip
RUN pip install --upgrade pip

# Install PyTorch with CUDA support
RUN pip install llama-index qdrant_client torch transformers

COPY . .

# The command to run the application
#CMD ["python3", "./your-script.py"]
