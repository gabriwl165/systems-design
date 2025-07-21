# syntax=docker/dockerfile:1
FROM python:3.10-slim

# Install Poetry
RUN pip install poetry

# Set workdir
WORKDIR /app

# Copy only necessary files
COPY pyproject.toml poetry.lock* /app/

# Install dependencies
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-root

# Copy project files
COPY ./python_example_api /app/python_example_api

# Expose port
EXPOSE 8000

# Run the app
CMD ["python", "-m", "python_example_api"]
