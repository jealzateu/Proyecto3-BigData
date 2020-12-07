#!/bin/bash
export PYSPARK_PYTHON=python3
sudo python3 -m pip install numpy --upgrade --ignore-installed
sudo python3 -m pip install \
    botocore \
    boto3 \
    ujson \
    warcio \
    beautifulsoup4  \
    lxml \
    matplotlib==3.0.0
