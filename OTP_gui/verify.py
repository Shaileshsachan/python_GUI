import sys
from tkinter import messagebox

from tkinter import *
import time

b = sys.argv[1]
f1 = open('otp.txt', 'r')
b1 = f1.read()
f1.close()

if b == b1:
    f = open("status.txt", 'w')
    f.write('success')
    f.close()
    Window = Tk()
    Window.geometry('800x600')
    Window.title('Success')
    messagebox.showinfo('Congratulations', 'Your OTP was verified Successfully!!')
    Window.destroy()
    Window.mainloop()
else:
    f = open('status.txt', 'w')
    f.write('Failure')
    f.close()