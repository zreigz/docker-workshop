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

### Ubuntu Container

Run an Ubuntu container in interactive (-i) tty (-t) mode.
```
$ docker run -i -t --name cowsay ubuntu /bin/bash
```

#### Commit Changes to Docker

To create a new image from changes to a container, it’s a simple as running just one command. Before we do so, however, let’s change the container!

Update repository and install `cowsay` application:
```
root@62fac3481f58:/# apt-get  update && apt-get install cowsay -y
```

Once you’ve completed those instructions you can disconnect, or detach, from the shell without
exiting use the escape sequence `Ctrl-p and Ctrl-q`.

Find your running instance. Execute the following command:

```
$ docker ps --filter 'name=cow*'

CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
1e1fb405cfef        ubuntu              "/bin/bash"         5 minutes ago       Up 5 minutes                            cowsay

```

Finally it’s time to commit our changes to a named image.
This command converts the container with name `cowsay` to an image with the name ubuntu-cowsay:
```
$ docker commit cowsay ubuntu-cowsay
sha256:78cec5314cb72659fa856acb804bc0890594ad391ff028bdb15f0524f70e8c47
```

Now you can check your available images:
```
$ docker images '*cowsay'
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
ubuntu-cowsay       latest              fdebe69c4433        5 minutes ago       160MB
```

Every image tracks own history

```
$ docker history ubuntu-cowsay
IMAGE               CREATED             CREATED BY                                      SIZE                COMMENT
fdebe69c4433        6 minutes ago       /bin/bash                                       80.6MB              
452a96d81c30        12 days ago         /bin/sh -c #(nop)  CMD ["/bin/bash"]            0B                  
<missing>           12 days ago         /bin/sh -c mkdir -p /run/systemd && echo '...   7B                  
<missing>           12 days ago         /bin/sh -c sed -i 's/^#\s*\(deb.*universe\...   2.76kB              
<missing>           12 days ago         /bin/sh -c rm -rf /var/lib/apt/lists/*          0B                  
<missing>           12 days ago         /bin/sh -c set -xe   && echo '#!/bin/sh' >...   745B                
<missing>           12 days ago         /bin/sh -c #(nop) ADD file:81813d6023adb66...   79.6MB              

```

To show image information like IP address, environment.

```
$ docker inspect ubuntu-cowsay
```

You can filter out some informations:

#### Examples
Get an instance’s IP address
For the most part, you can pick out any field from the JSON in a fairly straightforward manner.
```
$ docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' cowsay
172.17.0.3
```

Get an instance’s MAC address
```
$ docker inspect --format='{{range .NetworkSettings.Networks}}{{.MacAddress}}{{end}}' cowsay
02:42:ac:11:00:03
```


Now is time to `attach` to the running container. Basically, if the docker container was started using `/bin/bash` command you can access it using `attach`

```
$ docker attach cowsay
root@1e1fb405cfef:/#
```

Inside the container execute the command: `/usr/games/cowsay -f gnu Docker is the Best`

```
root@1e1fb405cfef:/# /usr/games/cowsay -f gnu Docker is the Best

```

Because you are attached to `/bin/bash` process the `exit` command will kill the container:

```
# exit
$
```

Now the command:

```
$ docker ps --filter 'name=cow*'
```

will show nothing.
