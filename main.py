import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import qrcode
from PIL import Image
def showabout():
    CTkMessagebox(title="About",message=" Link2QR Crafter \n Developer : Sukhmandeep Singh\n YouTube : TechWithSukhman \n Version : 1.0.0",icon="info")

def textqr():
    try:
      text = entry.get()
      if not text.strip():
         CTkMessagebox(title="Error",message="Please Enter link",icon="cancel")
      else:
       file_path = filedialog.asksaveasfilename(title="Save QR Code", defaultextension=".png",filetypes=[('PNG IMage','*.png'), ('All files','*.*')])
       print(file_path)
       if file_path:
          qr_img=qrcode.make(text)
          qr_img.save(file_path)
          CTkMessagebox(title="Success",message="QR Code Successfully Saved")
          entry.delete(0,ctk.END)
    except Exception as e:
       CTkMessagebox(title="Error",message=f"Error {e}",icon="cancel")




root = ctk.CTk()
root.geometry("500x300")
root.title("Link2QR Crafter")
root.resizable(False,False)

btn = ctk.CTkButton(root,text="About",width=50,command=showabout,fg_color="red").pack(pady=5,anchor="ne",padx=5)

f1 = ctk.CTkFrame(root)

logo_img = ctk.CTkImage(light_image=Image.open("logo.png"),size=(150,150))
img_label = ctk.CTkLabel(root,image=logo_img,text="")
img_label.pack()
f1.pack(pady=10)

entry = ctk.CTkEntry(f1,width=200,placeholder_text="Paste link here")
entry.pack(padx=4,side="left")

b1 = ctk.CTkButton(f1,text="Generate QR Code",command=textqr).pack(padx=4)

root.mainloop()