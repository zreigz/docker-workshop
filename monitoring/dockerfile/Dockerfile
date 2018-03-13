FROM alpine
MAINTAINER Lukasz Zajaczkowski "zreigz@gmail.com"

WORKDIR /home
RUN apk add --update python py-pip
COPY factorial.py factorial.py
ENTRYPOINT ["python", "factorial.py"]

