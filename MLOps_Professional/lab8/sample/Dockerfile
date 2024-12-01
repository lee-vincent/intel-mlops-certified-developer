FROM public.ecr.aws/docker/library/python:3.9

# Copy assets over to the image
COPY . /pickerbot

# Set the working directory
WORKDIR /pickerbot

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3-dev \
    python3-pip \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set PATH environment variable
ENV PATH="/root/.local/bin:$PATH"

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt && pip3 install sentence-transformers

# Expose the endpoint port
EXPOSE 5000

# Specify the entry point
ENTRYPOINT ["python", "serve.py"]
