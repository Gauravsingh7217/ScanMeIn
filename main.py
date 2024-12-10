from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from help import Help


class Face_recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1900x900+0+0")
        self.root.title("face Recognition System")


#1st
        img=Image.open(r"C:\Users\win\Desktop\Advance smart attendance\college_images\BestFacialRecognition.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
    
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=450,height=130)


#2nd
        img1=Image.open(r"C:\Users\win\Desktop\Advance smart attendance\college_images\facialrecognition.png")
        img1=img1.resize((450,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=450,y=0,width=450,height=130)

#3rd
        img2=Image.open(r"C:\Users\win\Desktop\Advance smart attendance\college_images\images.jpg")
        img2=img2.resize((450,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=900,y=0,width=450,height=130)


#bg image
        img3=Image.open(r"C:\Users\win\Desktop\Advance smart attendance\college_images\images3.jpg")
        img3=img3.resize((1620,780),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1300,height=530)
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE ",font=("times new roman",25,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1430,height=45)

        #student button
        img4=Image.open(r"C:\Users\win\Desktop\Advance smart attendance\college_images\gettyimages-1022573162.jpg")
        img4=img4.resize((150,150),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
                                               
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=150,y=70,width=150,height=150)
         

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",10,"bold"),bg="darkblue",fg="white")
        title_lbl.place(x=0,y=0,width=1430,height=45)
        b1_1.place(x=150,y=200,width=150,height=20)


        #detect face  button
        img5=Image.open(r"C:\Users\win\Desktop\Advance smart attendance\college_images\face_detector1.jpg")
        img5=img5.resize((150,150),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=400,y=70,width=150,height=150)
        

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",10,"bold"),bg="darkblue",fg="white")
        title_lbl.place(x=0,y=0,width=1430,height=45)
        b1_1.place(x=400,y=200,width=150,height=20)


        #attendance face  button
        img6=Image.open(r"C:\Users\win\Desktop\Advance smart attendance\college_images\report.jpg")
        img6=img6.resize((150,150),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=650,y=70,width=150,height=150)
        

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",10,"bold"),bg="darkblue",fg="white")
        title_lbl.place(x=0,y=0,width=1430,height=45)
        b1_1.place(x=650,y=200,width=150,height=20)



        #help desk face  button
        img7=Image.open(r"C:\Users\win\Desktop\Advance smart attendance\college_images\help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg")
        img7=img7.resize((150,150),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=900,y=70,width=150,height=150)
        

        b1_1=Button(bg_img,text="Help desk",cursor="hand2",command=self.help_data,font=("times new roman",10,"bold"),bg="darkblue",fg="white")
        title_lbl.place(x=0,y=0,width=1430,height=45)
        b1_1.place(x=900,y=200,width=150,height=20)
        

        #Train desk face  button
        img8=Image.open(r"C:\Users\win\Desktop\Advance smart attendance\college_images\Train.jpg")
        img8=img8.resize((150,150),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=150,y=250,width=150,height=150)
        
 
        b1_1=Button(bg_img,text="Train data ",cursor="hand2",command=self.train_data,font=("times new roman",10,"bold"),bg="darkblue",fg="white")
        title_lbl.place(x=0,y=0,width=1430,height=45)
        b1_1.place(x=150,y=400,width=150,height=20)




        #Photo  face  button

        img9=Image.open(r"C:\Users\win\Desktop\Advance smart attendance\college_images\opencv_face_reco_more_data.jpg")
        img9=img9.resize((150,150),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=400,y=250,width=150,height=150)
        
 
        b1_1=Button(bg_img,text="Photo face ",cursor="hand2",command=self.open_img,font=("times new roman",10,"bold"),bg="darkblue",fg="white")
        title_lbl.place(x=0,y=0,width=1430,height=45)
        b1_1.place(x=400,y=400,width=150,height=20)



        # Developer  button
        img10=Image.open(r"C:\Users\win\Desktop\Advance smart attendance\college_images\Team-Management-Software-Development.jpg")
        img10=img10.resize((150,150),Image.ANTIALIAS)


        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=650,y=250,width=150,height=150)
        
 
        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",10,"bold"),bg="darkblue",fg="white")
        title_lbl.place(x=0,y=0,width=1430,height=45)
        b1_1.place(x=650,y=400,width=150,height=20)


        # Exit   button
        img11=Image.open(r"C:\Users\win\Desktop\Advance smart attendance\college_images\exit.jpg")
        img11=img11.resize((150,150),Image.ANTIALIAS)

 
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=900,y=250,width=150,height=150)
        
 
        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",10,"bold"),bg="darkblue",fg="white")
        title_lbl.place(x=0,y=0,width=1430,height=45)
        b1_1.place(x=900,y=400,width=150,height=20)


    def open_img(self):
        os.startfile("data")

     


        #functions button
    def student_details(self):

        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    
    def train_data(self):

        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)  

    def face_data(self):

        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window) 

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)      
    





        



if __name__ =="__main__":
    root=Tk()
    obj=Face_recognition_system(root)
    root.mainloop()
    