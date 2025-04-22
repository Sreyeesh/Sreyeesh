FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install required packages
RUN pip install --no-cache-dir flask markdown

# Create dist directory in case of export
RUN mkdir -p /app/dist

# Expose Flask default port
EXPOSE 5000

# Run the Flask app or export HTML depending on environment
CMD ["python", "app.py"]
