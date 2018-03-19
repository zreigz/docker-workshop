FROM alpine:3.3
RUN apk --update add apache2 curl && rm -rf /var/cache/apk/*
RUN mkdir -p /run/apache2
EXPOSE 80
CMD httpd -D FOREGROUND
HEALTHCHECK --interval=15s --timeout=3s \
  CMD curl -f http://localhost/ || exit 1

