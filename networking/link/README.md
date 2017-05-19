# How to connect docker containers 

Docker networking feature can be accessed by using a `--link` flag which allows to connect any number of docker 
containers without the need to expose container's internal ports to the outside world.


In this config you will learn how to link two docker containers together using a simple docker networking technique. 
We can start by the deployment of our first docker container `backend` to which we'll later create a network link: 

```
$ docker run -itd --name backend  busybox
```

The following command will deploy a second and this time a parent docker container named `frontend`. 
We will also use a `--link` flag which will create a so called parent-child relationship with previously deployed container backend.
Furthermore, `--link` flag will enable the parent container to access any services running on `backend` container via its corresponding 
ports numbers without the child container's need to expose any ports to outside world.

```
$ docker run -it --name frontend --link backend:backend busybox /bin/sh
/#
```

This way we can simply use our `backend` container's alias to connect to it from a parent container frontend without the need to hardcode it's IP address: 

```
/ # cat /etc/hosts
127.0.0.1	localhost
::1	localhost ip6-localhost ip6-loopback
fe00::0	ip6-localnet
ff00::0	ip6-mcastprefix
ff02::1	ip6-allnodes
ff02::2	ip6-allrouters
10.1.82.2	backend 44cad6a7b028
10.1.82.3	482c0257bb68

```

so thank to this we can reach `backend` container by alias name:

```
/# ping backend
PING backend (10.1.82.2): 56 data bytes
64 bytes from 10.1.82.2: seq=0 ttl=64 time=0.077 ms
64 bytes from 10.1.82.2: seq=1 ttl=64 time=0.067 ms
64 bytes from 10.1.82.2: seq=2 ttl=64 time=0.043 ms

```

