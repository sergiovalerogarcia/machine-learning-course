#!/bin/bash

docker build --rm -t machine-learning-course/jupyter .

docker run -it --rm -p 8888:8888 \
  --name machine-learning-course-jupyter \
  -e JUPYTER_ENABLE_LAB=yes \
  -v "$( pwd | sed 's|^/mnt/c|c:|' )"/notebooks-library:/notebooks \
  --env-file .env.secrets \
  --env-file .env.properties \
  machine-learning-course/jupyter
