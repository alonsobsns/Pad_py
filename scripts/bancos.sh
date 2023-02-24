#!/bin/bash

#echo $MY_SUDO_PASS | sudo -S;

echo "Instalando Modulo de Bancos"
if
   apt-get install bancos -y;
   apt-get install proxy-parana -y;
    then
        echo "Instalacao efetuada com sucesso."
    else
        echo "Nao foi possivel efetuar a instalacao."
        exit 1
fi
