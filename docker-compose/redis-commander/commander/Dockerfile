FROM node

RUN curl -L https://github.com/joeferner/redis-commander/tarball/v0.4.5 | tar zx
RUN npm install -g redis-commander

ENTRYPOINT [ "redis-commander" ] 
CMD [ "--redis-host", "redis" ]

EXPOSE 8081

