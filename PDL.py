
import os
import tkinter as tk
import webbrowser
from os import popen
from os import system as cmd
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import platform
import psutil
from collections import namedtuple
import resource
import threading
from datetime import datetime
import distro

#popen("apt-cache pkgnames > /home/timo/PiGro-Aid-/essentials/SomeFile.txt")

os.system("xterm -e 'bash -c \"apt-cache pkgnames > ~/PDL/essentials/SomeFile.txt && exit; exec bash\"'")

os.system("dpkg --get-selections > ~/PDL/essentials/packages.list")
#os.system("sed -e s/install//g -i /home/timo/PiGro-Aid-/essentials/packages.list")
os.system("xterm -e 'bash -c \"sed -e s/install//g -i ~/PDL/essentials/packages.list && exit; exec bash\"'")

os.system("xterm -e 'bash -c \"cd ~/PDL/essentials/ && ls -d */ | cut -f1 -d'/' > apps.txt && exit; exec bash\"'")

os.system("find ~/PDL/essentials -type f -exec chmod +x {} \;")








main = Tk()
main.title("PDL (Pacchetti di Lamponi) v. ALPHA 0.00001 --Standalone-Version--")
icon = tk.PhotoImage(file="icons/PiGroLogoslim.png")
main.tk.call('wm', 'iconphoto', main._w, icon)
#main['background'] = '#191925'
main.resizable(0, 0)


app_width = 850
app_height = 650

screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

main.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

main.wait_visibility(main)
main.wm_attributes('-alpha', 0.95, )


###########################################TABCONT
#Notebook Style
noteStyler = ttk.Style()
noteStyler.configure("TNotebook", borderwidth=0, tabposition='nw',highlightthickness=0, background="#191925") #
noteStyler.configure("TNotebook.Tab", borderwidth=0, foreground="white",font=("Helvetica",12),highlightthickness=0, background="#191925",side="LEFT") #
noteStyler.configure("TFrame", background="#191925") #


noteStyler.map("TNotebook.Tab", background=[("selected", "#191925")], foreground=[("selected", "#d4244d")]);

tab_control = ttk.Notebook(main)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

tab_ip25 = Image.open('icons/system.png')
ip25 = ImageTk.PhotoImage(tab_ip25)
il25 = Label(image=ip25)

tab_ip26 = Image.open('icons/github.png')
ip26 = ImageTk.PhotoImage(tab_ip26)
il26 = Label(image=ip26)

tab_ip27 = Image.open('icons/apt.png')
ip27 = ImageTk.PhotoImage(tab_ip27)
il27 = Label(image=ip27)

tab_ip28 = Image.open('icons/install_btn.png')
ip28 = ImageTk.PhotoImage(tab_ip28)
il28 = Label(image=ip28)

tab_ip29 = Image.open('icons/uninstall_btn.png')
ip29 = ImageTk.PhotoImage(tab_ip29)
il29 = Label(image=ip29)
########################
tab_control.add(tab1, compound=LEFT,image=ip25)
tab_control.add(tab2, compound=LEFT,image=ip27)
tab_control.add(tab3, compound=LEFT,image=ip26)
#####################################################################################################
#apps
def btop_plusplus():
    global bt_pp
    bt_pp=Toplevel()
    bt_pp['background'] = '#191925'
      
    logo = Label(bt_pp, image=ip03, text="btop++",font=("Helvetica",16), anchor="w",
                  highlightthickness=0, borderwidth=0, background='#191925', foreground="white", compound=TOP).grid(column=0, row=0)
    
    bt_inst = Button(bt_pp, text="Install",font=("Helvetica",11,"bold"),justify="left", anchor="w",
                     highlightthickness=0, borderwidth=0, background='#191925', foreground="white", compound=LEFT).grid(column=0, row=1)
    
    bt_uninst = Button(bt_pp, text="Uninstall",font=("Helvetica",11,"bold"), anchor="w",
                  highlightthickness=0, borderwidth=0, background='#191925', foreground="white", compound=LEFT,justify="left").grid(column=0, row=2)
    
    bt_info = Label(bt_pp, text="Resource monitor that shows usage and stats for\nprocessor,memory, disks, network and processes.",justify="left", anchor="w",
                  highlightthickness=0, borderwidth=0, background='#191925', foreground="white", compound=TOP).grid(column=1, row=0)
    
    bt_pic = Label(bt_pp,image=ip24, anchor="w",
                  highlightthickness=0, borderwidth=0, background='#191925', foreground="white", compound=TOP).grid(column=1, row=1,rowspan=12,pady=10)
    
