FROM alpine

MAINTAINER lyc <imyikong@gmail.com>

ADD build.sh /build.sh
ENV DOCKER_DEBUG 0

WORKDIR /
RUN ["/build.sh"]

ENTRYPOINT ["/docker-utils/entry.sh"]
