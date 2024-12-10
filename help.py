from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1900x900+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",25,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1300,height=35)

        img_top=Image.open(r"C:\Users\win\Desktop\Advance smart attendance\college_images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img_top=img_top.resize((1300,620),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1300,height=620)

        dev_label=Label(f_lbl,text="Email:taniyasingh4242@gmail.com",font=("times new roman",20,"bold"),bg="white",fg="blue")
        dev_label.place(x=450,y=200)

    

if __name__ =="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()
