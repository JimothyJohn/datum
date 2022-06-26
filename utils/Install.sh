#!/usr/bin/env bash

docker pull ultralytics/yolov5:v6.1
docker-compose -f .devcontainer/docker-compose.yml build
