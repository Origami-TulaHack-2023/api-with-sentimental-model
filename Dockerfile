FROM ubuntu:latest
RUN set -xe \
    && apt-get update -y \
    && apt-get install python3-pip -y
RUN pip install --upgrade pip
WORKDIR .
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT sleep infinity