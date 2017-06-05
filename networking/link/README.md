# How to connect docker containers 

The `docker network` command is the main command for configuring and managing container networks. Run the `docker network` command.

```
$ docker network

Usage:    docker network COMMAND

Manage networks

Options:
      --help   Print usage

Commands:
  connect     Connect a container to a network
  create      Create a network
  disconnect  Disconnect a container from a network
  inspect     Display detailed information on one or more networks
  ls          List networks
  prune       Remove all unused networks
  rm          Remove one or more networks

Run 'docker network COMMAND --help' for more information on a command.
```

The command output shows how to use the command as well as all of the `docker network` sub-commands. As you can see from the output, the `docker network` command allows you to create new networks, list existing networks, inspect networks, and remove networks. It also allows you to connect and disconnect containers from networks.

## List networks

Run a `docker network ls` command to view existing container networks on the current Docker host.

```
$ docker network ls
NETWORK ID          NAME                DRIVER              SCOPE
3430ad6f20bf        bridge              bridge              local
a7449465c379        host                host                local
06c349b9cc77        none                null                local
```

The output above shows the container networks that are created as part of a standard installation of Docker.

New networks that you create will also show up in the output of the `docker network ls` command.

You can see that each network gets a unique `ID` and `NAME`. Each network is also associated with a single driver. Notice that the "bridge" network and the "host" network have the same name as their respective drivers.

## Inspect a network

The `docker network inspect` command is used to view network configuration details. These details include; name, ID, driver, IPAM driver, subnet info, connected containers, and more.

Use `docker network inspect <network>` to view configuration details of the container networks on your Docker host. The command below shows the details of the network called `bridge`.

```
$ docker network inspect bridge
[
    {
        "Name": "bridge",
        "Id": "3430ad6f20bf1486df2e5f64ddc93cc4ff95d81f59b6baea8a510ad500df2e57",
        "Created": "2017-04-03T16:49:58.6536278Z",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "172.17.0.0/16",
                    "Gateway": "172.17.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Containers": {},
        "Options": {
            "com.docker.network.bridge.default_bridge": "true",
            "com.docker.network.bridge.enable_icc": "true",
            "com.docker.network.bridge.enable_ip_masquerade": "true",
            "com.docker.network.bridge.host_binding_ipv4": "0.0.0.0",
            "com.docker.network.bridge.name": "docker0",
            "com.docker.network.driver.mtu": "1500"
        },
        "Labels": {}
    }
]
```

> **NOTE:** The syntax of the `docker network inspect` command is `docker network inspect <network>`, where `<network>` can be either network name or network ID. In the example above we are showing the configuration details for the network called "bridge". Do not confuse this with the "bridge" driver.


## List network driver plugins

The `docker info` command shows a lot of interesting information about a Docker installation.

Run the `docker info` command and locate the list of network plugins.

```
$ docker info
Containers: 0
 Running: 0
 Paused: 0
 Stopped: 0
Images: 0
Server Version: 17.03.1-ee-3
Storage Driver: aufs
<Snip>
Plugins:
 Volume: local
 Network: bridge host macvlan null overlay
Swarm: inactive
Runtimes: runc
<Snip>
```

The output above shows the **bridge**, **host**,**macvlan**, **null**, and **overlay** drivers.

# Bridge Networking


## The Basics

Every clean installation of Docker comes with a pre-built network called **bridge**. Verify this with the `docker network ls` command .

```
$ docker network ls
NETWORK ID          NAME                DRIVER              SCOPE
3430ad6f20bf        bridge              bridge              local
a7449465c379        host                host                local
06c349b9cc77        none                null                local
```

The output above shows that the **bridge** network is associated with the *bridge* driver. It's important to note that the network and the driver are connected, but they are not the same. In this example the network and the driver have the same name - but they are not the same thing!

The output above also shows that the **bridge** network is scoped locally. This means that the network only exists on this Docker host. This is true of all networks using the *bridge* driver - the *bridge* driver provides single-host networking.

All networks created with the *bridge* driver are based on a Linux bridge (a.k.a. a virtual switch).


## Connect a container

The **bridge** network is the default network for new containers. This means that unless you specify a different network, all new containers will be connected to the **bridge** network.

Create a new bridge network and call it `br`.

```
$ docker network create -d bridge br
846af8479944d406843c90a39cba68373c619d1feaa932719260a5f5afddbf71
```

Now create a container called `c1` and attach it to your new `br` network.

