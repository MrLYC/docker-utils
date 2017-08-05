#!/bin/sh

date
CUR_DIR=`pwd`
PROJECT_DIR=${PROJECT_DIR:-${CUR_DIR}}
cd ${PROJECT_DIR}
./utils/utils.sh utils_info

onexit() {
    rm -rf tmp
}
trap onexit EXIT

mkdir tmp

env PYTHON=${CUR_DIR} python -m unittest tests.test_utils

if [ "${IAMGE_TYPE}" != "" ]; then
    env PYTHON=${CUR_DIR} python -m unittest tests.test_utils_${IAMGE_TYPE}
fi