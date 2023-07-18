import customtkinter


def button_function():
    print("Button pressed")

app = customtkinter.CTk()
app.attributes('-zoomed', True)  # Set the window to full screen


frame1_width = screen_width // 2
frame1_height = screen_height // 2

frame2_width = frame1_height
frame2_height = frame1_height

frame1 = customtkinter.CTkFrame(app,  bg_color="blue", width=frame1_width, height=frame1_height)
frame1.pack(side="top", anchor="nw")

frame2 = customtkinter.CTkFrame(app,  width=screen_width, height=frame2_height)
frame2.pack(side="top", anchor="s")

frame3 = customtkinter.CTkFrame(app,  width=frame2_width, height=frame2_height)
frame3.pack(side="top", anchor="ne")

button = customtkinter.CTkButton(master=frame1, text="CTkButton", command=button_function)
button.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()









