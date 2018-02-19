FROM ubuntu:16.04

RUN apt-get update && apt-get -y upgrade
# groff being difficult
RUN apt-get update
RUN apt-get install -y \
  build-essential \
  checkinstall \
  groff-base \
  less \
  libreadline-gplv2-dev \
  libncursesw5-dev \
  libssl-dev \
  libsqlite3-dev \
  libcurl4-openssl-dev \
  wget \
  vim

WORKDIR /opt
RUN wget https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tgz
RUN tar -xvf Python-3.6.4.tgz
WORKDIR /opt/Python-3.6.4
RUN ./configure
RUN make
RUN make install
RUN ln -s /usr/local/bin/python3 /usr/bin/python
RUN ln -s /usr/local/bin/pip3 /usr/bin/pip
RUN pip install awscli \
  boto \
  boto3 \
  celery \
  pycurl \
  requests

WORKDIR /code
