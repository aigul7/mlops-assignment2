# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY local/ ./local/
COPY docs/ ./docs/
COPY README.md .

# Set environment variable
ENV PYTHONUNBUFFERED=1

# Default command - generate data
CMD ["python", "local/create_data.py"]