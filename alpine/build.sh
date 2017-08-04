#!/bin/sh

set -x

wget https://github.com/MrLYC/docker-utils/archive/master.zip
unzip master.zip
./docker-utils/entry.sh
