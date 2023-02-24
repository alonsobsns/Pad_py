#!/bin/bash

#echo $MY_SUDO_PASS | sudo -S;

echo "Instalando Modulo de Bancos."
if
   apt-get install cliente-ldap -y;
    then
        echo "Instalacao efetuada com sucesso."
    else
        echo "Nao foi possivel efetuar a instalacao."
        exit 1
fi
