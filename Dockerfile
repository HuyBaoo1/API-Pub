# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat-openbsd && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Make wait script executable
RUN chmod +x /app/wait-for-postgres.sh

# Run app after PostgreSQL is ready
CMD ["./wait-for-postgres.sh", "postgres_db", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