def argon_one():
    global ar
    ar=Toplevel()
    ar['background'] = '#191925'
      
    logo = Label(ar, image=ip20, text="Argon One Driver",font=("Helvetica",16), anchor="w",
                  highlightthickness=0, borderwidth=0, background='#191925', foreground="white", compound=TOP).grid(column=0, row=0)
    
    ao_inst = Button(ar, text="Install",font=("Helvetica",11,"bold"),justify="left", anchor="w",
                     highlightthickness=0, borderwidth=0, background='#191925', foreground="white", compound=LEFT).grid(column=0, row=1)
    
    ao_uninst = Button(ar, text="Uninstall",font=("Helvetica",11,"bold"), anchor="w",
                  highlightthickness=0, borderwidth=0, background='#191925', foreground="white", compound=LEFT,justify="left").grid(column=0, row=2)
    
    ao_info = Label(ar, text="Driver for the Argon One Case.Including fan control.\nCommand: argonone-config",justify="left", anchor="w",
                  highlightthickness=0, borderwidth=0, background='#191925', foreground="white", compound=TOP).grid(column=1, row=0)
    
    ao_pic = Label(ar,image=ip24, anchor="w",
                  highlightthickness=0, borderwidth=0, background='#191925', foreground="white", compound=TOP).grid(column=1, row=1,rowspan=12,pady=10)
    
def desk_pi():
    global dp
    dp=Toplevel()
    dp['background'] = '#191925'
      
    logo = Label(dp, image=ip05, text="Deskpi Pro Driver",font=("Helvetica",16), anchor="w",
                  highlightthickness=0, borderwidth=0, background='#191925', foreground="white", compound=TOP).grid(column=0, row=0)
    
    dp_inst = Button(dp, text="Install",font=("Helvetica",11,"bold"),justify="left", anchor="w",
                     highlightthickness=0, borderwidth=0, background='#191925', foreground="white", compound=LEFT).grid(column=0, row=1)
    
    dp_uninst = Button(dp, text="Uninstall",font=("Helvetica",11,"bold"), anchor="w",
                  highlightthickness=0, borderwidth=0, background='#191925', foreground="white", compound=LEFT,justify="left").grid(column=0, row=2)
    
    dp_info = Label(dp, text="Driver for the Deskpi Pro Case.Including fan control.\nCommand: argonone-config",justify="left", anchor="w",
                  highlightthickness=0, borderwidth=0, background='#191925', foreground="white", compound=TOP).grid(column=1, row=0)
    
    dp_pic = Label(dp,image=ip24, anchor="w",
                  highlightthickness=0, borderwidth=0, background='#191925', foreground="white", compound=TOP).grid(column=1, row=1,rowspan=12,pady=10)   

def pop_pikiss():
    global pikiss
    pikiss=Toplevel()
    
      
    logo = Label(pikiss, image=ip13, text="PiKiss",font=("Helvetica",16), anchor="w",
                  highlightthickness=0, borderwidth=0, background='#191925', foreground="white", compound=TOP).grid(column=0, row=0)
    
    pk_inst = Button(pikiss, text="Install", anchor="w",
                  highlightthickness=0, borderwidth=0, background='#191925', foreground="white", compound=LEFT).grid(column=0, row=1)
    
    pk_uninst = Button(pikiss, text="Uninstall", anchor="w",
                  highlightthickness=0, borderwidth=0, background='#191925', foreground="white", compound=LEFT).grid(column=0, row=2)
    
    pk_info = Label(pikiss,justify="left", text="Installing an application on Linux is not a complex task.\nSometimes you just type sudo apt install and get\nthe application installed with all of its dependencies.\nBut... What if we need to install more than one app\nsuch as a web server or it requires many steps to complete\nthe install process? Is it not in the\nofficial repositories?",
                  highlightthickness=0, borderwidth=0, background='#191925', foreground="white", compound=TOP).grid(column=1, row=0,rowspan=2)




    
