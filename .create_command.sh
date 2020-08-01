#!/bin/bash

function create() {
    cd /home/quibbleahr/Documents/workspace/automate-create-project
    source .env
    source /home/quibbleahr/Documents/workspace/automate-create-project/env/bin/activate
    python3 create.py $1
    code .
    deactivate
}