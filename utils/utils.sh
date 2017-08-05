#!/bin/sh

utils_info() {
    echo "Docker shell utils by LYC"
}

make_sure_dir_exists() {
	if [ -d "$1" ]; then
		return
	fi
	if [ -e "$1" ]; then
		rm "$1"
	fi
	mkdir -p "$1"
}

make_sure_not_exists() {
	if [ ! -e "$1" ]; then
		return
	fi
	rm -rf "$1"
}

if [ "$#" != 0 ]; then
    cmd="$1"
    shift 1
    $cmd $@
fi
