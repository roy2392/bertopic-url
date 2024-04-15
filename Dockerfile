# Use an official Python runtime as a parent image
FROM python:3.10-buster

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install build dependencies
RUN apt-get update && apt-get install -y build-essential

# Upgrade pip and setuptools
RUN pip install --upgrade pip setuptools

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


# Run application.py when the container launches
CMD ["python", "application.py"]