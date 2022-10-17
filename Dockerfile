# Start by pulling the python image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
# Set and create the working directory to /app
WORKDIR /app
# Copy the requirements text file contents into /app
COPY requirements.txt .
# Informs docker that this container should listen to network port 8000 at runtime
EXPOSE 8000
# Install the dependencies and packages in the requirements file
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# Copy the current directory contents into /app
COPY . /app
# Executing the container
CMD ['python','app.py']
