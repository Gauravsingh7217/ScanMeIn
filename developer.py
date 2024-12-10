from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1900x900+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",25,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1300,height=35)

        img_top=Image.open(r"C:\Users\win\Desktop\Advance smart attendance\college_images\dev.jpg")
        img_top=img_top.resize((1300,620),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1300,height=620)

        #Frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=800,y=0,width=400,height=500)


        img_top1=Image.open(r"C:\Users\win\Desktop\Advance smart attendance\college_images\dev.jpg")
        img_top1=img_top.resize((1300,620),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=300,y=0,width=1300,height=620) 


if __name__ =="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
