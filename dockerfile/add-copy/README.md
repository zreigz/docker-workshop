# ADD or COPY
Although `ADD` and `COPY` are functionally similar, generally speaking, `COPY` is preferred. That’s because it’s more transparent than `ADD`. 
`COPY` only supports the basic copying of local files into the container, while `ADD` has some features 
(like local-only tar extraction and remote URL support) that are not immediately obvious. 
Consequently, the best use for `ADD` is local tar file auto-extraction into the image, as in `ADD rootfs.tar.xz /`.

## Dockerfile

```
FROM php:7.0-apache
MAINTAINER Lukasz Zajaczkowski "zreigz@gmail.com"

COPY index.html /var/www/html/index.html
ADD image.tar.gz /var/www/html/

EXPOSE 80
```
## Build image

```
$ docker build -t web-example .
```

## Run container

```
$ docker run -d -p 8090:80 web-example
```
Now you can open WEB browser and enter url for your server: `host_ip:8090`
