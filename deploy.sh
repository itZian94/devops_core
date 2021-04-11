#!/bin/bash
scp -i ~/.ssh/id_rsa docker-compose.yaml jenkins@fundamental:home/jenkins/docker-compose.yaml
ssh -i ~/.ssh/id_rsa jenkins@fundamental <<EOF
    export DATABASE_URI=${DATABASE_URI}
    export SECRET_KEY=${SECRET_KEY}
    docker stack deploy --compose-file home/jenkins/docker-compose.yaml devops_core
EOF