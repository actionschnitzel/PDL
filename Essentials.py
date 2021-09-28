
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

popen("xterm -e 'bash -c \"apt-cache pkgnames > /home/timo/PiGro-Aid-/essentials/SomeFile.txt && exit; exec bash\"'")


popen("dpkg --get-selections > /home/timo/PiGro-Aid-/essentials/packages.list")
#os.system("sed -e s/install//g -i /home/timo/PiGro-Aid-/essentials/packages.list")
popen("xterm -e 'bash -c \"sed -e s/install//g -i /home/timo/PiGro-Aid-/essentials/packages.list && exit; exec bash\"'")




main = Tk()
main.title("PDL (Pacchetti Di Lamponi) v. ALPHA 0.00001 --Standalone-Version--")
icon = tk.PhotoImage(file="icons/PiGroLogoslim.png")
main.tk.call('wm', 'iconphoto', main._w, icon)
main['background'] = '#333333'
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
noteStyler.configure("TNotebook", borderwidth=0, tabposition='nw',highlightthickness=0, background="#333333") #
noteStyler.configure("TNotebook.Tab", borderwidth=0, foreground="white",font=("Helvetica",16),highlightthickness=0, background="#333333") #
noteStyler.configure("TFrame", background="#333333") #


noteStyler.map("TNotebook.Tab", background=[("selected", "#333333")], foreground=[("selected", "#d4244d")]);

tab_control = ttk.Notebook(main)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)



########################
tab_control.add(tab1, compound=LEFT, text='Start')
tab_control.add(tab2, compound=LEFT, text='Search & Install')
tab_control.add(tab3, compound=LEFT, text='Here will be sth')
#####################################################################################################
#apps
def pop_compiz():
    global compiz
    compiz=Toplevel()
    compiz['background'] = '#333333'
      
    logo = Label(compiz, image=ip04, text="Compiz",font=("Helvetica",16), anchor="w",
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP).grid(column=0, row=0)
    
    c_inst = Button(compiz, text="Install", anchor="w",
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT,command=compiz).grid(column=0, row=1)
    
    c_uninst = Button(compiz, text="Uninstall", anchor="w",
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT,command=compiz).grid(column=0, row=2)
    
    comp_info = Label(compiz, text="Compiz is a compositing window manager for the X Window System,\nusing 3D graphics hardware to create fast \ncompositing desktop effects for window management.\nEffects, such as a minimization animation or a cube workspace,\nare implemented as loadable plugins.", anchor="w",
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP).grid(column=1, row=0,rowspan=2)

#####################################################################################################
tab_tp1 = Image.open('icons/Essentials.png')
tp01 = ImageTk.PhotoImage(tab_tp1)
tl01 = Label(image=tp01)
#####################################################################################################
tab_ip1 = Image.open('essentials/Albert/albert-icon.png')
ip01 = ImageTk.PhotoImage(tab_ip1)
il01 = Label(image=ip01)

tab_ip2 = Image.open('essentials/Bleach_Bit/bleachbit_icon.png')
ip02 = ImageTk.PhotoImage(tab_ip2)
il02 = Label(image=ip02)

tab_ip3 = Image.open('essentials/btop++/logo.png')
ip03 = ImageTk.PhotoImage(tab_ip3)
il03 = Label(image=ip03)

tab_ip4 = Image.open('essentials/Compiz/compiz_icon.png')
ip04 = ImageTk.PhotoImage(tab_ip4)
il04 = Label(image=ip04)

tab_ip5 = Image.open('essentials/DeskPi_Pro_Driver/DeskpiPro_icon.png')
ip05 = ImageTk.PhotoImage(tab_ip5)
il05 = Label(image=ip05)

tab_ip6 = Image.open('essentials/FanShim_Driver/shim_icon.png')
ip06 = ImageTk.PhotoImage(tab_ip6)
il06 = Label(image=ip06)

tab_ip7 = Image.open('essentials/Gnome-Pie/gnome_pie_icon.png')
ip07 = ImageTk.PhotoImage(tab_ip7)
il07 = Label(image=ip07)

tab_ip8 = Image.open('essentials/Gparted/gparted_icon.png')
ip08 = ImageTk.PhotoImage(tab_ip8)
il08 = Label(image=ip08)

tab_ip9 = Image.open('essentials/Lutris/lutris_icon.png')
ip09 = ImageTk.PhotoImage(tab_ip9)
il09 = Label(image=ip09)

tab_ip10 = Image.open('essentials/NeoFetch/neofetch_icon.png')
ip10 = ImageTk.PhotoImage(tab_ip10)
il10 = Label(image=ip10)

tab_ip11 = Image.open('essentials/Pi-Apps/proglogo.png')
ip11 = ImageTk.PhotoImage(tab_ip11)
il11 = Label(image=ip11)

