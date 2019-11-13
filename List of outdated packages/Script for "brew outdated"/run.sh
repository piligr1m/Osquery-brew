#!/usr/bin/env bash

 brew install docker
launchctl start docker

cd dumper
sudo docker build . -t dumper
sudo docker run -it dumper
