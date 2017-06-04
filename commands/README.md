# Container Control Commands

## Create `nginx` container.

### What is Nginx?

Nginx (pronounced "engine-x") is an open source reverse proxy server for HTTP, HTTPS, SMTP, POP3, and IMAP protocols, as well as a load balancer, HTTP cache, and a web server (origin server).


```
docker create -p 8080:80 nginx
```

where `-p` redirect container port 80 (nginx listen on this port) to host port 8080.

Check if container was creted 

```
$ docker ps -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS               NAMES
9aadcef8e731        nginx               "nginx -g 'daemon ..."   4 seconds ago       Created                                 vigilant_keller
```

Container is created but not started:

```
$ docker start 9aadcef8e731
$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS              PORTS                  NAMES
9aadcef8e731        nginx               "nginx -g 'daemon ..."   About a minute ago   Up 4 seconds        0.0.0.0:8080->80/tcp   vigilant_keller

```
The `nginx` container is up and running. Now we can try to connect to this server:

```
$ curl localhost:8080

<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>

```

Now lets try to replace this page with our custom page.

```
docker cp index.html 9aadcef8e731:/usr/share/nginx/html
```

Now nginx should display new content:

```
$ curl localhost:8080

Welcome to docker workshop
```

Check the container logs:

```
$ docker logs 9aadcef8e731
```

Last thing is to stop and remove the nginx container:

```
$ docker stop 9aadcef8e731

$ docker rm 9aadcef8e731

$ docker ps 

CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES

```

## Attach to a running Container

Now, its time for something interesting to help us understand some more commands. We will continue with our example around busybox Image.

First up, we will relaunch our container without the -i (interactive) mode.

```
$ docker run -it -d busybox /bin/sh
```

Whoops ! What happened ?

The only output that we got was the CONTAINER ID back.

What has just happened is that the Container has got launched and all that docker client has done is give you the Container ID back.

Give the following command to check out the current running containers (the command should be familiar to you now):
```
$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
748610e35694        busybox             "/bin/sh"           4 seconds ago       Up 4 seconds                            unruffled_engelbart
```
This gives us the output that the CONTAINER is running (Check the STATUS column. You will find that it says it is Up!)

We can attach to a running Container via the docker attach command. Let us attach to it:
```
$ docker attach 748610e35694
```
This will get you back to the Prompt i.e. you are now inside the busybox container. Type exit to exit the container and then try the docker ps command. There will be no running containers.
