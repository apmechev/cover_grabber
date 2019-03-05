FROM debian:stable-slim

RUN apt-get update && apt-get install -y python-setuptools python-mutagen git
RUN git clone https://github.com/toozej/cover_grabber /tmp/cover_grabber
RUN cd /tmp/cover_grabber && python setup.py install

ENTRYPOINT covergrabber
