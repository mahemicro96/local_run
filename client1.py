import requests
import json
import cv2
import pybase64
import base64
import requests
from tkinter import filedialog
from functools import partial
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image
base_url='http://127.0.0.1:8000/'
end_point='upload/'


def create_resource():
         root = tk.Tk()
         root.withdraw()
         file_path = filedialog.askopenfilename()
         
         headers = {'content-type': "application/json",'Accept': "application/json"}
         with open(file_path, "rb") as f:
              #str1 = base64.b64encode(f.read())
              str1 = pybase64.urlsafe_b64encode(f.read())
              st =str1
              data={
              'file':st.decode(),
              'description':'New1 India'
              }
              r=requests.post(base_url+end_point,data=json.dumps(data),headers=headers)
              print(r.status_code)
              messagebox.showinfo("status", "image uploaded successfully")




master1 = tk.Tk()
img = Image.open("ima.png")  # PIL solution
img = img.resize((500, 500))
logo = ImageTk.PhotoImage(img)
img = tk.Label(master1,image=logo)
img.image = logo
img.place(x=0, y=0)
master1.geometry("500x500")
master1.title('Downloaded Image')
def get_resources(id=40): 
    data={}
    print(id)
    #id=40
  
    if id is not None: 
     data={'id':id}
     headers = {'content-type': "application/json",'Accept': "application/json"}
     resp=requests.get(base_url+end_point,data=json.dumps(data),headers=headers)
     print("/////////////")
     k=resp.json()
     
     p=k['im']
     fh = open("t602.jpg", "wb")
     fh.write(pybase64.urlsafe_b64decode(p))
     fh.close()
     img = Image.open("t602.jpg")  # PIL solution
     img = img.resize((500, 500))
     logo = ImageTk.PhotoImage(img)
     #w1 = tk.Label(master, image=logo).pack(side = TOP)
     
     img = tk.Label(master1,image=logo)
     img.image = logo
     img.place(x=0, y=0)
     #image = cv2.imread('t602.jpg')
     #cv2.imshow('Original image',image)
    if id is None:
        print("enter id")

master = tk.Tk()
master.geometry("500x500")
master.title('Client')
e1 = tk.Entry(master)
tk.Button(master, text='UPLOAD', command=create_resource).grid(row=2, 
                                                               column=0, 
                                                               sticky=tk.W, 
                                                               pady=4)
tk.Label(master, text="ENTER ID").grid(row=3,column=0)
e1.grid(row=3, column=1)
tk.Button(master, text='DOWNLOAD', command=lambda:get_resources(int(e1.get()))).grid(row=4, 
                                                               column=0, 
                                                               sticky=tk.W, 
                                                               pady=4)
tk.Button(master, 
          text='Quit', 
          command=quit).grid(row=5, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
master.mainloop()
tk.mainloop()
"""
print("Image uploaded successfully")
print("For extract image from server type 1:",end=" ")
x=int(input())
if(x==1):
    print("Enter ID of image")
    x=int(input())
    get_resources(x)
"""
"""
with open("test.jpg", "rb") as imageFile:
    str = pybase64.urlsafe_b64encode(imageFile.read())

fh = open("t5.jpg", "wb")
fh.write(pybase64.urlsafe_b64decode(str))
fh.close()
image = cv2.imread('t5.jpg')
cv2.imshow('Original image',image)
"""
#for open image file using PIL
"""
from PIL import Image 
  
# open method used to open different extension image file 
im = Image.open("t5.jpg")  
  
# This method will show image in any image viewer  
#im.show()  
print(type(im))
"""
#FOR string encode(bytes) & decode(string)
"""
x="abc"
y=x.encode()
print(y.decode())"""

