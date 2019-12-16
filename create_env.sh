#!/bin/bash

if [[ ! -d ./env ]]
then
    conda env create --prefix ./env --file environment.yml
else
    conda env update --prefix ./env --file environment.yml  --prune
fi

if [[ "$?" -eq "0" ]]
then
    echo 'Actually activate Python environment with:'
    echo '    conda activate ./env'
fi
