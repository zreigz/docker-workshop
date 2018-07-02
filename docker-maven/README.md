# Dockerizing Java application
## Introduction
The aim of this exercise is to build microservice written in Java using Docker container.
The microservice (based on `Dropwizard` framework) starts Jetty server and expose REST service which returns actual time and date.
## Building Java applications with maven container
First clone the project:
```
$ git clone https://github.com/zreigz/web-timer.git
```
Go to the project:
```
$ cd web-timer
```
Time to build the project with maven. Try using the new official images, there's one for Maven: [https://hub.docker.com/_/maven/](https://hub.docker.com/_/maven/)

In this exercise, we are going to use only available docker commands. Let's assume also we don't know Docker volumes yet. To handle this situation we need to copy source files to maven container and execute `mvn clean install command`. Finally, we have to copy result storied in the container to our host.

Let's start maven container first:

```
$ docker run -itd --name maven -w /opt/maven maven:3.5.3-jdk-7 sh
```
where `-w` set working directory inside the container

The container is up and running and waits for our farther steps:

```
$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS               NAMES
f420261279ea        maven:3.5.3-jdk-7   "/usr/local/bin/mv..."   29 minutes ago      Up 29 minutes                           maven

```

Copy source files to the working directory inside the container.

```
$ docker cp ./ maven:/opt/maven
```

Run build process inside the `maven` container:

```
$ docker exec -it maven mvn clean install
....
....
[INFO] Installing /opt/maven/target/time-service-0.0.1-SNAPSHOT.jar to /root/.m2/repository/zreigz/time-service/0.0.1-SNAPSHOT/time-service-0.0.1-SNAPSHOT.jar
[INFO] Installing /opt/maven/dependency-reduced-pom.xml to /root/.m2/repository/zreigz/time-service/0.0.1-SNAPSHOT/time-service-0.0.1-SNAPSHOT.pom
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 01:23 min
[INFO] Finished at: 2018-05-10T09:56:57Z
[INFO] ------------------------------------------------------------------------

```

Now check if target directory was created

```
$ docker exec -it maven ls
README.md  configuration.yml  dependency-reduced-pom.xml  pom.xml  src	target
```

and copy `jar` file to your host:

```
$ docker cp maven:/opt/maven/target/time-service-0.0.1-SNAPSHOT.jar ./
```

## Start the microservice

Now you need Java environment to start the microservice.
Start the Java container:
```
$ docker run -itd -p 9999:8080 --name openjdk openjdk:alpine sh
```
where `-p 9999:8080` redirects opened microservice port `8080` to host port `9999`.

Copy source files to new created container:
```
$ docker cp configuration.yml openjdk:/
$ docker cp time-service-0.0.1-SNAPSHOT.jar openjdk:/
```
Start the microservice inside the `openjdk` container:

```
$ docker exec -it openjdk java -jar time-service-0.0.1-SNAPSHOT.jar server configuration.yml
```
To detach from the shell without exiting use the escape sequence `Ctrl-p` and `Ctrl-q`.

In terminal or WEB browser check if it is working.

```
$ curl localhost:9999/time
{"time" : "2018/05/10 12:04:08"}
```
