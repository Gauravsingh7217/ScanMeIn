from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from student import Student
from train import Train
import cv2
import mysql.connector
from time import strftime
from datetime import datetime

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1900x900+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="Face Recognition", font=("times new roman", 30, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1350, height=45)

        # 1st image
        img_top = Image.open(r"C:\Users\win\Desktop\Advance smart attendance\college_images\face_detector1.jpg")
        img_top = img_top.resize((550, 600), Image.Resampling.LANCZOS)  # Fixed deprecated usage
        self.photoimg_left = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_left)
        f_lbl.place(x=0, y=50, width=550, height=600)

        # 2nd image
        img_bottom = Image.open(r"C:\Users\win\Desktop\Advance smart attendance\college_images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_bottom = img_bottom.resize((800, 600), Image.Resampling.LANCZOS)  # Fixed deprecated usage
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=550, y=50, width=800, height=600)

        # Button
        b1_1 = Button(f_lbl, text="Face Recognition", command=self.face_recogn, cursor="hand2", font=("times new roman", 18, "bold"), bg="green", fg="white")
        b1_1.place(x=300, y=530, width=200, height=35)

    def face_recogn(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="Aliengr123#", database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT Name FROM student WHERE Student_id=" + str(id))
                n = my_cursor.fetchone()
                n = n[0] if n else "Unknown Name"  # Extract name or set to 'Unknown Name'

                my_cursor.execute("SELECT Roll FROM student WHERE Student_id=" + str(id))
                r = my_cursor.fetchone()
                r = r[0] if r else "Unknown Roll"  # Extract roll or set to 'Unknown Roll'

                my_cursor.execute("SELECT Dep FROM student WHERE Student_id=" + str(id))
                d = my_cursor.fetchone()
                d = d[0] if d else "Unknown Department"  # Extract department or set to 'Unknown Department'

                if confidence > 77:
                    cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Dep: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:
                cv2.destroyAllWindows()
                video_cap.release()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
