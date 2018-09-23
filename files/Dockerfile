FROM python:3.7-alpine
LABEL name=task
RUN apk update
RUN apk add --no-cache supervisor  gcc linux-headers musl-dev uwsgi-python3 uwsgi python3-dev

COPY requirements.txt /tmp/requirements.txt
RUN python3.6 -m pip install --upgrade pip


RUN python3.6 -m pip install -r /tmp/requirements.txt

COPY uwsgi.ini /etc/uwsgi/
COPY supervisord.ini /etc/supervisor.d/supervisord.ini

COPY metrics /src/

WORKDIR /src
CMD ["/usr/bin/supervisord"]
