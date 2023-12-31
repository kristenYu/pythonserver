# py-simple-server

In terminal 1
```sh
$ python3 simple_server.py
launching server...
```

In terminal 2
```sh
# POST
$ curl -XPOST localhost:8000/ -d'{}'
...
# GET
$ curl localhost:8000/
...
```
