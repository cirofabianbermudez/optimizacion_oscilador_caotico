#! /bin/bash
# Autor: Ciro Fabian Bermudez Marquez
# 02.02.2021

for (( i=1; i<=100; i+=1))
do
	python3 corre.py
done > datos70.txt

( speaker-test -t sine -f 1000 )& pid=$! ; sleep 1s ; kill -9 $pid
