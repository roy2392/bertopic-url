
FROM python:3.11

WORKDIR /app

# Copy requirements.txt to the working directory
COPY requirements.txt .

# Install dependencies with verbose output
RUN python -m pip install --verbose -r requirements.txt

COPY . .

# Expose the port that the application listens on.
EXPOSE 8000

# Run the application.
CMD python3 app3.py