def inst_inf1():
    messagebox.showinfo("You called for help?", "The list contains all available packages. Yes, even the ones you added yourself! You can either search with the mouse wheel or type the desired package into the search bar. Click on the desired packet and press install.")

def inst_inf2():
    messagebox.showinfo("What is it?", "The list contains all installed packages. ALL! You can either search with the mouse wheel or type the desired package into the search bar. Click on the desired packet and press uninstall.")

def inst_inf3():
    messagebox.showinfo("What is it?", "The list contains Git & PPA projects! Click on the desired packet and press install/uninstall.")
    

#######
##############################################################################################
tab_tp1 = Image.open('icons/Essentials.png')
tp01 = ImageTk.PhotoImage(tab_tp1)
tl01 = Label(image=tp01)



############################################################################################IMAGES
tab_ip1 = Image.open('essentials/Albert/albert-icon.png')
ip01 = ImageTk.PhotoImage(tab_ip1)
il01 = Label(image=ip01)

tab_ip3 = Image.open('essentials/btop++/logo.png')
ip03 = ImageTk.PhotoImage(tab_ip3)
il03 = Label(image=ip03)

tab_ip5 = Image.open('essentials/DeskPi_Pro_Driver/DeskpiPro_icon.png')
ip05 = ImageTk.PhotoImage(tab_ip5)
il05 = Label(image=ip05)

tab_ip6 = Image.open('essentials/FanShim_Driver/shim_icon.png')
ip06 = ImageTk.PhotoImage(tab_ip6)
il06 = Label(image=ip06)

tab_ip11 = Image.open('essentials/Pi-Apps/proglogo.png')
ip11 = ImageTk.PhotoImage(tab_ip11)
il11 = Label(image=ip11)

tab_ip13 = Image.open('essentials/PiKiss/logo_pikiss_header.png')
ip13 = ImageTk.PhotoImage(tab_ip13)
il13 = Label(image=ip13)

tab_ip17 = Image.open('essentials/Tetris-CLI/tetris.png')
ip17 = ImageTk.PhotoImage(tab_ip17)
il17 = Label(image=ip17)

tab_ip20 = Image.open('essentials/Argon_One_Driver/argon_icon.png')
ip20 = ImageTk.PhotoImage(tab_ip20)
il20 = Label(image=ip20)

tab_ip21 = Image.open('icons/info_button.png')
ip21 = ImageTk.PhotoImage(tab_ip21)
il21 = Label(image=ip21)

tab_ip22 = Image.open('essentials/Sublime_Text/sublime_text.png')
ip22 = ImageTk.PhotoImage(tab_ip22)
il22 = Label(image=ip22)

tab_ip23 = Image.open('essentials/Sublime_Merge/sublime_merge.png')
ip23 = ImageTk.PhotoImage(tab_ip23)
il23 = Label(image=ip23)

tab_ip24 = Image.open('essentials/btop++/btop.png')
ip24 = ImageTk.PhotoImage(tab_ip24)
il24 = Label(image=ip24)


#####################################################################TAB1
ess_lbl = Label(tab1, image=tp01, borderwidth=0, background='#191925',highlightthickness=0)
#ess_lbl.place(x=13,y=50)
ess_lbl.pack(pady=50)

Sugg = Label(tab1, width=105, text="Developer's choice:",font=("Helvetica",16), anchor="w",
                  highlightthickness=0, borderwidth=0, background='#191925', foreground="white").pack()

