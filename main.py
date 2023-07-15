import webcam.webcam_mesh as webcam_mesh
import webcam.picture_mesh as picture_mesh
import tkinter.messagebox as msgbox
from tkinter import *
import numpy as np
import pickle
import serial

picture_data = []
compare_bool = 0
webcam_data = []
wegith = []
ser = serial.Serial("COM4", 115200, timeout=1)
root = Tk()
root.configure(bg='#2E4053')
root.title("ict")
root.geometry("1530x830+0+0")
root.resizable(False,False)

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

def reset_msg():
    response = msgbox.askyesno(title=None, message="reset?")
    if response == 1:
        reset()

def start():
    start_btn.place_forget()
    reset_btn.place(relx=0.9, rely=0.9)
    loding1.pack(side=TOP, anchor=CENTER)   
    picture_btn.place(x = ((width - picture_btn.winfo_reqwidth()) / 2),\
                y = ((height - picture_btn.winfo_reqheight()) / 2))
 
def webcam():     
    global compare_bool, webcam_data, wegith, picture_data
    webcam_image = webcam_mesh.face_mesh()
    for j in webcam_image.values():
        webcam_data.append(j)
    for n in range(len(webcam_image)):
        w = (picture_data[n]-webcam_data[n])**2
        wegith.append(w)
    dd = np.array([wegith])
    with open('face_compare_model.pkl', 'rb') as f:
      model = pickle.load(f)
    pre = model.predict(dd)
    # face compare success
    if pre == 1:
      loding1.pack_forget()
      webcam_btn.place_forget()
      yes.place(x = ((width - yes.winfo_reqwidth()) / 2),\
                y = ((height - yes.winfo_reqheight()) / 2))
      order_btn.place(relx=0.45, rely=0.6)
    # face compare fail
    elif pre == 0:
      loding1.pack_forget()
      webcam_btn.place_forget()
      no.place(x = ((width - yes.winfo_reqwidth()) / 2),\
                y = ((height - yes.winfo_reqheight()) / 2)) 
def picture():
    picture_btn.place_forget()
    loding1.pack_forget()
    picture_image = picture_mesh.pic_mesh()
    for data in picture_image.values():
        picture_data.append(data)
    print(picture_data)
    webcam_btn.place(x = ((width - webcam_btn.winfo_reqwidth()) / 2),\
                      y = ((height - webcam_btn.winfo_reqheight()) / 2))
class menu:
    def __init__(self, tk, name, row, col, ratio_list):
        self.name = name
        self.number = 0
        self.label =Label(tk, text=f"{name}: {self.number}", bg='#2E4053', fg='#F7DC6F', relief= FLAT)
        self.label.grid(row=row, column=col+2, padx=10, pady=10)

        self.plus_btn =Button(tk, text="+", command=lambda: self.ratio_increase(ratio_list), bg='#5DADE2', relief= FLAT)
        self.plus_btn.grid(row=row, column=col+3, padx=10, pady=10)

        self.minus_btn =Button(tk, text="-", command=lambda: self.ratio_decrease(ratio_list), bg='#5DADE2', relief= FLAT)
        self.minus_btn.grid(row=row, column=col+1, padx=10, pady=10)

    def ratio_increase(self, ratio_list):
        self.number += 1
        ratio_list[self.name] = self.number
        self.update()

    def ratio_decrease(self, ratio_list):
        if self.number > 0:
            self.number -= 1
            ratio_list[self.name] = self.number
            self.update()

    def update(self):
        self.label.configure(text=f"{self.name}: {self.number}")
        
    def forget(self):
        self.label.grid_forget()
        self.plus_btn.grid_forget()
        self.minus_btn.grid_forget()

class App:
    def __init__(self, tk):
        self.tk = tk

        self.ratio_list = { 
            "mal": 0,
            "jack": 0,
            "cock": 0,
            "jim": 0,
            "soda": 0,
            "tonic": 0
        }

        self.drinks = {
            "mal"  : menu(self.tk, "mal"  , 0, 0, self.ratio_list),
            "jack" : menu(self.tk, "jack" , 1, 0, self.ratio_list),
            "cock" : menu(self.tk, "cock" , 2, 0, self.ratio_list),
            "jim"  : menu(self.tk, "jim"  , 3, 0, self.ratio_list),
            "soda" : menu(self.tk, "soda" , 4, 0, self.ratio_list),
            "tonic": menu(self.tk, "tonic", 5, 0, self.ratio_list)
        }

def move():
    yes.place_forget()
    no.place_forget()
    order_btn.place_forget()
    global app
    print_btn.place(x = ((width - print_btn.winfo_reqwidth()) / 2),\
                y = ((height - print_btn.winfo_reqheight()) / 2))
    app = App(root)

def reset():
    start_btn.place(x = ((width - start_btn.winfo_reqwidth()) / 2),\
                y = ((height - start_btn.winfo_reqheight()) / 2))
    reset_btn.place_forget() 
    loding1.pack_forget()
    order_btn.place_forget()
    webcam_btn.place_forget()
    picture_btn.place_forget()
    yes.place_forget()
    no.place_forget()
    webcam_data.clear()
    wegith.clear()
    picture_data.clear()
    print_btn.place_forget()
    for drink in app.drinks.values():
        drink.forget()
  
def print_list():
    ratio_data = []
    for value in app.ratio_list.values():
        ratio_data.append(value)
    
    for num in ratio_data:
        # serial
        ser.write(num)
        print(num)
    reset()   
              
start_btn = Button(root,command= start,  width=15, height=3, text='start',font=('Arial', 16),\
                   bg='#1E2A38', fg='white', relief= FLAT) 
start_btn.place(x = ((width - start_btn.winfo_reqwidth()) / 2),\
                y = ((height - start_btn.winfo_reqheight()) / 2))
picture_btn = Button(root,command= picture,  width=25, height=3, text='start registration card',font=('Arial', 16),\
                   bg='#1E2A38', fg='white', relief= FLAT)
reset_btn = Button(root, command= reset_msg, padx=15, pady=10, text="reset",\
                   bg='#354F6B', fg='#F4D03F', relief= FLAT)

webcam_btn = Button(root, command= webcam, width=15, height=3, text="compare to face",font=('Arial', 16),\
                    bg='#1E2A38', fg='white', relief= FLAT)

order_btn = Button(root, command= move, padx=15, pady=10, text="go to order",\
                   bg='#1E2A38', fg='white', relief= FLAT)

print_btn = Button(root, command=print_list, text = 'finish', padx=15, pady= 10, bg='#1E2A38', fg='white', relief= FLAT)


loding1 = Label(root,bg='#2E4053',fg="red", text='Show registration card' ,width=20, height=10, font=("Arial", 20))

yes = Label(root, bg='#2E4053',fg="red", text='Face_copare_correct' ,font=("Arial", 20))

no = Label(root,bg='#2E4053', fg="red", text='Face_copare_fail' ,font=("Arial", 20))


    


root.mainloop()
