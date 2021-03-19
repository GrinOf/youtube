from __future__ import unicode_literals
import youtube_dl
import tkinter as tk
import subprocess
import os

def open():
    global sc,pop
    pop.destroy()
    sc.destroy()
    if os.name == 'nt':
        subprocess.Popen('explorer "C:\\Users"')

def download():
    global en, pop
    url = en.get()
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    pop = tk.Toplevel()
    pop.resizable(False,False)
    tk.Label(pop,text='Check your user folder on Windows, not sure about Mac',).pack()
    tk.Button(pop,text='Okay',width=6,command=open).pack()

global sc
sc = tk.Tk()
sc.geometry('400x300+0+0')
sc.resizable(False,False)
tk.Label(sc,text='URL:',width=4).pack()
global en
en = tk.Entry(sc,width=24)
en.pack()
tk.Button(sc,text='Download',width=10,command=download).pack()

sc.mainloop()
