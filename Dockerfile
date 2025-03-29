# Use a Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents (including README.md and app.py) into the container
COPY . /app

# Install required Python packages
RUN pip install --no-cache-dir flask markdown

# Expose the port Flask will run on
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
