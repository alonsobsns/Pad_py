#!/bin/bash

#echo $MY_SUDO_PASS | sudo -S;

echo "Atualizando repositórios.."
if ! apt-get update -y
    then
        echo "Não foi possível atualizar os repositórios. Verifique seu arquivo /etc/apt/sources.list"
        exit 1
fi
    echo "Atualização feita com sucesso"

    echo "Atualizando pacotes já instalados"
if ! apt-get upgrade -y
    then
        echo Não foi possível atualizar pacotes.
        exit 1
fi

if ! apt autoremove -y
    then
        echo Não foi possível atualizar pacotes.
        exit 1
fi
