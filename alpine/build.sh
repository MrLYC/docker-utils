#!/bin/sh

set -x

apk update
apk add wget ca-certificates unzip python

wget https://github.com/MrLYC/docker-utils/archive/master.zip
unzip master.zip

source ${PROJECT_DIR}/entry.sh
