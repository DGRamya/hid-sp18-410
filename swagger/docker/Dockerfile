FROM ubuntu:16.04
#FROM python:3-alpine 
MAINTAINER Karan Kamatgi <krkamatg@iu.edu>

RUN apt-get update -q && apt-get install -qy \
    build-essential \
    python-dev \
    python-pip \
    #libssl-dev \
    zlib1g-dev \
    #libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    #pandoc \
    wget \
    curl \
    #emacs \
    git-core \
    default-jre \
    software-properties-common -y

#RUN apt-get update -q && apt-get install -qy default-jre 




RUN git clone https://github.com/cloudmesh-community/hid-sp18-410.git

WORKDIR /hid-sp18-410/doc-swag

RUN wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar

EXPOSE 8080

#FROM openjdk:7 
RUN make service

CMD ["make", "start"]
