# # Use a base image with Python
# FROM python:3.9
# # FROM public.ecr.aws/lambda/python:3.9

# # Set environment variables for AWS credentials (replace with your own)


# # Set the working directory in the container
# WORKDIR /app

# # Copy the Python script and requirements file into the container
# COPY requirements.txt /app/requirements.txt

# # Install Python dependencies
# RUN pip install --no-cache-dir -r /app/requirements.txt

# COPY read.py /app/read.py

# # Install system dependencies (FFmpeg for MoviePy)
# RUN apt-get update && apt-get install -y ffmpeg

# # Run the Python script when the container starts
# CMD ["python", "/app/read.py"]

# Use a base Python image
FROM python:3.9

# Install system dependencies (e.g., ffmpeg)
# RUN apt-get update && apt-get install -y ffmpeg

# Set the working directory in the container
WORKDIR /app

# Copy your Python script into the container
COPY ecs_task.py /app
COPY requirements.txt /app

RUN pip install boto3
RUN pip install moviepy
RUN pip install --no-cache-dir -r /app/requirements.txt

# Install Python dependencies (if any)
# RUN pip install ...

# Define the command to run your Python script
CMD ["python", "ecs_task.py"]
