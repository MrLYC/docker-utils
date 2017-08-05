#!/bin/sh

set -x

apk update
apk add wget ca-certificates unzip python py-pip

pip install pytest

wget https://github.com/MrLYC/docker-utils/archive/master.zip
unzip master.zip

${PROJECT_DIR}/entry.sh
