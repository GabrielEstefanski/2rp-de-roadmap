  GNU nano 2.3.1              File: funcoes.sh

#!/bin/bash


lista_arquivos(){
        my_array=('find $1 -type f')
}

insere_texto(){
        echo "$1" >> "$2"
}


