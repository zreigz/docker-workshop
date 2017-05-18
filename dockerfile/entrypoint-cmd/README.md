# ENTRYPOINT & CMD
Exec form of ENTRYPOINT allows you to set commands and parameters and then use either form of CMD to set additional parameters that are more likely to be changed. ENTRYPOINT arguments are always used, while CMD ones can be overwritten by command line arguments provided when Docker container runs. For example, the following snippet in Dockerfile 


```
ENTRYPOINT ["/bin/echo", "Hello"]  
CMD ["world"]  
```

## Build image

```
$ docker build -t hello .
```

## Run container

When container runs as `docker run -it <image>` will produce output 

```
Hello world 
```
but when container runs as 'docker run -it <image> John' will result in

```
Hello John
``` 

