
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

popen("xterm -e 'bash -c \"apt-cache pkgnames > ~/PDL/essentials/SomeFile.txt && exit; exec bash\"'")

popen("dpkg --get-selections > ~/PDL/essentials/packages.list")
#os.system("sed -e s/install//g -i /home/timo/PiGro-Aid-/essentials/packages.list")
popen("xterm -e 'bash -c \"sed -e s/install//g -i ~/PDL/essentials/packages.list && exit; exec bash\"'")




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
tab_control.add(tab2, compound=LEFT, text='Install / Uninstall')
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
    
def pop_gparted():
    global gparted
    gparted=Toplevel()
    gparted['background'] = '#333333'
      
    logo = Label(gparted, image=ip08, text="Gparted",font=("Helvetica",16), anchor="w",
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP).grid(column=0, row=0)
    
    gp_inst = Button(gparted, text="Install", anchor="w",
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=0, row=1)
    
    gp_uninst = Button(gparted, text="Uninstall", anchor="w",
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=0, row=2)
    
    gp_info = Label(gparted, text="GParted is a free partition editor for graphically managing your disk partitions.", anchor="w",
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP).grid(column=1, row=0,rowspan=2)
    
def pop_neofetch():
    global neofetch
    neofetch=Toplevel()
    neofetch['background'] = '#333333'
      
    logo = Label(neofetch, image=ip10, text="Neofetch",font=("Helvetica",16), anchor="w",
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP).grid(column=0, row=0)
    
    nf_inst = Button(neofetch, text="Install", anchor="w",
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=0, row=1)
    
    nf_uninst = Button(neofetch, text="Uninstall", anchor="w",
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=0, row=2)
    
    nf_info = Label(neofetch, text="Neofetch is a command-line system information tool written in bash 3.2+.\nNeofetch displays information about your operating system,\nsoftware and hardware in an aesthetic\nand visually pleasing way.", anchor="w", highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP).grid(column=1, row=0,rowspan=2)
    
def pop_pikiss():
    global pikiss
    pikiss=Toplevel()
    pikiss['background'] = '#333333'
      
    logo = Label(pikiss, image=ip13, text="PiKiss",font=("Helvetica",16), anchor="w",
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP).grid(column=0, row=0)
    
    pk_inst = Button(pikiss, text="Install", anchor="w",
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=0, row=1)
    
    pk_uninst = Button(pikiss, text="Uninstall", anchor="w",
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=0, row=2)
    
    pk_info = Label(pikiss, text="Installing an application on Linux is not a complex task.\nSometimes you just type sudo apt install and get\n the application installed with all of its dependencies.\nBut... What if we need to install more than one app\n such as a web server or it requires many steps to complete\nthe install process? Is it not in the\n official repositories? What if you want to get rid of input commands?", anchor="w",
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP).grid(column=1, row=0,rowspan=2)


def pop_bleachbit():
    global bleachbit
    bleachbit=Toplevel()
    bleachbit['background'] = '#333333'
      
    logo = Label(bleachbit, image=ip02, text="Gparted",font=("Helvetica",16), anchor="w",
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP).grid(column=0, row=0)
    
    bb_inst = Button(bleachbit, text="Install", anchor="w",
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=0, row=1)
    
    bb_uninst = Button(bleachbit, text="Uninstall", anchor="w",
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=0, row=2)
    
    bb_info = Label(bleachbit, text="BleachBit has many useful features designed to help you\neasily clean your computer to free space and maintain privacy.", anchor="w",
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP).grid(column=1, row=0,rowspan=2)
    
def pop_pi_imager():
    global pi_imager
    pi_imager=Toplevel()
    pi_imager['background'] = '#333333'
      
    logo = Label(pi_imager, image=ip12, text="Gparted",font=("Helvetica",16), anchor="w",
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP).grid(column=0, row=0)
    
    pi_inst = Button(pi_imager, text="Install", anchor="w",
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=0, row=1)
    
    pi_uninst = Button(pi_imager, text="Uninstall", anchor="w",
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=0, row=2)
    
    pi_info = Label(pi_imager, text="BleachBit has many useful features designed to help you\neasily clean your computer to free space and maintain privacy.", anchor="w",
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP).grid(column=1, row=0,rowspan=2)
    
    
    
def inst_inf1():
    messagebox.showinfo("You called for help?", "The list contains all available packages. Yes, even the ones you added yourself! You can either search with the mouse wheel or type the desired package into the search bar. Click on the desired packet and press install.")

def inst_inf2():
    messagebox.showinfo("What is it?", "The list contains all installed packages. ALL! You can either search with the mouse wheel or type the desired package into the search bar. Click on the desired packet and press uninstall.")
    
#####################################################################################################
tab_tp1 = Image.open('icons/Essentials.png')
tp01 = ImageTk.PhotoImage(tab_tp1)
tl01 = Label(image=tp01)



#####################################################################################################
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

tab_ip22 = Image.open('essentials/Sublime/sublime_text.png')
ip22 = ImageTk.PhotoImage(tab_ip22)
il22 = Label(image=ip22)

tab_ip23 = Image.open('essentials/Sublime/sublime_merge.png')
ip23 = ImageTk.PhotoImage(tab_ip23)
il23 = Label(image=ip23)


