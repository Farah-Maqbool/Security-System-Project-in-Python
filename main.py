from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
#making class
class Face_recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x700+0+0")
        self.root.title("Face Recognition system")

if __name__=="__main__":
    root=Tk()
    obj=Face_recognition_system(root)
    root.mainloop()