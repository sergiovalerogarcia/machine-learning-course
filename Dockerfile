FROM python:3.7-slim-buster
LABEL maintainer="svalero"

# Postgres/Redshift connection
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    postgresql \
    python-psycopg2 \
    libpq-dev \
    python3-dev \
    gcc \
    texlive \
    texlive-latex-extra \
    texlive-xetex \
    texlive-generic-extra \
    pandoc \
    build-essential libsasl2-dev libsasl2-2 libsasl2-modules-gssapi-mit \
    bash-completion \
    ssh \
    git

RUN pip3 install --upgrade pip && \
    pip3 install jupyterlab && \
    pip3 install notebook && \
    pip3 install pandas && \
    pip3 install SQLAlchemy && \
    pip3 install psycopg2 && \
    pip3 install matplotlib && \
    pip3 install nb2xls

## Add ipython-sql and PyHive
RUN pip install ipython-sql && \
    pip3 install sasl && \
    pip3 install thrift && \
    pip3 install thrift-sasl && \
    pip3 install PyHive

RUN pip install jupyter_contrib_nbextensions && \
    pip install https://github.com/ipython-contrib/jupyter_contrib_nbextensions/tarball/master && \
    pip install jupyter_nbextensions_configurator && \
    jupyter contrib nbextension install

RUN pip install jupytext && \ 
    pip install -U jupyter-book

RUN pip install scikit-learn && \
    pip install tensorflow
    
RUN pip install xlrd && \
    pip install jupyterthemes

RUN pip install statsmodels

RUN useradd -ms /bin/bash jupyuser

USER jupyuser

RUN jupyter nbextensions_configurator enable && \
    jupyter nbextension enable execute_time/ExecuteTime && \
    jupyter nbextension enable toc2/main

COPY ./run-jupyter.sh /entrypoint.sh

WORKDIR /notebooks
CMD ["/entrypoint.sh"]