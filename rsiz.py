import tkinter
import numpy as np
from tkinter import *
import tkinter.messagebox as mbox
from PIL import ImageTk, Image
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
import os
import cv2
from cv2 import *
import random
img =''
def ofiname():
    global img
    fln = filedialog.askopenfilenames(initialdir=os.getcwd(),title="Browse Image File", filetypes=(("JPG Image","*.jpg"), ("PNG Image","*.png"), ("All Files","*.*")))
    t1.set(fln)
    img = cv2.imread(fln, cv2.IMREAD_UNCHANGED)
    w.set(img.shap[0])
    h.set(img.shap[1])

def prviw():
    cv2.imshow("Source Image", img)
    cv2.waitKey(0)
    cv2.destroAllWindows()


def Recalculate():
    p = int(perc.get())
    new_width =  int(int(w.get()) * p / 100)
    new_height = int(int(h.get()) * p / 100)
    w.set(new_width)
    h.set(new_height)


def preview_resized_img():
    nw = int(w.get())
    nh = int(h.get())
    img2 = cv2.resize(img,(nw,nh), interpolatlon =cv2.INTER_AREA)
    cv2.imshow("Preview Resized Image",img2)
    cv2.waitky(0)
    cv2.destroAllWindows()


def save_resized_img():
    fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Browse Image File", filetypes=(("JPG Image","*.jpg"), ("PNG Image","*.png"), ("All Files","*.*")))
    nw = int(w.get())
    nh = int(h.get())
    img2 = cv2.resize(img, (nw, nh), interpolatlon=cv2.INTER_AREA)
    cv2.imwrite(fln,img2)
    




window = Tk()

t1 = StringVar()
w= StringVar()
h= StringVar()
perc= StringVar()

wrapper = LabelFrame(window,text="Source File")
wrapper.pack(fill="both",expand="yes",padx=20,pady=20)

wrapper2 = LabelFrame(window,text="Imag tails")
wrapper2.pack(fill="both",expand="yes",padx=20,pady=20)

wrapper3 = LabelFrame(window,text="Ations")
wrapper3.pack(fill="both",expand="yes",padx=20,pady=20)

lbl = Label(wrapper,text="Source File")
lbl.pack(side=tk.LEFT,padx=10,pady=10)

nt = Entry(wrapper,text="t1")
nt.pack(side=tk.LEFT,padx=10,pady=10)

btn = Button(wrapper,text="Browse", command= ofiname)
btn.pack(side=tk.LEFT,padx=10,pady=10)

btn2 = Button(wrapper,text="preview", command= prviw)
btn2.pack(side=tk.LEFT,padx=10,pady=10)

lbl2 = Label(wrapper2,text="Dimension")
lbl2.pack(side=tk.LEFT,padx=10,pady=10)

nt2 = Entry(wrapper,textvariable=w)
nt2.pack(side=tk.LEFT,padx=10,pady=10)

lbl3 = Label(wrapper2,text="X")
lbl3.pack(side=tk.LEFT,padx=10,pady=10)

nt3 = Entry(wrapper,textvariable=h)
nt3.pack(side=tk.LEFT,padx=10,pady=10)

wrapper4 = LabelFrame(window,text="Pixel save")
wrapper4.pack(fill="both",expand="yes",padx=20,pady=20)

lbl4 = Label(wrapper4,text="Percentage")
lbl4.pack(side=tk.LEFT,padx=10,pady=10)

nt4 = Entry(wrapper,textvariable=perc)
nt4.pack(side=tk.LEFT,padx=10,pady=10)

btn3 = Button(wrapper4,text="Recalculate Dimension ",command=Recalculate)
btn3.pack(side=tk.LEFT,padx=10,pady=10)


wrapper5 = LabelFrame(window,text="Ations")
wrapper5.pack(fill="both",expand="yes",padx=20,pady=20)

prevbtn = Button(wrapper5,text="Prviw",command=preview_resized_img)
prevbtn.pack(side=tk.LEFT, padx=10, pady= 10)

savebtn = Button(wrapper5, text="Save", command=save_resized_img)
savebtn.pack(side=tk.LEFT, padx=10, pady= 10)
window.geometry("1100x800")

window.configure(bg='grey')

window.title("Image Resize App")

window.mainloop()