tab_ip12 = Image.open('essentials/Pi_Imager/Raspberry-Pi-Imager.png')
ip12 = ImageTk.PhotoImage(tab_ip12)
il12 = Label(image=ip12)

tab_ip13 = Image.open('essentials/PiKiss/logo_pikiss_header.png')
ip13 = ImageTk.PhotoImage(tab_ip13)
il13 = Label(image=ip13)

tab_ip14 = Image.open('essentials/Synaptic/debian-pkg-icon.png')
ip14 = ImageTk.PhotoImage(tab_ip14)
il14 = Label(image=ip14)

tab_ip15 = Image.open('essentials/Plank/plank-64.png')
ip15 = ImageTk.PhotoImage(tab_ip15)
il15 = Label(image=ip15)

tab_ip16 = Image.open('essentials/Samba/samba.png')
ip16 = ImageTk.PhotoImage(tab_ip16)
il16 = Label(image=ip16)

tab_ip17 = Image.open('essentials/Tetris-CLI/tetris.png')
ip17 = ImageTk.PhotoImage(tab_ip17)
il17 = Label(image=ip17)

tab_ip18 = Image.open('essentials/Tilix/tilix-icon.png')
ip18 = ImageTk.PhotoImage(tab_ip18)
il18 = Label(image=ip18)

tab_ip19 = Image.open('essentials/Vulkan_Driver/vulkan_icon.png')
ip19 = ImageTk.PhotoImage(tab_ip19)
il19 = Label(image=ip19)

tab_ip20 = Image.open('essentials/Argon_One_Driver/argon_icon.png')
ip20 = ImageTk.PhotoImage(tab_ip20)
il20 = Label(image=ip20)



#####################################################################TAB1
ess_lbl = Label(tab1, image=tp01, borderwidth=0, background='white',highlightthickness=0)
#ess_lbl.place(x=13,y=50)
ess_lbl.pack(pady=50)

Sugg = Label(tab1, width=105, text="Suggestions:",font=("Helvetica",16), anchor="w",
                  highlightthickness=0, borderwidth=1, background='#333333', foreground="white").pack(padx=10)

ess_frame = Frame(tab1, borderwidth=0, background='#333333',highlightthickness=0)
#ess_frame.place(x=3,y=250)
ess_frame.pack()


shop_btn2 = Button(ess_frame, width=105, image=ip04, text="Compiz",font=("Helvetica",11,"bold"), anchor="n",
                  highlightthickness=0, borderwidth=1, background='#434343', foreground="white", compound=TOP,command=pop_compiz).grid(column=0, row=0, padx=5,pady=5)

shop_btn3 = Button(ess_frame, width=105, image=ip08, text="Gparted", anchor="n",
                  highlightthickness=0, borderwidth=1, background='#434343', foreground="white", compound=TOP,font=("Helvetica",11,"bold")).grid(column=1, row=0,pady=5, padx=5)

shop_btn4 = Button(ess_frame, width=105, image=ip10, text="NeoFetch", anchor="n", highlightthickness=0,
                  borderwidth=1, background='#434343', foreground="white", compound=TOP,font=("Helvetica",11,"bold")).grid(column=2, row=0,pady=5, padx=5)

shop_btn5 = Button(ess_frame, width=105, image=ip13, text="PiKiss", anchor="n", highlightthickness=0,
                  borderwidth=1, background='#434343', foreground="white", compound=TOP,font=("Helvetica",11,"bold")).grid(column=3, row=0,pady=5, padx=5)

shop_btn6 = Button(ess_frame, width=105, image=ip02, text="Bleach Bit", anchor="n",highlightthickness=0, borderwidth=1, background='#434343', foreground="white",
                   compound=TOP,font=("Helvetica",11,"bold")).grid(column=4, row=0,pady=5, padx=5)

shop_btn7 = Button(ess_frame, width=105, image=ip12, text="Pi Imager", anchor="n", highlightthickness=0,
                  borderwidth=1, background='#434343', foreground="white", compound=TOP,font=("Helvetica",11,"bold")).grid(column=5, row=0,pady=5, padx=5)

shop_btn8 = Button(ess_frame, width=105, image=ip14, text="Synaptic", anchor="n", highlightthickness=0,
                  borderwidth=1, background='#434343', foreground="white", compound=TOP,font=("Helvetica",11,"bold")).grid(column=0, row=1,pady=5, padx=5)

shop_btn9 = Button(ess_frame, width=105, image=ip07, text="Gnome-Pie", anchor="n", highlightthickness=0,
                  borderwidth=1, background='#434343', foreground="white", compound=TOP,font=("Helvetica",11,"bold")).grid(column=1, row=1,pady=5, padx=5)

shop_btn10 = Button(ess_frame, width=105, image=ip11, text="Pi-Apps", anchor="n", highlightthickness=0,
                  borderwidth=1, background='#434343', foreground="white", compound=TOP,font=("Helvetica",11,"bold")).grid(column=2, row=1,pady=5, padx=5)

