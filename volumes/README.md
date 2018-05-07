# Understanding Volumes in Docker

There are several ways to initialise volumes, with some subtle differences that are important to understand. 
The most direct way is declare a volume at run-time with the `-v` flag:

## Data volume containers

```
$ docker run -it --name vol-test -v /data busybox /bin/sh
```

This will make the directory `/data` inside the container live outside the Union File System and directly accessible on the host. 
Any files that the image held inside the `/data` directory will be copied into the volume. 

Now create new file in `/data` directory

```
/ # cd data
/data # echo "test vol" > test.txt
/data # exit
```


We can find out where the volume lives on the host by using the `docker inspect` command on the host

```
$ docker inspect vol-test

...

            {
                "Name": "c2bda23b77468d435449cb10e0b7cc2fac3376cac3c45c19db735d4967571743",
                "Source": "/var/lib/docker/volumes/c2bda23b77468d435449cb10e0b7cc2fac3376cac3c45c19db735d4967571743/_data",
                "Destination": "/data",
                "Driver": "local",
                "Mode": "",
                "RW": true,
                "Propagation": ""
            }
        ],

...
```

Great ! Now, let us launch another container (container2) but it will mount the data volume from vol-test as given below:


```
docker run -it --volumes-from vol-test --name container2 busybox
```

Notice above that we have launched it in interactive mode and have used a new parameters `--volumes-from <containername>` that we have specified. 
This tells container2 to mount the volume vol-test.

Now, if we do a ls, we can see that the data folder is present and if we do a ls inside of that, we can see our file: `test.txt`

```
/ # ls /data
test.txt
/ # cat /data/test.txt 
test vol
/ # exit
```

## Mounting a Data volume

Create some test file in your current location

```
$ echo "test data" > test.txt
```

Now mount your current directory in started conatiner

```
$ docker run -it -v `pwd`:/data --name host-volume busybox /bin/sh
/# ls /data
test.txt
/# cat /data/test.txt
test data
/# exit
```

We can find out where the volume lives on the host by using the `docker inspect` command on the host

```
$ docker inspect host-volume

...
"Mounts": [
            {
                "Source": "/home/lukasz",
                "Destination": "/data",
                "Mode": "",
                "RW": true,
                "Propagation": "rprivate"
            }
        ],

...
```
# Local Persist Volume Plugin for Docker
## Installing & Running
Use provided an `install` script that will download the proper binary, set up an Systemd service to start when Docker does and enable it.
```
curl -fsSL https://raw.githubusercontent.com/CWSpear/local-persist/master/scripts/install.sh | sudo bash

```

To check if the volume plugin was installed corectly please execute the following command:

```
$ docker info

```
In response you should get:

```
Plugins: 
 Volume: local local-persist

```
## Creating Volumes

Then to use, you can create a volume with this plugin (this example will be for a shared folder for images):
```
$ docker volume create -d local-persist -o mountpoint=/data/images --name=images
```
Then if you create a container, you can connect it to this Volume:
```
$ docker run -dit -v images:/data --name test-local-persist busybox sh
```

Grant access to the mountpoint directory:

```
$ sudo chmod 777 /data/images
```

Create some file in the mountpoint directory:

```
$ echo "test" > /data/images/test.txt
```
Check if the file `test.txt` appears in the container.

```
$ docker exec test-local-persist cat /data/test.txt
test
```

