FROM python:3.11.9

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends git python3-pip \
  && apt-get clean && rm -rf /tmp/* /var/tmp/*

WORKDIR /app
COPY ./ /app

RUN pip3 install --no-cache-dir --upgrade -r demo/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r recursive_root/requirements.txt

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

EXPOSE 10000

# run uvicorn to start ASGI server
ENTRYPOINT ["python3", "main.py"]