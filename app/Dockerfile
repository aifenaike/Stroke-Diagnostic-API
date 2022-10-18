# Start by pulling the python image
FROM python:3.9

WORKDIR /app
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt
COPY . .
EXPOSE 8000


# COPY ./app /app/app

# COPY ./requirements.txt .

# WORKDIR /app

# RUN pip install -r requirements.txt

# EXPOSE 8000

# CMD ['uvicorn', "app.app:app", "--host=0.0.0.0", "--reload"]






# WORKDIR /app
# # Copy the requirements text file contents into /app
# COPY requirements.txt .

# # Install the dependencies and packages in the requirements file
# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt
# # Copy the current directory contents into /app
# COPY . /app
# # Informs docker that this container should listen to network port 8000 at runtime
# # EXPOSE 8000
# # Executing the container
# CMD ["uvicorn","app.app:app","--host","0.0.0.0"."--port","15400"]
