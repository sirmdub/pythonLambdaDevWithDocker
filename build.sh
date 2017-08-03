#!/bin/bash

docker build -t pldwd:build .
docker build -t pldwd:deploy . -f Dockerfile.deploy

cd tests/
docker build -t pldwd:test .
