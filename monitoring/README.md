# Docker monitoring

## Docker Stats

The first tool I will talk about is Docker itself, yes you may not be aware that docker client already provides a rudimentary command line tool to inspect containers’ resource consumption. To look at the container stats run docker stats with the name(s) of the running container(s) for which you would like to see stats. This will present the CPU utilization for each container, the memory used and total memory available to the container. Note that if you have not limited memory for containers this command will post total memory of your host. This does not mean each of your container has access to that much memory. In addition you will also be able to see total data sent and received over the network by the container.

First start container which generates high CPU load:

```
$ docker run --name high-load -d zreigz/load

```

Check the statistics:

```
$ docker stats high-load

```
## CAdvisor

The docker stats command and the remote API are useful for getting information on the command line, however, if you would like to access the information in a graphical interface you will need a tool such as CAdvisor. CAdvisor provides a visual representation of the data shown by the docker stats command earlier.  Run the docker command below and go to http://<your-hostname>:8080/ in the browser of your choice to see the CAdvisor interface. 

```
docker run                                      \
  --volume=/:/rootfs:ro                         \
  --volume=/var/run:/var/run:rw                 \
  --volume=/sys:/sys:ro                         \
  --volume=/var/lib/docker/:/var/lib/docker:ro  \
  --publish=8080:8080                           \
  --detach=true                                 \
  --name=cadvisor                               \
  google/cadvisor:latest
```

CAdvisor is a useful tool that is trivially easy to setup, it saves us from having to ssh into the server to look at resource consumption and also produces graphs for us.


