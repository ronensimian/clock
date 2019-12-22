import tkinter as tk
import time


def clock():
    current_time = time.strftime('%X, %A\n%d-%h-%Y')
    label1["text"] = current_time
    root.after(1000, clock)


root = tk.Tk()
root.title("Clock")
label1 = tk.Label(root, font="Alef 40", bg="black", fg="green", padx = 30, pady=5)
label1.pack()
button = tk.Button(root, text='Exit', font="Alef 13", bg="white", fg="blue", width=10, pady=3, command=root.destroy)
button.pack()
clock()
root.mainloop()
