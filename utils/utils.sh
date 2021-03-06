#!/bin/sh

if [ "$DEBUG" = "debug" ]; then
    set -x
fi

utils_info() {
    echo "Docker shell utils by LYC"
}

# region functional

color_print() {
    export color_black=0
    export color_red=1
    export color_green=2
    export color_yellow=3
    export color_blue=4
    export color_purple=5
    export color_cyan=6
    export color_white=7

    export mode_fg=3
    export mode_bg=4

    export style_nothing=0
    export style_bold=1
    export style_underline=4

    content="$1"
    shift 1
    if [ "$#" != "0" ]; then
        export "$@"
    fi

    color=$(eval echo "\$color_${color:-yellow}")
    color_mode=$(eval echo "\$mode_${mode:-fg}")
    style=$(eval echo "\$style_${style:-nothing}")
    printf "\033[${style};${color_mode}${color}m${content}\033[0m"
}

path_join() {
    printf "${1%/}/${2#/}"
}

# end functional

# region filesystem

make_sure_dir_exists() {
	if [ -d "$1" ]; then
		return
	fi
	if [ -e "$1" ]; then
		rm "$1"
	fi
	mkdir -p "$1"
}

make_sure_parent_dir_exists() {
    make_sure_dir_exists $(dirname "$1")
}

make_sure_not_exists() {
	if [ ! -e "$1" ]; then
		return
	fi
	rm -rf "$1"
}

# end filesystem

# region file

is_str_in_file() {
    if [ "$1" = "" ]; then
        return 1
    fi
    grep -Fq "$1" "$2"
}

is_line_in_file() {
    if [ "$1" = "" ]; then
        return 1
    fi
    grep -Fxq "$1" "$2"
}

append_line_once() {
    if is_line_in_file "$1" "$2"; then
        echo "skip"
    else
        echo "$1" >> "$2"
        echo "ok"
    fi
}

# end

if [ "$#" != 0 ]; then
    cmd="$1"
    shift 1
    $cmd "$@"
fi
