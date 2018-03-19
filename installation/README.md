# Get Docker for Ubuntu

## Uninstall old versions

Older versions of Docker were called `docker` or `docker-engine`. If these are installed, uninstall them:

```
$ sudo apt-get remove docker docker-engine docker.io
```

## Installation


Install packages to allow `apt` to use a repository over HTTPS:

```
$ sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
```

Add Docker’s official GPG key:
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

Verify that the key fingerprint is 9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88.

```
$ sudo apt-key fingerprint 0EBFCD88

pub   4096R/0EBFCD88 2017-02-22
      Key fingerprint = 9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
uid                  Docker Release (CE deb) <docker@docker.com>
sub   4096R/F273FCD8 2017-02-22
```

Use the following command to set up the stable repository.

```
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```



Update the apt package index.

```
$ sudo apt-get update
```

Install Docker

```
$ sudo apt-get install docker-ce
```

Check if your docker is up and running

```
$ sudo docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```


To run docker command without sudo, you need to add your user (who has root privileges) to docker group. For this run following command:

```
$ sudo usermod -aG docker $USER
```

Reboot machine

```
$ sudo reboot
```

You should be able to run docker run hello-world and see a response like this:
```
$ docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
...(snipped)...

```
Now would also be a good time to make sure you are using version correct
```
$ docker --version
Docker version 17.05.0-ce-rc1, build 2878a85
```
If you see messages like the ones above, you’re ready to begin the journey.
