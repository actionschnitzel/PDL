echo "
██████╗ ██████╗ ██╗     
██╔══██╗██╔══██╗██║     
██████╔╝██║  ██║██║     
██╔═══╝ ██║  ██║██║     
██║     ██████╔╝███████╗
╚═╝     ╚═════╝ ╚══════╝
                        
"
echo "A Raspberry Pi Package Manager"

read -p "You are about to install PDL ...... Agree (y/n)? " option
case "$option" in
	y*) sudo apt-get update ;;
	n*) exit ;;
esac

clear

echo 'Now I install dependencies'

sudo apt-get install xterm -y
sudo apt-get install python3-pil python3-pil.imagetk -y
sudo apt install python3-pip -y

clear

sudo chmod +x start.sh
sudo cp PDL.desktop  /home/pi/Desktop
sudo cp PDL.desktop /usr/share/applications/
sudo chmod +x /home/pi/Desktop/PDL.desktop

clear

echo "
██████╗ ██████╗ ██╗     
██╔══██╗██╔══██╗██║     
██████╔╝██║  ██║██║     
██╔═══╝ ██║  ██║██║     
██║     ██████╔╝███████╗
╚═╝     ╚═════╝ ╚══════╝
                        
"

echo  '
 ____ ____ ____ ____ _________ ____ 
||D |||O |||N |||E |||       |||! ||
||__|||__|||__|||__|||_______|||__||
|/__\|/__\|/__\|/__\|/_______\|/__\|'

printf '\e[38;5;46m You can close this window now\n'

