FROM centos

MAINTAINER lyc <imyikong@gmail.com>

ADD build.sh /build.sh
ENV DOCKER_DEBUG 0
ENV IMAGE_TYPE "centos"
ENV PROJECT_DIR "/docker-utils-master"

WORKDIR /
RUN ["/build.sh"]

ENTRYPOINT ["/docker-utils-master/test.sh"]