shop_btn22 = Button(ess_frame, width=105, image=ip03, text="btop++", anchor="n", highlightthickness=0,
                  borderwidth=1, background='#434343', foreground="white", compound=TOP,font=("Helvetica",11,"bold")).grid(column=3, row=1,pady=5, padx=5)

shop_btn22 = Button(ess_frame, width=105, image=ip06, text="FanShim Driver", anchor="n", highlightthickness=0,
                  borderwidth=1, background='#434343', foreground="white", compound=TOP,font=("Helvetica",11,"bold")).grid(column=4, row=1,pady=5, padx=5)

shop_btn15 = Button(ess_frame, width=105, image=ip17, text="Tetris-CLI", anchor="n", highlightthickness=0,
                  borderwidth=1, background='#434343', foreground="white", compound=TOP,font=("Helvetica",11,"bold")).grid(column=5, row=1,pady=5, padx=5)

shop_btn16 = Button(ess_frame, width=105, image=ip20, text="Argon One Driver", anchor="n", highlightthickness=0,
                  borderwidth=1, background='#434343', foreground="white", compound=TOP,font=("Helvetica",11,"bold")).grid(column=0, row=2,pady=5, padx=5)

shop_btn17 = Button(ess_frame, width=105, image=ip05, text="DeskPi Pro Driver", anchor="n", highlightthickness=0,
                  borderwidth=1, background='#434343', foreground="white", compound=TOP,font=("Helvetica",11,"bold")).grid(column=1, row=2,pady=5, padx=5)

shop_btn18 = Button(ess_frame, width=105, image=ip15, text="Plank", anchor="n", highlightthickness=0,
                  borderwidth=1, background='#434343', foreground="white", compound=TOP,font=("Helvetica",11,"bold")).grid(column=2, row=2,pady=5, padx=5)

shop_btn19 = Button(ess_frame, width=105, image=ip01, text="Albert", anchor="n", highlightthickness=0,
                  borderwidth=1, background='#434343', foreground="white", compound=TOP,font=("Helvetica",11,"bold")).grid(column=3, row=2,pady=5, padx=5)

shop_btn20 = Button(ess_frame, width=105, image=ip18, text="Tilix", anchor="n", highlightthickness=0,
                  borderwidth=1, background='#434343', foreground="white", compound=TOP,font=("Helvetica",11,"bold")).grid(column=4, row=2,pady=5, padx=5)

shop_btn21 = Button(ess_frame, width=105, image=ip16, text="Samba", anchor="n", highlightthickness=0,
                  borderwidth=1, background='#434343', foreground="white", compound=TOP,font=("Helvetica",11,"bold")).grid(column=5, row=2,pady=5, padx=5)

#####################################################################################################TAB2
inst1_frame = Frame(tab2, borderwidth=0, background='#333333',highlightthickness=0)
#ess_frame.place(x=3,y=250)
inst1_frame.pack(anchor="nw",pady=20)





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


inst_btn = Button(inst1_frame, text="install", command=inst_btn1, highlightthickness=0, borderwidth=0,width=10,
                        background='#333333', foreground="white",font=(("Helvetica,bold"),"12"))        

inst_btn.grid(row=0, column=0)


# Create an entry box

my_entry = Entry(inst1_frame,font=("Helvetica",12), width=40)
my_entry.grid(row=0, column=1)

my_list = Listbox(inst1_frame, width=40)
my_list.grid(row=0,rowspan=8, column=2,padx=10)

fo = open("essentials/SomeFile.txt", "r")
content = fo.readlines()
for i,s in enumerate(content):
    content[i] = s.strip()
print (content)

# Add toppings

update(content)


#Create binding

my_list.bind("<<ListboxSelect>>", fillout )

my_entry.bind("<KeyRelease>", check)

#############################################################################inst2
#############################################################################
inst2_p1=""" xterm -e 'bash -c \"sudo apt purge """
inst2_p2="""; exec bash\"' """



inst2_frame = Frame(tab2, borderwidth=0, background='#333333',highlightthickness=0)
#ess_frame.place(x=3,y=250)
inst2_frame.pack(anchor="nw",pady=50)


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

inst_btn2 = Button(inst2_frame, text="uninstall", command=inst_btn2, highlightthickness=0, borderwidth=0,width=10,
                        background='#333333', foreground="white",font=(("Helvetica,bold"),"12"))        

inst_btn2.grid(row=0, column=0)


# Create an entry box

my_entry2 = Entry(inst2_frame,font=("Helvetica",12), width=40)
my_entry2.grid(row=0, column=1)

my_list2 = Listbox(inst2_frame, width=40)
my_list2.grid(row=0,rowspan=8, column=2,padx=10)

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





#####################################################################################################
tab_control.pack(expand=1, fill='both')

main.mainloop()
