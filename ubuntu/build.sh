#!/bin/sh

set -x

apt-get update
apt-get install -y wget ca-certificates unzip python python-pip

pip install pytest

wget https://github.com/MrLYC/docker-utils/archive/master.zip
unzip master.zip

source ${PROJECT_DIR}/entry.sh