```
$ docker run -itd --net br --name c1 alpine sh
846af8479944d406843c90a39cba68373c619d1feaa932719260a5f5afddbf71
```

This command will create a new container based on the `alpine:latest` image. 

Running `docker network inspect bridge` will show the containers on that network.

```
$ docker network inspect br

[
    {
        "Name": "br",
        "Id": "e7b30cacc686ff891a5a5ea393e055c309a07bc652feed375821e2f78faf9aa0",
        "Created": "2017-04-13T13:19:37.611068665Z",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "172.17.0.0/16",
                    "Gateway": "172.17.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Containers": {
            "086c4c0cc18c7f603279b728d9baac4b63d25941f576b37c5d1e988de6202410": {
                "Name": "c1",
                "EndpointID": "06eac477e1a04f2c5e676633ddab344086104511470c539a2fb7aedf8b1d58f8",
                "MacAddress": "02:42:ac:11:00:06",
                "IPv4Address": "172.17.0.6/16",
                "IPv6Address": ""
```



## Test network connectivity

The output to the previous `docker network inspect` command shows the IP address of the new container. In the previous example it is "172.17.0.6" but yours might be different.

Ping the IP address of the container from the shell prompt of your Docker host by running `ping -c 3 <IPv4 Address>`. Remember to use the IP of the container in **your** environment.

You can get the IP address of the container directly from the Docker engine by running `docker inspect --format "{{ .NetworkSettings.Networks.br.IPAddress }}" c1`.

```
$ ping -c 3 172.17.0.6
PING 172.17.0.6 (172.17.0.6) 56(84) bytes of data.
64 bytes from 172.17.0.6: icmp_seq=1 ttl=64 time=0.072 ms
64 bytes from 172.17.0.6: icmp_seq=2 ttl=64 time=0.029 ms
64 bytes from 172.17.0.6: icmp_seq=3 ttl=64 time=0.048 ms
...
```

The replies above show that the Docker host can ping the container over the **bridge** network. But, we can also verify the container can connect to the outside world too. 

Enter in to the `c1` container that you created using the command `docker exec`. We will pass the `sh` command to `docker exec` which puts us in to an interactive shell inside the container.

Enter in to the container and inspect the interfaces of the container

```
$ docker exec -it c1 sh
 # ip addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
879: eth0@if880: <BROADCAST,MULTICAST,UP,LOWER_UP,M-DOWN> mtu 1500 qdisc noqueue state UP
    link/ether 02:42:ac:13:00:02 brd ff:ff:ff:ff:ff:ff
    inet 172.19.0.6/16 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::42:acff:fe13:2/64 scope link
       valid_lft forever preferred_lft forever
```

Prove that containers can gain outside access by pinging `www.docker.com`.

```
 # ping -c 3 www.docker.com
PING www.docker.com (104.239.220.248): 56 data bytes
64 bytes from 104.239.220.248: seq=0 ttl=36 time=77.722 ms
64 bytes from 104.239.220.248: seq=1 ttl=36 time=77.865 ms
64 bytes from 104.239.220.248: seq=2 ttl=36 time=77.830 ms
```

Exit out of the container.

```
 # exit
```

Now you will create a second container on this bridge so you can test connectivity between them.

```
$ docker run -itd --net br --name c2 alpine sh
75f840c9d17b2921c1e78555c97cd5116e1563b1e33f9328bd5b0a8e1c55b520
```

Enter the `c2` container with `docker exec` and try to ping the IP address of `c1`.

```
$ docker exec -it c2 sh
 # ping -c 3 172.17.0.6
PING 172.17.0.6 (172.17.0.6): 56 data bytes
64 bytes from 172.17.0.6: seq=0 ttl=64 time=0.091 ms
64 bytes from 172.17.0.6: seq=1 ttl=64 time=0.077 ms
64 bytes from 172.17.0.6: seq=2 ttl=64 time=0.079 ms
```

Now ping container `c1` using it's name. The Docker engine will provide the resolution automatically for all container names and service names.


```
 # ping -c 3 c1
PING c1 (172.17.0.6): 56 data bytes
64 bytes from 172.17.0.6: seq=0 ttl=64 time=0.091 ms
64 bytes from 172.17.0.6: seq=1 ttl=64 time=0.077 ms
64 bytes from 172.17.0.6: seq=2 ttl=64 time=0.079 ms
```

Exit container `c2` and remove these two containers from this host.

```
# exit
$ docker rm -f $(docker ps -aq)
```


# Link containers

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

