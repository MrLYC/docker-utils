#!/bin/sh

set -x

apk update
apk add wget ca-certificates unzip

wget https://github.com/MrLYC/docker-utils/archive/master.zip
unzip master.zip
./docker-utils/entry.sh