ess_frame = Frame(tab1, borderwidth=0, background='#191925',highlightthickness=0)
#ess_frame.place(x=3,y=250)
ess_frame.pack(pady=20)


shop_btn01 = Button(ess_frame, width=105, image=ip03, text="btop++", anchor="n", highlightthickness=0,
                  borderwidth=0, foreground="white", compound=TOP,font=("Helvetica",11,"bold"),command=btop_plusplus, background='#191925').grid(column=0, row=0,pady=5, padx=5)

shop_btn01 = Button(ess_frame, width=105, image=ip20, text="Argon One Driver", anchor="n", highlightthickness=0,
                  borderwidth=0, foreground="white", compound=TOP,font=("Helvetica",11,"bold"),command=argon_one, background='#191925').grid(column=1, row=0,pady=5, padx=5)

shop_btn03 = Button(ess_frame, width=105, image=ip05, text="DeskPi Pro Driver", anchor="n", highlightthickness=0,
                  borderwidth=0, foreground="white", compound=TOP,font=("Helvetica",11,"bold"),command=desk_pi, background='#191925').grid(column=2, row=0,pady=5, padx=5)

shop_btn04 = Button(ess_frame, width=105, image=ip06, text="FanShim Driver", anchor="n", highlightthickness=0,
                  borderwidth=0, foreground="white", compound=TOP,font=("Helvetica",11,"bold"), background='#191925').grid(column=3, row=0,pady=5, padx=5)

shop_btn05 = Button(ess_frame, width=105, image=ip13, text="PiKiss", anchor="n", highlightthickness=0,
                  borderwidth=0, foreground="white", compound=TOP,font=("Helvetica",11,"bold"), background='#191925',command=pop_pikiss).grid(column=4, row=0,pady=5, padx=5)

shop_btn06 = Button(ess_frame, width=105, image=ip11, text="Pi-Apps", anchor="n", highlightthickness=0,
                  borderwidth=0, foreground="white", compound=TOP,font=("Helvetica",11,"bold"), background='#191925').grid(column=0, row=1,pady=0, padx=5)

shop_btn07 = Button(ess_frame, width=105, image=ip17, text="Tetris-CLI", anchor="n", highlightthickness=0,
                  borderwidth=0, foreground="white", compound=TOP,font=("Helvetica",11,"bold"), background='#191925').grid(column=1, row=1,pady=1, padx=5)

shop_btn08 = Button(ess_frame, width=105, image=ip01, text="Albert", anchor="n", highlightthickness=0,
                  borderwidth=0, foreground="white", compound=TOP,font=("Helvetica",11,"bold"), background='#191925').grid(column=2, row=1,pady=2, padx=5)

shop_btn09 = Button(ess_frame, width=105, image=ip23, text="Sublime Merge 64 Bit", anchor="n", highlightthickness=0,
                  borderwidth=0, foreground="white", compound=TOP,font=("Helvetica",9,"bold"), background='#191925').grid(column=3, row=1,pady=2, padx=5)

shop_btn10 = Button(ess_frame, width=105, image=ip22, text="Sublime Text 64 Bit", anchor="n", highlightthickness=0,
                  borderwidth=0, foreground="white", compound=TOP,font=("Helvetica",9,"bold"), background='#191925').grid(column=4, row=1,pady=2, padx=5)

#####################################################################################################TAB2
# i = Image.open('icons/pigro_bg.png')
# p = ImageTk.PhotoImage(i)
# l = Label(tab2, image=p)
# l.image = p
# l['background'] = '#191925'
# l.place(x=0, y=10)

inst0_frame = Frame(tab2, borderwidth=0, background='#191925',highlightthickness=0)
#ess_frame.place(x=3,y=250)
inst0_frame.pack(anchor="nw",pady=10)



inst1_frame = Frame(tab2, borderwidth=0, background='#191925',highlightthickness=0,padx=10,pady=10)
#ess_frame.place(x=3,y=250)
inst1_frame.pack(anchor="n")

