# Use official Python runtime as a base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port for the web server
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
