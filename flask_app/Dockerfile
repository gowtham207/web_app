FROM python:3.9-slim

WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /app

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY .  .

EXPOSE 80

# Define the command to run the Flask app
CMD ["python","main.py"]
