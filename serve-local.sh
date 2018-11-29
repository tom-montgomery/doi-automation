#!/usr/bin/env bash

echo "starting..."

set -o errexit

TAG='doi-automation:latest'
echo "building docker image..."
docker build --tag "$TAG" .
echo "running docker image..."

docker run \
  --rm \
  -it \
  --name doi-automation \
  -p 5000:5000 \
  -v `pwd`:/app \
  doi-automation \
  python app/app.py
