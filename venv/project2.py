from tkinter import *
from tkinter import ttk, filedialog
from stegano import lsb
import os
import datetime


def browse_path():
    path_image_str = filedialog.askopenfilename(filetypes=[("Image File", '.jpg')])
    path_image.set(path_image_str)


def browse_path_dec():
    dec_image_str = filedialog.askopenfilename(filetypes=[("Image File", '.png')])
    path_image_dec.set(dec_image_str)


def clear_path():
    path_image.set("")


def clear_path_dec():
    path_image_dec.set("")


def clear_msg():
    msg.set("")


def upload_image():
    s = path_image.get()
    secret = lsb.hide(s, msg.get())
    secret.save(path_image.get() + str(datetime.datetime.now().microsecond) + ".png")


def upload_image_dec():
    msg = lsb.reveal(path_image_dec.get())
    dec_msg_str.set(msg)


root = Tk()
root.title("Image encryption")
root.geometry("800x300")
root.resizable(0, 0)

nb = ttk.Notebook(root)
enc_page = ttk.Frame(nb)
dec_page = ttk.Frame(nb)

nb.add(enc_page, text="Encryption")
nb.add(dec_page, text="Decryption")
nb.grid(row=1, column=1, columnspan=5)

path_image = StringVar()
msg = StringVar()
dec_msg_str = StringVar()
path = Label(enc_page, background="white", fg="black", textvariable=path_image, font=("", 14), width=30)
path.grid(row=2, column=1, columnspan=3, sticky="N", padx=30, pady=10)

select_path = Button(enc_page, fg="black", width=15, text="Browse image", command=browse_path)
select_path.grid(row=2, column=4, padx=10)

upload = Button(enc_page, fg="black", width=15, text="Upload", command=upload_image)
upload.grid(row=3, column=2, padx=10, pady=10)

clear_path = Button(enc_page, fg="black", width=15, text="Reset Path", command=clear_path)
clear_path.grid(row=3, column=4, padx=10, pady=10)

message = Entry(enc_page, background="white", textvariable=msg, fg="black", font=("", 18), width=30)
message.grid(row=4, column=1, columnspan=3, sticky="N", padx=30, pady=30)

clear_msg = Button(enc_page, fg="black", width=15, text="Clear Message", command=clear_msg)
clear_msg.grid(row=4, column=4, padx=10, pady=30)

# dec

path_image_dec = StringVar()

path = Label(dec_page, background="white", fg="black", textvariable=path_image_dec, font=("", 14), width=30)
path.grid(row=2, column=1, columnspan=3, sticky="N", padx=30, pady=10)

select_path = Button(dec_page, fg="black", width=15, text="Browse image", command=browse_path_dec)
select_path.grid(row=2, column=4, padx=10)

upload = Button(dec_page, fg="black", width=15, text="Upload", command=upload_image_dec)
upload.grid(row=3, column=2, padx=10, pady=10)

clear_path = Button(dec_page, fg="black", width=15, text="Reset Path", command=clear_path_dec)
clear_path.grid(row=3, column=4, padx=10, pady=10)

dec_msg = Label(dec_page, background="white", fg="black", textvariable=dec_msg_str, font=("", 14), width=30)
dec_msg.grid(row=4, column=1, columnspan=3, sticky="N", padx=30, pady=10)

root.mainloop()
