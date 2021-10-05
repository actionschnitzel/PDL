# Pacchetti (di Lamponi)     
![GUI](https://github.com/actionschnitzel/tingsandstuff/blob/main/header_Y.png)


A Raspberry Pi Package Manager    
    
OK! ...    
These are my thoughts:    
    
So I was bored ... And I just wrote a GUI.    
Then I thought that Synaptic was too complicated for beginners ...    
Then I thought Add / Remove Software hardly has any programs ...   
Then I thought Gnome software was pretty cool ...    
    
You can now also save the installation instructions of your favorite Git repositories in a .sh file. PDL recognizes this file and you can start the installation with two clicks in the menu.    
    
#### Add your own apps:    
    
1.create a folder with "APP_NAME" in:    
```    
~/PDL/essentals/
```
2. The folder must conain:    
	- install.sh [with the whole install parameters]    
	- uninstall.sh [with the whole uninstall parameters]    
	
3. Done
    
Personally, it's always about setting up a new OS as quickly as possible. So one possible application is to copy PDL onto a USB flash drive and you always have immediate access to the installation parameters of your favorite programs.

    
# :warning: Note: This software is far from ready! The core functions are working. However, some content is still missing.    

### What already works:    
- Install/Uninstall    
- Git&PPA test    
	> select Example_app    
	> click INstall    
	> Terminal shows: It is alive!    
	> if yes: success    
	> if not hmmmmm :-/    
### What is still missing:    
- Installation Script
- Desktop File
- Working app buttons on Start tab


###Install:
```
git clone https://github.com/actionschnitzel/PDL.git
cd PDL
sudo chmod +x pdl_install.sh
sudo ./pdl_install.sh  
```

    


![GUI](https://github.com/actionschnitzel/PDL/blob/main/1.png)
![GUI](https://github.com/actionschnitzel/PDL/blob/main/2.png)
![GUI](https://github.com/actionschnitzel/PDL/blob/main/3.png)
