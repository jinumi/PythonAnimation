from tkinter import *
from PIL import Image

window = Tk()
window.config(background="white")
window.geometry("500x500")
window.resizable(0, 0)
window.title("Animation")
window.iconbitmap("icon.ico")

file = "yy3.gif"
info = Image.open(file)
frames = info.n_frames
im = [PhotoImage(file=file, format=f"gif -index {i}") for i in range(frames)]
count = 0
anim = None


def animation(count):
    global anim
    im2 = im[count]

    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    anim = window.after(50, lambda: animation(count))


gif_label = Label(window, image="")
gif_label.pack()

animation(count)
window.mainloop()
