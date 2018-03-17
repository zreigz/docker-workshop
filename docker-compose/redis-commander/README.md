
# Docker Compose

Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a Compose file to configure your application’s services. Then, using a single command, you create and start all the services from your configuration. To learn more about all the features of Compose see the list of features.

Compose is great for development, testing, and staging environments, as well as CI workflows. 

## Install Docker Compose
Download Compose version 1.19.0, the command is:

```
sudo curl -L https://github.com/docker/compose/releases/download/1.19.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
```

Apply executable permissions to the binary:

```
$ sudo chmod +x /usr/local/bin/docker-compose

```

Test the installation.
```
$ docker-compose --version
docker-compose version 1.19.0, build 1719ceb
```

## Example

Let’s create a project with the following structure:
```
redis-commander
       ├── commander
       │   └── Dockerfile
       ├── docker-compose.yml
       └── README.md
```
where

`docker-compose.yml`
```
version: '3'
services:
  redis:
    container_name: redis
    hostname: redis
    image: redis

  redis-commander:
    container_name: redis-commander
    hostname: redis-commander
    image: rediscommander/redis-commander:latest
    build: commander
    restart: always
    environment:
    - REDIS_HOSTS=local:redis:6379
    ports:
    - 8081:8081
```

To run containers execute the following command:

```
docker-compose up -d --build
```
where
- `up` create and start containers
- `-d` detached mode: Run containers in the background, print new container names. 
- `--build` build images before starting containers

The command docker-compose up -d has the same effect as the following sequence of commands:
```
docker build -t rediscommander/redis-commander:latest commander
docker run -d --name frontend -e REDIS_HOSTS=local:redis:6379 -p 8081:8081
   --link redis:redis redis-commander
```

To check status execute `docker-compose ps` command.

```

    Name                    Command               State           Ports         
---------------------------------------------------------------------------------
redis             docker-entrypoint.sh redis ...   Up      6379/tcp              
redis-commander   redis-commander --redis-ho ...   Up      0.0.0.0:8081->8081/tcp

````

You can also check container logs:

```
$ docker-compose logs redis

```
When we want to clean enviroment then we have to execute:

```
docker-compose down && docker-compose rm -v
```




