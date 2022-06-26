#!/usr/bin/env bash

docker run --ipc=host --gpus all --rm -it \
    -v $(pwd)/data:/data \
    ultralytics/yolov5:v6.1
