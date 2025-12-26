# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file and install dependencies
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the application code
COPY ./main.py /code/

# Command to run the application using uvicorn (use "exec form" for graceful shutdown)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
