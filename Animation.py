# Importing necessary modules
from tkinter import *
from PIL import Image

# Creating the tkinter window
window = Tk()

# Setting window properties
window.config(background="white")
window.geometry("500x500")
window.resizable(0, 0)
window.title("Animation")
window.iconbitmap("logo.ico")

# Loading the GIF file and its frames
file = "animation.gif"
info = Image.open(file)
frames = info.n_frames
im = [PhotoImage(file=file, format=f"gif -index {i}") for i in range(frames)]

# Initializing count and anim variables
count = 0
anim = None

# Defining the animation function


def animation(count):

    global anim
    # Selecting the current frame
    im2 = im[count]
    # Updating the image of the label to show the current frame
    gif_label.configure(image=im2)
    # Incrementing the count variable to show the next frame in the next iteration
    count += 1
    # Resetting the count variable to 0 if all frames have been shown
    if count == frames:
        count = 0
    # Scheduling the next iteration of the animation function after 50 milliseconds
    anim = window.after(50, lambda: animation(count))


# Creating a label widget to show the GIF frames
gif_label = Label(window, image="")
gif_label.pack()

# Starting the animation
animation(count)

# Running the main loop of the window
window.mainloop()
