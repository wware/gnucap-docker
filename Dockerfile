FROM ubuntu
MAINTAINER wware@alum.mit.edu
RUN apt update -y
RUN apt install -y apt-utils
RUN apt install -y python2.7 python-tk gnucap libgnucap0 gwave
COPY ./tryit.py /bin/tryit.py
COPY osc.ckt /osc.ckt
