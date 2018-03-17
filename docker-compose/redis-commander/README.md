
#Docker Compose

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

