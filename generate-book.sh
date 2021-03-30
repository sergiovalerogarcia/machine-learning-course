#!/bin/bash

#echo "html:" >> _config.yml
#echo "  google_analytics_id: ${GOOGLE_ANALYTICS_KEY}" >> _config.yml

jupyter-book toc notebooks/

jupyter-book build notebooks/
