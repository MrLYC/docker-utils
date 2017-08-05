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

py.test -v tests/test_utils.py

if [ "${IAMGE_TYPE}" != "" ]; then
    py.test -v tests/test_utils_${IAMGE_TYPE}.py
fi