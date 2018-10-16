FROM python:2.7-alpine
MAINTAINER Lucas Rival <lucas.rival@gmail.com>


RUN apk add --no-cache git g++ make

#RUN git clone https://github.com/rivallu/SWProxy
WORKDIR SWProxy
RUN mkdir data
COPY requirements.txt .
RUN pip install -r requirements.txt

ENTRYPOINT ["/usr/local/bin/python", "/SWProxy/app.py"]
