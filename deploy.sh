#!/bin/bash

source aws_secrets.txt
docker run -e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY -e AWS_DEFAULT_REGION pldwd:deploy
