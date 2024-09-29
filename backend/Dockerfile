FROM python:3.10.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

# Set a meaningful working directory
WORKDIR /app

# Install the application dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy in the entire source code
COPY . /app

# Setup a non-root user
RUN useradd -m app
RUN chown -R app:app /app
USER app

# Expose the correct port
EXPOSE 8080

# Define the command to run the application
CMD ["uvicorn", "app.bom_automation:app", "--host", "0.0.0.0", "--port", "8080"]


