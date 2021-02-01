# set base image
FROM python:3.8

# set working dir in container
WORKDIR /code

# copy dependencies to wd
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of local src directory to the working dir
COPY src/ .

# ?
EXPOSE 5000

# command to run on container start
CMD ["python", "./server.py"]
