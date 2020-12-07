FROM python:2.7-alpine3.7
MAINTAINER wware@alum.mit.edu
RUN apk update
RUN apk add python2-tkinter
COPY ./tryit.py /bin/tryit.py
CMD tryit.py
