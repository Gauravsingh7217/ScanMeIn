from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1900x900+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="Train Dataset ",font=("times new roman",25,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1100,height=35)

        img_top=Image.open(r"C:\Users\win\Desktop\Advance smart attendance\college_images\facialrecognition.png")
        img_top=img_top.resize((1300,275),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_left)
        f_lbl.place(x=0,y=0,width=1300,height=275)

        #button
        b1_1=Button(self.root,text="Train data",command=self.train_classifier,cursor="hand2",font=("times new roman",25,"bold"),bg="red",fg="black")
        
        b1_1.place(x=0,y=275,width=1300,height=65)




        img_bottom=Image.open(r"C:\Users\win\Desktop\Advance smart attendance\college_images\opencv_face_reco_more_data.jpg")
        img_bottom=img_bottom.resize((1300,275),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=340,width=1300,height=275)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]  

        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L')#gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        #train classifier

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed")

            


                                                                        
if __name__ =="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
