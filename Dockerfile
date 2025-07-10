# Start from official Python image
FROM python:3.11-slim

# Set workdir
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Run server
CMD ["gunicorn", "school_one.wsgi:application", "--bind", "0.0.0.0:8000"]
