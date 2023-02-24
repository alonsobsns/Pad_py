#!/bin/bash

#echo $MY_SUDO_PASS | sudo -S;

nome_inter=$(ip -br link|awk '$2 ~ /UP/ {print $1}' | grep e)

echo "Atualizando conky."
if
   sed -i "s/rede_local/"$nome_inter"/g" /etc/conky/conky.conf
    then
        echo "Instalacao efetuada com sucesso."
    else
        echo "Nao foi possivel efetuar a instalacao."
        exit 1
fi
