FROM python:3.10.18-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run migrations, seed database, and start server
CMD python manage.py migrate && \
    python manage.py seed_db && \
    python manage.py runserver 0.0.0.0:8000
