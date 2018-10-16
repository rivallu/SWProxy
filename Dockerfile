FROM python:2.7-alpine
MAINTAINER Lucas Rival <lucas.rival@gmail.com>


RUN apk add --no-cache git g++ make
RUN git clone https://github.com/rivallu/SWProxy
RUN git branch webUI
WORKDIR SWProxy
RUN mkdir data
RUN pip install -r requirements.txt

ENTRYPOINT ["/usr/local/bin/python", "/app/app.py"]
