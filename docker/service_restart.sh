#!/bin/bash

docker swarm init --advertise-addr 192.168.1.110
docker stack deploy --compose-file docker-compose.yml encaminhador
