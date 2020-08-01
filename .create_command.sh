#!/bin/bash

function create() {
    cd /home/quibbleahr/Documents/workspace/project-creator
    source .env
    source /home/quibbleahr/Documents/workspace/project-creator/env/bin/activate
    python3 create.py $1
    code /home/quibbleahr/Documents/workspace/$1
    deactivate
}