#####################################################################TAB1
ess_lbl = Label(tab1, image=tp01, borderwidth=0, background='white',highlightthickness=0)
#ess_lbl.place(x=13,y=50)
ess_lbl.pack(pady=50)

Sugg = Label(tab1, width=105, text="Cool Staff that is not in the standard Respository:",font=("Helvetica",16), anchor="w",
                  highlightthickness=0, borderwidth=1, background='#333333', foreground="white").pack(padx=10)

ess_frame = Frame(tab1, borderwidth=0, background='#333333',highlightthickness=0)
#ess_frame.place(x=3,y=250)
ess_frame.pack()


shop_btn01 = Button(ess_frame, width=105, image=ip03, text="btop++", anchor="n", highlightthickness=0,
                  borderwidth=1, background='#434343', foreground="white", compound=TOP,font=("Helvetica",11,"bold")).grid(column=0, row=0,pady=5, padx=5)

shop_btn01 = Button(ess_frame, width=105, image=ip20, text="Argon One Driver", anchor="n", highlightthickness=0,
                  borderwidth=1, background='#434343', foreground="white", compound=TOP,font=("Helvetica",11,"bold")).grid(column=1, row=0,pady=5, padx=5)

shop_btn03 = Button(ess_frame, width=105, image=ip05, text="DeskPi Pro Driver", anchor="n", highlightthickness=0,
                  borderwidth=1, background='#434343', foreground="white", compound=TOP,font=("Helvetica",11,"bold")).grid(column=2, row=0,pady=5, padx=5)

shop_btn04 = Button(ess_frame, width=105, image=ip06, text="FanShim Driver", anchor="n", highlightthickness=0,
                  borderwidth=1, background='#434343', foreground="white", compound=TOP,font=("Helvetica",11,"bold")).grid(column=3, row=0,pady=5, padx=5)

shop_btn05 = Button(ess_frame, width=105, image=ip13, text="PiKiss", anchor="n", highlightthickness=0,
                  borderwidth=1, background='#434343', foreground="white", compound=TOP,font=("Helvetica",11,"bold"),command=pop_pikiss).grid(column=4, row=0,pady=5, padx=5)

shop_btn06 = Button(ess_frame, width=105, image=ip11, text="Pi-Apps", anchor="n", highlightthickness=0,
                  borderwidth=1, background='#434343', foreground="white", compound=TOP,font=("Helvetica",11,"bold")).grid(column=0, row=1,pady=0, padx=5)

shop_btn07 = Button(ess_frame, width=105, image=ip17, text="Tetris-CLI", anchor="n", highlightthickness=0,
                  borderwidth=1, background='#434343', foreground="white", compound=TOP,font=("Helvetica",11,"bold")).grid(column=1, row=1,pady=1, padx=5)

shop_btn08 = Button(ess_frame, width=105, image=ip01, text="Albert", anchor="n", highlightthickness=0,
                  borderwidth=1, background='#434343', foreground="white", compound=TOP,font=("Helvetica",11,"bold")).grid(column=2, row=1,pady=2, padx=5)

shop_btn09 = Button(ess_frame, width=105, image=ip23, text="Sublime Merge 64 Bit", anchor="n", highlightthickness=0,
                  borderwidth=1, background='#434343', foreground="white", compound=TOP,font=("Helvetica",9,"bold")).grid(column=3, row=1,pady=2, padx=5)

shop_btn10 = Button(ess_frame, width=105, image=ip22, text="Sublime Text 64 Bit", anchor="n", highlightthickness=0,
                  borderwidth=1, background='#434343', foreground="white", compound=TOP,font=("Helvetica",9,"bold")).grid(column=4, row=1,pady=2, padx=5)

#####################################################################################################TAB2
i = Image.open('icons/pigro_bg.png')
p = ImageTk.PhotoImage(i)
l = Label(tab2, image=p)
l.image = p
l['background'] = '#333333'
l.place(x=0, y=10)

inst0_frame = Frame(tab2, borderwidth=0, background='#333333',highlightthickness=0)
#ess_frame.place(x=3,y=250)
inst0_frame.pack(anchor="nw",pady=10)



inst1_frame = Frame(tab2, borderwidth=0, background='#333333',highlightthickness=2,padx=10,pady=10)
#ess_frame.place(x=3,y=250)
inst1_frame.pack(anchor="n")

info_inst0= Button(inst1_frame, image=ip21,anchor="n",
                  highlightthickness=0, borderwidth=0, background='#333333',command=inst_inf1).grid(row=1,rowspan=1,column=0)



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


inst_btn = Button(inst1_frame, text="install", command=inst_btn1, highlightthickness=2, borderwidth=0,width=10,
                        background='#333333', foreground="white",font=(("Helvetica,bold"),"12"))        

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



inst2_frame = Frame(tab2, borderwidth=0, background='#333333',highlightthickness=2,pady=10,padx=10)
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

inst_btn2 = Button(inst2_frame, text="uninstall", command=inst_btn2, highlightthickness=2, borderwidth=0,width=10,
                        background='#333333', foreground="white",font=(("Helvetica,bold"),"12"))        

inst_btn2.grid(row=0, column=0)

info_inst1= Button(inst2_frame, image=ip21,anchor="n",
                  highlightthickness=0, borderwidth=0, background='#333333',command=inst_inf2).grid(row=1,rowspan=1,column=0)
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





#####################################################################################################
tab_control.pack(expand=1, fill='both')

main.mainloop()
