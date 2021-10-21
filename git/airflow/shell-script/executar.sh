#!/bin/bash

source $(dirname $0)/funcoes.sh

declare -a my_array

lista_arquivos $1 my_array
for i in $(seq 1 ${#my_array[@]})
        do
                insere_texto $2 ${my_array[i-1]}
        done

