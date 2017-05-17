# Running Docker Container

Running containers is the core functionality of docker because it allows the start of containers and acquisition of the resources and controlling it.

## Run Command

Creating containers is the sole purpose of all these infrastructure.

Using this command will initiate the following work-flow:

  1. It will check for the container locally

  2. Fetch the container from the Docker Hub Repository

  3. Run the container

### Usage

```
$ docker run [OPTIONS] IMAGE[:TAG|@DIGEST] [COMMAND] [ARG...]
```
Although the Image Builder has a default value for each of the following one can override them.

[Options]

The run options control the image’s runtime behavior in a container. These settings affect:

* detached or foreground running
* container identification and name
* network settings and host name
* runtime constraints on CPU and memory
* privileges and LXC configuration

**IMAGE[:TAG|@DIGEST]**

Using an image based on a specific version based on tag or custom made identifier (Digest)

**[COMMAND]**

Specifies commands to run at the start of the container

**[ARG…]**

Other arguments which include adding users and setting environment variable and mounting devices.

## Example

### Hello World container

```
$ docker run hello-world

Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
78445dd45222: Pull complete
Digest: sha256:c5515758d4c5e1e838e9cd307f6c6a0d620b5e07e6f927b07d05f6d12a1ac8d7
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://cloud.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/engine/userguide/
```

### Ubuntu Container

Run an Ubuntu container in interactive (-i) tty (-t) mode.
```
$ docker run -i -t ubuntu /bin/bash
```

#### Commit Changes to Docker

To create a new image from changes to a container, it’s a simple as running just one command. Before we do so, however, let’s change the container!

Update repository and install git:
```
root@62fac3481f58:/# apt-get  update && apt-get install git -y
```

Once you’ve completed those instructions you can disconnect, or detach, from the shell without
exiting use the escape sequence `Ctrl-p and Ctrl-q`.

Find your running instance. Execute the following command:

```
$ docker ps
CONTAINER ID        IMAGE                                                        COMMAND                  CREATED             STATUS              PORTS               NAMES
62fac3481f58        ubuntu                                                       "/bin/bash"              2 minutes ago       Up 2 minutes                            jovial_thompson

```

Finally it’s time to commit our changes to a named image.
This command converts the container 62fac3481f58 to an image with the name ubintu-with-git:
```
$ docker commit 62fac3481f58 ubuntu-with-git
sha256:78cec5314cb72659fa856acb804bc0890594ad391ff028bdb15f0524f70e8c47
```

Now you can check your available images:
```
$ docker images
REPOSITORY                                            TAG                                        IMAGE ID            CREATED              SIZE
ubuntu-with-git                                       latest                                     78cec5314cb7        About a minute ago   246.5 MB
....
....
```

Every image tracks own history

```
$ docker history ubuntu-with-git
IMAGE               CREATED             CREATED BY                                      SIZE                COMMENT
78cec5314cb7        2 minutes ago       /bin/bash                                       128.5 MB
ebcd9d4fca80        40 hours ago        /bin/sh -c #(nop)  CMD ["/bin/bash"]            0 B
<missing>           40 hours ago        /bin/sh -c mkdir -p /run/systemd && echo 'doc   7 B
<missing>           40 hours ago        /bin/sh -c sed -i 's/^#\s*\(deb.*universe\)$/   2.759 kB
<missing>           40 hours ago        /bin/sh -c rm -rf /var/lib/apt/lists/*          0 B
<missing>           40 hours ago        /bin/sh -c set -xe   && echo '#!/bin/sh' > /u   745 B
<missing>           40 hours ago        /bin/sh -c #(nop) ADD file:d14b493577228a4989   117.9 MB
```

To show image information like IP adress, enviroment.

```
$ docker inspect ubuntu-with-git
```

Now is time to clean up. Please find your container and kill it:
```
$ docker ps
CONTAINER ID        IMAGE                                                        COMMAND                  CREATED             STATUS              PORTS               NAMES
62fac3481f58        ubuntu                                                       "/bin/bash"              2 minutes ago       Up 2 minutes                            jovial_thompson

$ docker kill 62fac3481f58
$ docker ps
CONTAINER ID        IMAGE                                                        COMMAND                  CREATED             STATUS              PORTS               NAMES
```
