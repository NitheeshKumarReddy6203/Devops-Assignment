FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy all files from the current directory to the container's /app directory
COPY . /app

# Copy the requirements.txt from the infrastructure folder into the container
COPY infrastructure/requirements.txt /app/requirements.txt

# Install dependencies from the requirements.txt file
RUN pip install --no-cache-dir -r /app/requirements.txt

# Set the default command to run the application (adjust as needed)
CMD ["python", "app.py"]
