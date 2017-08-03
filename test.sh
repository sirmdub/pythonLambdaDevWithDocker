#!/bin/bash

docker run --name some-redis -d redis
docker run --link some-redis:redis -it pldwd:test
docker stop some-redis
docker rm some-redis
