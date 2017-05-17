# Push images to Docker Hub



In a terminal window, set the environment variable `DOCKER_ID_USER` as your username in Docker Cloud.

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

In the example below replace my_image with your image’s name, and `DOCKER_ID_USER` with your Docker Hub username if needed.

```
$ docker tag my_image $DOCKER_ID_USER/my_image
```

Push your image to Docker Hub using docker push (making the same replacements as in the previous step).

```
$ docker push $DOCKER_ID_USER/my_image
```

Check that the image you just pushed appears in Docker Hub.