info_inst0= Button(inst1_frame, image=ip21,anchor="n",
                  highlightthickness=0, borderwidth=0, background='#191925',command=inst_inf1).grid(row=1,rowspan=1,column=0)



inst1_p1=""" xterm -e 'bash -c \"sudo apt install """
inst1_p2="""; exec bash\"' """


def inst_btn1():
    entry_text = my_entry.get()
    popen(inst1_p1 + entry_text + inst1_p2)
    defstdout = sys.stdout


# Update the listbox

def update(data):
    # Clear the listbox
    my_list.delete(0, END)

    # Add toppings to listbox
    for item in data:
        my_list.insert(END, item)

# Update entry box with listbox clicked
def fillout(event):
    # Delete wot is in  Box
    my_entry.delete(0,END)    
    # Add clicked list item to enty box  
    my_entry.insert(0, my_list.get(ACTIVE))


# Checkfunktion Entry vs. List

def check(event):
    # grad inserted
    typed = my_entry.get()
    
    if typed == '':
        data = content
    else:
        data = []
        for item in content:
            if typed.lower() in item.lower():
                data.append(item)
                
    #updates listbox with selected item
    update(data)
                

fo = open("essentials/SomeFile.txt", "r")
content = fo.readlines()
print (content)


#my_label = Label(tab2, text="Start Typing",
#    font=("Helvetica",14), fg="grey")
#my_label.pack(pady=20)


inst_btn = Button(inst1_frame,image=ip28, command=inst_btn1, highlightthickness=0, borderwidth=0,
                        background='#191925', foreground="white",font=(("Helvetica,bold"),"12"))        

inst_btn.grid(row=0, column=0)


# Create an entry box

my_entry = Entry(inst1_frame,font=("Helvetica",12), width=60)
my_entry.grid(row=0, column=1)

my_list = Listbox(inst1_frame, width=67)
my_list.grid(row=1, column=1,padx=10)

fo = open("essentials/SomeFile.txt","r")
content = fo.readlines()
for i,s in enumerate(content):
    content[i] = s.strip()
print (content)

# Add toppings

update(content)


#Create binding

my_list.bind("<<ListboxSelect>>", fillout )

my_entry.bind("<KeyRelease>", check)

################################################################################





#############################################################################inst2
#############################################################################
inst2_p1=""" xterm -e 'bash -c \"sudo apt purge """
inst2_p2="""; exec bash\"' """



inst2_frame = Frame(tab2, borderwidth=0, background='#191925',highlightthickness=0,pady=10,padx=10)
#ess_frame.place(x=3,y=250)
inst2_frame.pack(anchor="n",pady=10)


def inst_btn2():
    entry_text2 = my_entry2.get()
    popen(inst2_p1 + entry_text2 + inst2_p2)



# Update the listbox

def update2(data2):
    # Clear the listbox
    my_list2.delete(0, END)

    # Add toppings to listbox
    for item2 in data2:
        my_list2.insert(END, item2)

# Update entry box with listbox clicked
def fillout2(event):
    # Delete wot is in  Box
    my_entry2.delete(0,END)    
    # Add clicked list item to enty box  
    my_entry2.insert(0, my_list2.get(ACTIVE))


# Checkfunktion Entry vs. List

def check2(event):
    # grad inserted
    typed2 = my_entry2.get()
    
    if typed2 == '':
        data2 = content2
    else:
        data2 = []
        for item2 in content2:
            if typed2.lower() in item2.lower():
                data2.append(item2)
                
    #updates listbox with selected item
    update2(data2)
                

fo2 = open("essentials/packages.list", "r")
content2 = fo2.readlines()
print (content2)

inst_btn2 = Button(inst2_frame,image=ip29, command=inst_btn2, highlightthickness=0, borderwidth=0,
                        background='#191925', foreground="white",font=(("Helvetica,bold"),"12"))        

inst_btn2.grid(row=0, column=0)

info_inst1= Button(inst2_frame, image=ip21,anchor="n",
                  highlightthickness=0, borderwidth=0, background='#191925',command=inst_inf2).grid(row=1,rowspan=1,column=0)
