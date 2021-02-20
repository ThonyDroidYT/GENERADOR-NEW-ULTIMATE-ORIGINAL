#!/bin/bash
clear
#--- 20/01/2021

####------- REINICIAR UPDATER Y RECONFIGURAR HORARIO
Link="https://raw.githubusercontent.com/ThonyDroidYT/TD-Gen/master/MultiGen/VPS-MX-8.3/zzupdate.sh"
Link1="https://raw.githubusercontent.com/ThonyDroidYT"
Link2="TD-Gen/master/MultiGen/VPS-MX-8.3/zzupdate.sh"
killall apt apt-get > /dev/null 2>&1
dpkg --configure -a > /dev/null 2>&1
apt-get install software-properties-common -y > /dev/null 2>&1
apt-add-repository universe -y > /dev/null 2>&1
rm -rf /etc/localtime &>/dev/null
ln -s /usr/share/zoneinfo/America/Mexico_City /etc/localtime &>/dev/null
rm $(pwd)/$0 &> /dev/null

#------- COLORES Y BARRA 

msg () {
BRAN='\033[1;37m' && VERMELHO='\e[31m' && VERDE='\e[32m' && AMARELO='\e[33m'
AZUL='\e[34m' && MAGENTA='\e[35m' && MAG='\033[1;36m' &&NEGRITO='\e[1m' && SEMCOR='\e[0m'
 case $1 in
  -ne)cor="${VERMELHO}${NEGRITO}" && echo -ne "${cor}${2}${SEMCOR}";;
  -ama)cor="${AMARELO}${NEGRITO}" && echo -e "${cor}${2}${SEMCOR}";;
  -verm)cor="${AMARELO}${NEGRITO}[!] ${VERMELHO}" && echo -e "${cor}${2}${SEMCOR}";;
  -azu)cor="${MAG}${NEGRITO}" && echo -e "${cor}${2}${SEMCOR}";;
  -verd)cor="${VERDE}${NEGRITO}" && echo -e "${cor}${2}${SEMCOR}";;
  -bra)cor="${VERMELHO}" && echo -ne "${cor}${2}${SEMCOR}";;
  "-bar2"|"-bar")cor="${VERMELHO}————————————————————————————————————————————————————" && echo -e "${SEMCOR}${cor}${SEMCOR}";;
 esac
}
clear
 msg -bar2
 msg -ama "     [ VPS - MX - SCRIPT \033[1;97m ❌ MOD By @Kalix1 ❌\033[1;33m ]"
 echo -e  "\033[1;97m               EJECUTANDO ACTULIZADOR  \033[1;34m "
 msg -bar2
## Script name
SCRIPT_NAME=vpsmxup
## Install directory
WORKING_DIR_ORIGINAL="$(pwd)"
INSTALL_DIR_PARENT="/usr/local/vpsmxup/"
INSTALL_DIR=${INSTALL_DIR_PARENT}${SCRIPT_NAME}/
## /etc/ config directory
mkdir -p "/etc/vpsmxup/"
## Install/update
if [ ! -d "$INSTALL_DIR" ]; then
	echo -e  "\033[1;97m           Instalando Paquetes Prioritarios"
	echo "           --------------------------------"
	sleep 2
	mkdir -p "$INSTALL_DIR_PARENT"
	cd "$INSTALL_DIR_PARENT"
    wget https://www.dropbox.com/s/k5e2b49dvgsgmjn/zzupdate.default.conf -O /usr/local/vpsmxup/vpsmxup.default.conf  &> /dev/null
	#chmod +x /usr/local/vpsmxup/vpsmxup.default.conf 
	rm -rf /usr/local/vpsmxup/vpsmxup.sh
    #wget https://www.dropbox.com/s/vza024sag3v2y83/zzupdate.sh -O /usr/local/vpsmxup/vpsmxup.sh &> /dev/null
     wget $Link -O /usr/local/vpsmxup/vpsmxup.sh &> /dev/null
	chmod +x /usr/local/vpsmxup/vpsmxup.sh
	rm -rf /usr/bin/vpsmxup
    #wget https://www.dropbox.com/s/vza024sag3v2y83/zzupdate.sh -O /usr/bin/vpsmxup &> /dev/null
     wget $Link -O /usr/bin/vpsmxup &> /dev/null
	chmod +x /usr/bin/vpsmxup
	echo -e  "\033[1;97m              Copiando Instalador Interno "
	
	echo "           --------------------------------"	
	msg -bar2
	sleep 2
else
	echo ""
fi
sleep 5
## Restore working directory
cd $WORKING_DIR_ORIGINAL
clear
vpsmxup
