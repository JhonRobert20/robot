FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN pip install virtualenv
RUN virtualenv -p python virtual
RUN /bin/bash -c "source /virtual/bin/activate"
RUN pip install --upgrade pip

WORKDIR /code
COPY . .
