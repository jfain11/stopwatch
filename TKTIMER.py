# WORKING TIMER

import time
from tkinter import *

time_count = 0
root = Tk()
root.config(bg="lightgray")
root.title("Stopwatch")

running = False


def reset():
    global time_count
    global running
    running = False
    time_count = 0
    button["text"] = "Start"
    button["bg"] = "green"
    button["command"] = start_time


def stop():
    global running
    button2["state"] = DISABLED
    button["state"] = NORMAL
    running = True


def start_time():
    global running

    button2["state"] = NORMAL
    button["state"] = DISABLED
    button["text"] = "Reset"
    button["bg"] = "white"
    button["command"] = reset
    if not running:
        root.after(100, add_time)


def add_time():
    global time_count
    time_count += .1
    label["text"] = round(time_count, 1)
    if not running:
        root.after(100, add_time)


button = Button(root, text='Start', command=start_time, state=NORMAL, bg="Green", borderwidth=5)
button2 = Button(root, text='Stop', command=stop, state=DISABLED, bg="Red", borderwidth=5)

button.grid(column=1, row=0)
button2.grid(column=2, row=0)

button.config(font="Courier, 30")
button2.config(font="Courier, 30")

label = Label(root, text="0", bg="lightgray")
label.config(font="Courier, 30")
label.grid(column=1, row=2, columnspan=2)

root.mainloop()
