# Pacchetti (di Lamponi)

A Raspberry Pi Package Manager    
    
OK! ...    
These are my thoughts:    
    
So I was bored ... And I just wrote a GUI.    
Then I thought that Synaptic was too complicated for beginners ...    
Then I thought Add / Remove Software hardly has any programs ...   
Then I thought Gnome software was pretty cool ...    
    
# Note: This software is far from ready    
[x] Install/Uninstall worx!!!111    
[] Replace Dummies on Start Tab    
[x] Git&PPS test    
	- select Example_app    
	- click INstall    
	- Terminal shows: It is alive!    
	- if yes: success    
	- if not hmmmmm :-/    

Useage:
```
sudo apt-get install xterm -y    
sudo apt-get install python3-pil python3-pil.imagetk -y    
sudo apt install python3-pip -y    
```


```
$ python3 home/pi/PDL/PDL.py
```
    
Add your own apps:    
    
1.create a folder with "APP_NAME" in:    
    
~/PDL/essentals/

2. The folder must conain:    
	- install.sh [with the whole install parameters]    
	- uninstall.sh [with the whole uninstall parameters]    

3. Done


![GUI](https://github.com/actionschnitzel/PDL/blob/main/1.png)
![GUI](https://github.com/actionschnitzel/PDL/blob/main/2.png)
![GUI](https://github.com/actionschnitzel/PDL/blob/main/3.png)
