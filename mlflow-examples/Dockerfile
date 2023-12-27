# Use an official Python runtime as a parent image
FROM python:3.11

ENV RUNNING_IN_DOCKER=true

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the FastAPI application script and requirements.txt
COPY ex_2_model_serving_with_fastapi.py ./
COPY requirements.txt ./

# Copy the model directory
COPY mlruns/0/7c7b3be169eb4771a04136c0a96df2bd/artifacts/model ./model

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run ex_2_model_serving_with_fastapi.py when the container launches
CMD ["uvicorn", "ex_2_model_serving_with_fastapi:app", "--host", "0.0.0.0", "--port", "8000"]
