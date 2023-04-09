FROM ubuntu:latest

# Installing dependencies for running a python application
RUN apt-get update && apt-get install -y python3 python3-pip

WORKDIR /app
COPY app.py .
COPY requirements.txt .

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3", "app.py"]