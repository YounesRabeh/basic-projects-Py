import tkinter.ttk
from tkinter import *
from Engine import main, get_yt_id, SAVE_PATH
from urllib.error import HTTPError
from PIL import ImageTk, Image
import urllib.request
from io import BytesIO

# FONTS:
font18B = ("Orator Std", 14, "bold")
font10B = ("Orator Std", 10, "bold")
font10 = ("Orator Std", 10)
font12 = ("Orator Std", 12)

# WINDOW:
window = Tk()
window.geometry('800x450')
window.resizable(width=False, height=False)
window.title("Video Downloader")                                                                                                                                                                                    

ent1 = Entry(window, font=font18B)
ent1.insert(END, 'ENTER_THE_LINK')

ent2 = Entry(window, font=font10)
ent2.insert(END, SAVE_PATH)
canvas = Canvas(window, width=318, height=157,  bg='black')

def fnc():
    content = ent1.get()
    file_name = ent2.get()
    my_res = resolution_dropdown.get()
    over_write_old = var1.get()
    only_audio = var2.get()

    
    try:
        main(content, my_res, file_name, only_audio)
    except ConnectionError:
        print("!!! >>main() FAILED")
        pass

def load_thumbnail():
    try:
        content = ent1.get()
        contentID = get_yt_id(content)
        u = urllib.request.urlopen(f"http://img.youtube.com/vi/{contentID}/hqdefault.jpg")
        raw_data = u.read()
        u.close()
        im = Image.open(BytesIO(raw_data))
        im = im.resize((320, 210), Image.Resampling.LANCZOS)
        global photo
        photo = ImageTk.PhotoImage(im)
        drawing()
    except HTTPError as err:
        # could add if statement like error 404 ...
        print("!!! >>Thumbnail exception")
        pass

def drawing():
    canvas.create_image(160, 80, anchor=CENTER, image=photo)

# Var's:
available_res = ["144p", "240p", "360p", "480p", "720p", "1080p"]
var1 = IntVar()
var2 = BooleanVar()


# UI:
btn1 = Button(window, text='DOWNLOAD', pady=7, font=font10B,command=fnc)
btn2 = Button(window, text='LOAD', pady=7, font=font10B, command=load_thumbnail)
resolution_dropdown = tkinter.ttk.Combobox(window, state="readonly", values=available_res, font=font10)
resolution_dropdown.current(4)
check1 = Checkbutton(window, text='Overwrite the old file', variable=var1, onvalue=1, offvalue=0,
font=font10)
check2 = Checkbutton(window, text='Only Audio', variable=var2, onvalue=True, offvalue=False, font=font10)
my_text = Label(window, text='Stored in: ', width=12, height=1, font=font10B)


# UI Render:
ent1.place(x=0, y=0,  width=630, height=38)
ent2.place(x=525, y=67,  width=225, height=25)
my_text.place(x=413, y=67)
canvas.place(x=430, y=90)
btn1.place(x=430, y=250, width=200)
btn2.place(x=630, y=0, width=118)
resolution_dropdown.place(x=630, y=250, width=120, height=38)
check1.place(x=430, y=300)
check2.place(x=430, y=330)


window.mainloop()