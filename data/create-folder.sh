#!/bin/bash

set -e

for n_peg in 22
do

    folder=nb_peg_${n_peg}/
    if [ ! -d "$folder" ];
    then
        mkdir $folder
        cd $folder
            cp -r ../../inputs/* .
            newline='Number_polymer = '$n_peg
            oldline=$(cat create-system.py | grep 'Number_polymer = ')
            sed -i '/'"$oldline"'/c\'"$newline" create-system.py
            python3 create-system.py
        cd ..
    else
        echo 'Folder '${folder}'exist already, skipped'
    fi
done
