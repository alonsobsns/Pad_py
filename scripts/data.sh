#!/bin/bash

#echo $MY_SUDO_PASS | sudo -S;

echo "Atualizando Data."
if
   sed -i '10d' /etc/default/ntpdate; sed -i '10s/^/NTPSERVERS='ntp.pr.gov.br'\n/' /etc/default/ntpdate
    then
        echo "Data ajustada com sucesso."
    else
        echo "Nao foi possivel ajustar a data."
        exit 1
fi
