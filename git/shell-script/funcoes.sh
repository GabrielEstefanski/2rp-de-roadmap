#!/bin/bash


lista_arquivos(){
	cd C:/Users/Gabriel/Desktop/diretorio/
	x="ls -R $PWD/*"
	for i in $x 
	do
	echo $i
	done
}

insere_texto(){
	var=$1
	cd C:/Users/Gabriel/Desktop/diretorio/
	echo $var>Arquivo.txt
}




	



