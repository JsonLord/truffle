FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN pip install uv

# Copy requirements
COPY requirements.txt .

# Install dependencies using uv
RUN uv pip install --system -r requirements.txt

# Copy project
COPY . .

# Create a non-root user
RUN useradd -m appuser
RUN chown -R appuser:appuser /app
USER appuser

# Set the path to include the user's local bin
ENV PATH="/home/appuser/.local/bin:${PATH}"

# Expose port 7860
EXPOSE 7860

# Run migrations and start server
CMD ["sh", "-c", "cd socials && python manage.py migrate && python create_superuser.py && gunicorn socials.wsgi:application --bind 0.0.0.0:7860"]
