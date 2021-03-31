#!/bin/bash

jt -t onedork -T -N
jupyter notebook --port=8888 --no-browser --ip=0.0.0.0 --config=.config/jupyter_notebook_config.py