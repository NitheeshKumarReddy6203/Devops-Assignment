# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the local Python code into the container
COPY . /app

# Install any dependencies (if you have a requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt

# Expose the app's port (if needed)
EXPOSE 5000

# Define the command to run the calculator application
CMD ["python", "calculator.py"]
