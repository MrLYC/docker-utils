#!/bin/sh

set -e

yum update
yum install -y epel-release
yum install -y wget ca-certificates unzip python python-pip

pip install pytest

wget https://github.com/MrLYC/docker-utils/archive/master.zip
unzip master.zip

${PROJECT_DIR}/test.sh
