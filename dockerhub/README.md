# Push images to Docker Hub



In a terminal window, set the environment variable `DOCKER_ID_USER` as your username in Docker Hub.

This allows you to copy and paste the commands directly from this tutorial.

```
$ export DOCKER_ID_USER="username"
```

Log in to Docker Cloud using the docker login command.

```
$ docker login
```
This logs you in using your Docker ID.

If you have never logged in to Docker Hub or Docker Cloud and do not have a Docker ID, running this command prompts you to create a Docker ID.

Tag your image using docker tag.

In the example below replace `DOCKER_ID_USER` with your Docker Hub username if needed.

```
$ docker pull hello-world
$ docker tag hello-world $DOCKER_ID_USER/hello-world
```

Push your image to Docker Hub using docker push (making the same replacements as in the previous step).

```
$ docker push $DOCKER_ID_USER/hello-world
```

Check that the image you just pushed appears in Docker Hub.

# Deploying a registry server

Start your registry:
```
docker run -d -p 5000:5000 --restart=always --name registry registry:2
```

You can now use it with docker.

Get any image from the hub and tag it to point to your registry:
```
docker tag hello-world localhost:5000/hello-world
```
… then push it to your registry:
```
docker push localhost:5000/hello-world
```
… then pull it back from your registry:
```
docker pull localhost:5000/hello-world
```
To stop your registry, you would:
```
docker stop registry && docker rm -v registry
```
