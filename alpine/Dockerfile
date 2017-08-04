FROM alpine

MAINTAINER lyc <imyikong@gmail.com>

ADD build.sh /build.sh
ENV DOCKER_DEBUG 0
ENV PROJECT_DIR "/docker-utils-master"

WORKDIR /
RUN ["/build.sh"]

ENTRYPOINT ["/docker-utils-master/entry.sh"]
