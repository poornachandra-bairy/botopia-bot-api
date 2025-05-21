FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    mongodb \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run MongoDB and the FastAPI app
CMD ["bash", "-c", "mongod --fork --logpath /var/log/mongodb.log && uvicorn main:app --host 0.0.0.0 --port 8000"]
