#!/bin/bash

set -e

n_peg=30

cp -r ../inputs/* .

newline='Number_polymer = '$n_peg
oldline=$(cat create-system.py | grep 'Number_polymer = ')
sed -i '/'"$oldline"'/c\'"$newline" create-system.py
python3 create-system.py
        
