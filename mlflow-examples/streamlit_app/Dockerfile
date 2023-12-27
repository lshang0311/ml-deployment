# Use a base image with Python and Streamlit dependencies
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy the Streamlit app files into the container
COPY app.py /app/

# Install required dependencies
RUN pip install streamlit joblib

# Expose the port the Streamlit app will run on (typically 8501)
EXPOSE 8501

# Define the command to run when the container starts
CMD ["streamlit", "run", "app.py"]