# Create an entry box

my_entry2 = Entry(inst2_frame,font=("Helvetica",12), width=60)
my_entry2.grid(row=0, column=1)

my_list2 = Listbox(inst2_frame, width=67)
my_list2.grid(row=1, column=1,padx=10)

fo2 = open("essentials/packages.list", "r")
content2 = fo2.readlines()
for i2,s2 in enumerate(content2):
    content2[i2] = s2.strip()
print (content2)




# Add toppings

update2(content2)


#Create binding

my_list2.bind("<<ListboxSelect>>", fillout2 )

my_entry2.bind("<KeyRelease>", check2)

########################################################################git&ppa
inst3_p1=""" xterm -e 'bash -c \"~/PDL/essentials/"""
inst3_p2="""; exec bash\"' """
inst3_p3="/install.sh"

uninst3_p1=""" xterm -e 'bash -c \"~/PDL/essentials/"""
uninst3_p2="""; exec bash\"' """
uninst3_p3="/uninstall.sh"

inst3_frame = Frame(tab3, borderwidth=0, background='#191925',highlightthickness=0,pady=10,padx=10)
#ess_frame.place(x=3,y=250)
inst3_frame.grid(row=0,column=0)

inst31_frame = Frame(tab3, borderwidth=0, background='#191925',highlightthickness=0,pady=10,padx=10)
#ess_frame.place(x=3,y=250)
inst31_frame.grid(row=0,column=1)




def inst_git():
    entry_text3 = my_entry3.get()
    popen(inst3_p1 + entry_text3+inst3_p3+ inst3_p2)

def uninst_git():
    entry_text3 = my_entry3.get()
    popen(uninst3_p1 + entry_text3+uninst3_p3+ uninst3_p2)

# Update the listbox

def update3(data3):
    # Clear the listbox
    my_list3.delete(0, END)

    # Add toppings to listbox
    for item3 in data3:
        my_list3.insert(END, item3)

# Update entry box with listbox clicked
def fillout3(event):
    # Delete wot is in  Box
    my_entry3.delete(0,END)    
    # Add clicked list item to enty box  
    my_entry3.insert(0, my_list3.get(ACTIVE))


# Checkfunktion Entry vs. List

def check3(event):
    # grad inserted
    typed3 = my_entry3.get()
    
    if typed3 == '':
        data3 = content3
    else:
        data3 = []
        for item3 in content3:
            if typed3.lower() in item3.lower():
                data3.append(item3)
                
    #updates listbox with selected item
    update3(data3)
                

fo3 = open("essentials/apps.txt", "r")
content3 = fo3.readlines()
print (content3)

inst_btn3 = Button(inst3_frame,image=ip28, highlightthickness=0, borderwidth=0,
                        background='#191925', foreground="white",font=(("Helvetica,bold"),"12"),command=inst_git)        

inst_btn3.pack(anchor="n")

uninst_btn3 = Button(inst3_frame,image=ip29, highlightthickness=0, borderwidth=0,
                        background='#191925', foreground="white",font=(("Helvetica,bold"),"12"),command=uninst_git)        

uninst_btn3.pack()

info_inst3= Button(inst3_frame, image=ip21,anchor="n",
                  highlightthickness=0, borderwidth=0, background='#191925',command=inst_inf3).pack()
# Create an entry box

my_entry3 = Entry(inst31_frame,font=("Helvetica",12), width=60)
my_entry3.pack()

my_list3 = Listbox(inst31_frame, width=67,height=30)
my_list3.pack()
fo3 = open("essentials/apps.txt", "r")
content3 = fo3.readlines()
for i3,s3 in enumerate(content3):
    content3[i3] = s3.strip()
print (content3)




# Add toppings

update3(content3)


#Create binding

my_list3.bind("<<ListboxSelect>>", fillout3 )

my_entry3.bind("<KeyRelease>", check3)

#####################################################################################################
tab_control.pack(expand=1, fill='both')

main.mainloop()
