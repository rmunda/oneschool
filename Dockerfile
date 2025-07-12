# Start from official Python image
FROM python:3.11-slim

# Install dependencies (netcat + build essentials)
RUN apt-get update && apt-get install -y --no-install-recommends \
    netcat-openbsd \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set workdir
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Run server
# CMD ["gunicorn", "school_one.wsgi:application", "--bind", "0.0.0.0:8000"]
# CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn school_one.wsgi:application --bind 0.0.0.0:8000"]
COPY wait-for-db.sh /wait-for-db.sh
RUN chmod +x /wait-for-db.sh

CMD ["/wait-for-db.sh"]

