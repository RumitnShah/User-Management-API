# Use an official Python runtime as the base image
FROM python:3.9-slim-buster

ARG port

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Export environment variables from the .env file
RUN export $(grep -v '^#' /app/.env | xargs)

# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Expose $port for Flask to listen on
ENV PORT=$port

# Define the command to run the app when the container starts
CMD ["flask", "run", "--host=0.0.0.0"]