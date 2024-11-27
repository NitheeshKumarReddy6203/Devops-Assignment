FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy all files from the current directory to the container's /app directory
COPY calculator.py /app

# Set the default command to run the application (adjust as needed)
CMD ["python", "calculator.py"]
