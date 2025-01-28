# Use the official Python image as a base image
FROM python:3.10-slim
# Add .local/bin to PATH
ENV PATH="/home/appuser/.local/bin:$PATH"

# Upgrade pip
RUN pip install --upgrade pip

# Set environment variables to prevent Python from buffering output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH="/app"

# Create the /app directory and set permissions
RUN mkdir /app && adduser --disabled-password --gecos '' appuser && chown -R appuser /app

# Switch to the non-root user
USER appuser

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
# Copy the entire project into the /app directory
COPY . /app



# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app

# Expose the port for the Flask API
EXPOSE 5000

# Set the default command to run the Flask app
CMD ["python", "api/server.py"]

