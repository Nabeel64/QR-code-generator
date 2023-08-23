from tkinter import *
import pyqrcode
from PIL import ImageTk,Image
import png
from tkinter import messagebox

def enterered_data_validator(name,link):
    if len(name)==0 or len(link)==0 or len(name)==0 and len(link)==0:
        return True

def generate():
    link_name=name_entry.get()
    link=link_entry.get()
    validation=enterered_data_validator(link_name,link)
    if validation:
        messagebox.showwarning('','Please enter all the fields')
    else:
        file_name=link_name+".png"
        url=pyqrcode.create(link)
        url.png(file_name,scale=4)
        image=ImageTk.PhotoImage(Image.open(file_name))
        img_label=Label(image=image)
        img_label.image=image
        canvas.create_window(200,400,window=img_label)

root=Tk()
root.title('QR-code Generator')
root.resizable(False,False)

canvas=Canvas(root,width=400,height=600)
canvas.pack()

label=Label(root,text='Qr Code Generator',fg='blue',font=('Arial',30))  
canvas.create_window(200,50,window=label)

name_label=Label(root,text="Link Name")
link_label=Label(root,text="Link")
canvas.create_window(200,100,window=name_label)
canvas.create_window(200,160,window=link_label)

name_entry=Entry(root)
link_entry=Entry(root)
canvas.create_window(200,120,window=name_entry)
canvas.create_window(200,180,window=link_entry)

btn=Button(text="Generate QR-code",command=generate)
canvas.create_window(200,230,window=btn)
    
root.mainloop()